Title: Replacing U1 with OwnCloud on Digital Ocean
Date: 2014-04-22 19:04
Tags: juju, owncloud, digitalocean, ubuntu, planet
Slug: replacing-u1-with-owncloud-on-digital-ocean
Category: Community

Juju is an enterprise grade system orchestration tool. But, that doesn't mean its only place is in some big fortune 500 company. Juju helps me in my day to day orchestration of the webapps that power my home, and pet projects. I've come to rely on using Juju to orchestrate all of my deployments whether personal or commercial.

So, with that being said - when Canonical announced they would be closing down the Ubuntu 1 file store, I started looking for a replacement. This was a perfect opportunity for OwnCloud to step in and take up some of that slack. Their official announcement was right on the heels of the closing post of U1, and this was enough to grab my attention.

Several late nights were put into helping [Jose](http://joseeantonior.wordpress.com/2014/04/11/owncloud-charm-updated/) develop the new revisions to the [OwnCloud Charm](https://jujucharms.com/sidebar/search/precise/owncloud-13/?text=owncloud), and I piloted it every step of the way. We're rounding the 98% completion mark - only pending SSL integration into the charm so its secure by default.

Without further adeu, Lets deploy Owncloud on Digital Ocean for 30 gigs of cloud storage for $10 USD a month, orchestrated, and updated by Juju.

## Configuring Juju to talk to Digital Ocean
To get started, we'll need to gather some of the requirements.

Ensure you've got the latest juju stable release. At the time of this writing, its 1.18.1

	sudo add-apt-repository ppa:juju/stable
    sudo apt-get update
    sudo apt-get install juju
    juju generate-config

Next you'll need to fetch a plugin.

[Hazmat's Digital Ocean provider plugin](https://github.com/kapilt/juju-digitalocean)  from PyPi :

	pip install -U juju-docean

With the Digital Ocean plugin installed, we'll need to add DO to our environments.yaml

    digitalocean:
        type: manual
        bootstrap-host:  null
        bootstrap-user: root

We'll also need to add our API credentials as an environment variable. According to the installation readme, a good place to put this would be in ~/.bashrc

    export DO_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    export DO_CLIENT_ID=xxxxxxxxxxxxxxxxxxxxx

You can find these on your Digital Ocean Account page:

![](/content/images/2014/Apr/DO_API.png)


### Bootstrapping our DO Service

	juju switch digitalocean
    juju docean bootstrap --constraints="mem=1G region=nyc2"

This will communicate with the DO API and provision a droplet for you with 1G of memory. The bare minimum to warehouse both the bootstrap node, AND our fileserver.

## Deploying OwnCloud

Now that we've gotten all the hard stuff out of the way. We're ready to deploy and configure OwnCloud.

	juju deploy owncloud --to 0

This deploys owncloud to our bootstrap node. This is not the *ideal* solution, but I wanted to consume 1 node, and didn't really care about scale-out for OwnCloud. My particular setup will be one user, many devices. And 30GB of storage is plenty to replace my free 5GB provided by U1.

#### Caveats to deploying on your bootstrap node

This will limit your ability to scale, and you'll lose some disk space to the juju components and logs. You've been warned that while this works, its not a recommended practice for any other Juju Deployments.

#### Notes on configuration

Owncloud supports 2 backends. It deploys as a standalone service with SQLite DB support, and supports MySQL as the backend for scale out usage. Since I'm a single user, and I'm not planning on scaling out, we're done configuring owncloud from Juju - as everything is setup on first login when its deployed as a stand alone service.


### Setup Owncloud

Connect to the deployed owncloud server by opening a browser and connecting to the public IP of your owncloud instance. You can discern the public IP of your OwnCloud by running `juju status`

	  owncloud/0:
        agent-state: started
        agent-version: 1.19.0
        machine: "0"
        open-ports:
        - 80/tcp
        public-address: 172.22.13.173

On first run, you will be prompted to define your administrative user. The remainder of the settings while tempting to tweak - should be left as their defaults.

![](/content/images/2014/Apr/do_first_run.png)

With the server component completed. Lets take a look at getting the rest of the ecosystem setup, starting with the PC.


## Connecting OwnCloud to your PCs

OwnCloud provides a client app available from the Ubuntu Software Center

![](/content/images/2014/Apr/owncloud_client_software_center.png)

Easily installed via apt

	sudo apt-get install owncloud-client

![](/content/images/2014/Apr/do_client_screen-1.png)

The configuration here is very straight forward, and can mimic the U1 behavior if you opt out of picking a "parent" sync directory to sync all your files. You'll need to start with that configuration, but remove it and pick individual directories to sync, with a corresponding directory on the owncloud server. See the example above.


## Replacing the Mobile Component

Owncloud sync doesn't have to just stop at your desktop. I explored some of the offerings in the Google Play store to build the story for replacing U1 on the phone with OwnCloud.


#### Files

The primary task of ownCloud is, of course, file storage and sharing. ownCloud implements WebDAV interface to serve files. This means that you can use any of WebDAV applications available in Google Play which are plenty. There is an official application which costs $1 and doesn't do a lot, but is nice to have anyway. It allows you to view your cloud directories and download individual files for offline usage (similar to Dropbox and Google Drive clients). As a pleasant bonus, it provides Instant Upload feature for your photos, so if you tick the respective checkbox your pics will be automatically uploaded to your cloud (instead of Google+).

Because I required something more automatic, I installed FolderSync Lite to synchronize cloud folders with those on the device. It operates the same as desktop ownCloud client - you specify folders you want to synchronize and respective local directories, sync interval, overwrite policies etc etc; and it will download/upload files in these folders according to the rules. There is also a paid version of the app, but I don't really notice the limitations of the free one.

#### Calendar

Calendar functionality in ownCloud is done using… wait for it… CalDAV. As always, we head to the Play Market and shell out another three bucks for [CalDAV-Sync](https://play.google.com/store/apps/details?id=org.dmfs.caldav.lib).This one does what it is supposed to do, with no real complaints. The Android stock Calendar suffices completely.

A small hack I had to employ on the server side because ownCloud does not support iCal subscriptions. The solution is vividly described [here](http://forum.owncloud.org/viewtopic.php?f=8&t=11576). Basically you have to set up a cron job that fetches calendar entries from the link and pushes them to ownCloud via CLI WebDAV client cadaver.

#### Music

OwnCloud can store your music and play it in the browser. But what's more cool is that it can stream music via Ampache, and then you can listen to this stream using any Ampache-included music player. I haven't got to using this feature just yet, as I don't want to fill all my DO-provided storage with music (and it will take a while too). But having a personal Spotify sounds like a fun idea to me.

## Final Thoughts

Managing and book-keeping all your data yourself is partly a vanity endeavor. You spend a good chunk of time on stuff you otherwise wouldn't do. But in the end of the day the warm fuzzy feeling of having everything under your control makes it worth the struggle. This, and the ability to backup all your data in a single shell command. So be safe, be aware.
