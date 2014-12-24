Title: Cooking the Errbit charm with Chef
Date: 2013-12-14 23:12
Tags: juju, errbit, rails, app-deployment, juju-strano
Slug: cooking-the-errbit-charm-with-chef
Category: Devops

My good friend [Marco Ceppi](http://marcoceppi.com) sent me a link to a github repository for Juju Chef Helpers : [https://github.com/Altoros/juju-charm-chef](https://github.com/Altoros/juju-charm-chef)

I have to admit, I'm really happy this was here. I was brain bending around how I was going to try to integrate chef as my provisioner of choice. At first glance its a pure abstraction of the chef provisioner in charm hook format. Each aspect of the charm correlates to a chef cookbook and associated recipes.


![](/images/2013/Dec/interesting_call_tracking.jpeg)


## Translating the hooks

Changing installation from a Bash script to the current incantation in chef was a learning curve. I tried to keep myself away from consuming too many cookbooks since I wanted to display a reliance on being clever and understanding the application I was packaging and not demonstrating pure use of chef. This may change in the near future.

### Install

```
#include the apt cookbook for the LWRPS
include_recipe "apt"

# Add the 10gen repository for MongoDB
apt_repository "mongodb-10gen" do
  uri "http://downloads-distro.mongodb.org/repo/ubuntu-upstart"
  distribution "dist"
  components ["10gen"]
  keyserver "keyserver.ubuntu.com"
  key "7F0CEB10"
end

```
So far so good in straightforwardness. This is the prep work for the installation of MongoDB

```
package "mongodb-10gen" do
  action :install
  not_if { File.exist?("$CHARM_DIR/.mongodb") }
end

#install dependencies
package "libxslt-dev" do
  action :install
end

package "libxml2-dev" do
  action :install
end

package "nginx" do
  action :install
end

```

Package installation  - notice the ` not_if File.exist ` statement above. We are checking for a sentinel that tells us if the mongodb relationship is present.

```
user "errbit" do
  shell "/bin/bash"
  home "/home/errbit"
  system true
  supports :manage_home => true
  action :create
  uid 3000
end

git "/home/errbit/errbit" do
  repository config_get['repository']
  reference config_get['release']
  action :sync
end

juju_port 80 do
  action :open
end

execute "chown -R errbit:errbit /home/errbit/errbit" do
  action :run
end

```

and finally setup the application user, clone the source code, and open port 80







### Config-Changed

```
#drop the templates
template "/home/errbit/errbit/config/config.yml" do
  owner "errbit"
  group "errbit"
  mode "0660"
  source "config.yml.erb"
  variables({
   confirm_resolve: config_get['confirm_resolve'],
   gravatar: config_get['gravatar'],
   smtp_host: config_get['smtp_host'],
   smtp_domain: config_get['smtp_domain'],
   smtp_port: config_get['smtp_port'],
   smtp_starttls_auto: config_get['smtp_starttls_auto'],
   smtp_user: config_get['smtp_user'],
   smtp_pass: config_get['smtp_pass']
   })
end

  template "/home/errbit/errbit/config/mongoid.yml" do
    owner "errbit"
    group "errbit"
    mode "0660"
    source "mongoid.yml.erb"
    variables({ mongo_uri: "mongodb://localhost:27017/errbit" })
    not_if { File.exists?("$CHARM_DIR/.mongodb") }
  end

#delete existing upstart templates if they exist
template "/etc/init/errbit.conf" do
  action :delete
end

template "/etc/init/errbit-web.conf" do
  action :delete
end

#setup upstart templates
template "/etc/init/errbit.conf" do
  action :create
  owner 'root'
  group 'root'
  mode '0644'
  source 'errbit.conf.erb'
end

template "/etc/init/errbit-web.conf" do
  action :create
  owner 'root'
  group 'root'
  mode '0644'
  source 'errbit-web.conf.erb'
end


template "/home/errbit/errbit/config/unicorn.rb" do
  action :create
  owner 'errbit'
  group 'errbit'
  mode 0644
  source 'unicorn.rb.erb'
  variables({
    unicorn_workers: config_get['unicorn_workers']
  })
end


#setup the NGINX configuration
template "/etc/nginx/sites-available/errbit" do
  action :create
  owner 'root'
  group 'root'
  mode 0644
  source 'errbit-nginx.erb'
  variables({
    hostname: config_get['hostname']
  })
end

link "/etc/nginx/sites-enabled/errbit" do
  action :create
  to "/etc/nginx/sites-available/errbit"
end

#TODO: document that we remove the default nginx vhost
link "/etc/nginx/sites-enabled/default" do
  action :delete
end


```
config-changed starts out populating a majority of the templates we need in order to run in our juju environment. Sets up the database connection template, the nginx config, unicorn config, all the stuff we normally leave to capistrano

```


#Prep the post-deployment script to circumvent chef's personality conflicts
template "/tmp/bundler.sh" do
  action :create
  owner 'errbit'
  group 'errbit'
  mode 0777
  source 'bundler.sh.erb'
end

```
This is where I had difficulty. I didn't know how to complete the deployment in chef. So I cheated and built a shell script to handle calling all the rake tasks we want to be executed as wrap up of the deployment.

*NOTE* : I also ran into an odd issue - when running bundle install from the execute resource within chef, it always ran in the $CHARM_DIR re-packing the chef-solo Gemfile.lock in deployment mode. This warrants further investigation


Ok cool, we're setup with errbit. Chef has taken care of most of the heavy lifting.

If you want to see the templates, you can view them from the [github repository](https://github.com/chuckbutler/errbit-charm-chef)


### Relationship Hook Sequence

Relationship hooks are processed anytime a relationship joins, parts, or changes configuration. This is where you can make real magic happen. For example the wordpress charm speaks from the Wordpress unit to the connecting MySQL database unit to provision a user, generate a password, and hand that data back across the wire to populate wordpresses configuration files.

In order to fully consume this, you have to know which hooks are called during the `juju add-relation` phase, and the `juju remove-relation` phase.

### juju add-relation


#### mongodb-relation-joined

as the MongoDB unit and the Errbit unit have a relationship added, we need to dump the MongoDB Database in /mnt to take advantage of cloud storage.

```
#cleanup any stale dumps residing in ephemeral storage
directory "mnt/mongo-data" do
  action :delete
end

directory "/mnt/mongo-data" do
  action :create
end

execute "mongodump" do
  command "mongodump -h localhost -d errbit -o /mnt/mongo-data"
end
```

#### mongodb-relation-changed

The relation-changed hook will be run everytime the remote system receives a configuration change, and is also the last hook executed during the `juju relation-add` phase of hook execution.

My first challenge was figuring out how I was going to fetch the relationship information from MongoDB. Since Mongodb by default doesn't require db user accounts, its a safe assumption to just use the host credentials in the MongoDB URI

All of the information required to build the relationship is defined by the interface of the connecting MongoDB unit. This information is provided to us by the Juju Helpers cookbook through `relation_get`


```ruby
=> {"hostname"=>"10.0.3.233",
 "port"=>"27017",
 "private-address"=>"10.0.3.233",
 "replset"=>"myset",
 "type"=>"database"}
```

```
require 'securerandom'

mongodb = {
	host: relation_get['hostname'],
	port: relation_get['port'],
	database: 'errbit'
	}

# This failout condition will do nothing
# if we cannot find the relationship details.

if [:host, :port].any? { |attr| mongodb[attr].nil? || mongodb[attr].empty? }
  juju-log("Waiting for all attributes to be set")
else

  template "/home/errbit/errbit/config/mongoid.yml" do
    variables({
      mongo_uri: "mongodb://#{mongodb[:host]}:#{mongodb[:port]}/#{mongodb[:database]}",
    })
    user 'errbit'
    group 'errbit'
    mode '0644'
    source "mongoid.yml.erb"
    cookbook "errbit"
    action :create
  end

  #deploy the backup data
  execute "mongorestore" do
    command "mongorestore -h #{relation_get['hostname']} -d errbit /mnt/mongo-data/errbit/"
  end

  service 'errbit' do
    ignore_failure true
    provider Chef::Provider::Service::Upstart
    action :restart
  end

  package "mongodb-10gen" do
    action :purge
  end

  execute "touch $CHARM_DIR/.mongodb" do
    action :nothing
  end

end


```
Great, with this portion completed, we now have our charm deploying the application, and migrating data from the local database if any was accrued, and pushed that to the remote MongoDB provider.


<!--

#### Links about Backup/Restore on MongoDB

- [Slide Share from 10gen](http://www.slideshare.net/mongodb/mongo-boston2012backuprestore)

-->
