Title: Writing Juju Charms on OSX
Date: 2014-03-06 11:03
Tags: juju, osx, vagrant, ubuntu
Slug: writing-juju-charms-on-osx
Category: Devops
Video: TSLJ22ntPQA

Developing charms on Ubuntu is an extremely straight forward process thanks to the addition of the local provider. LXC containers spin up quickly, integrate directly into your desktop OS, and leave you with very little configuration needed out of the box to get started.

What about users on OSX? What's their developer story like? The technical limitation is that OS X does not support operating system-level virtualization, like containers in Linux. The next best thing is to use a virtualization wrapper solution like [Vagrant](http://vagrantup.com)!

### Getting Started


To start you will want to ensure you've got the following tools installed on your development machine:

- [Homebrew](http://brew.sh)
- [Vagrant](http://vagrantup.com)
- [VirtualBox](https://www.virtualbox.org/)
- [Juju](http://juju.ubuntu.com)


#### Fetching the box
Head over to the [Juju Vagrant](https://juju.ubuntu.com/docs/config-vagrant.html) provider documentation. We'll need to fetch the latest basebox for Vagrant. I recommend using the precise basebox, or whatever the current LTS release vagrant image is.

```
vagrant box add JujuBox http://cloud-images.ubuntu.com/vagrant/precise/current/precise-server-cloudimg-amd64-juju-vagrant-disk1.box
```

This process takes a short while to complete, as its downloading a 200mb virtual machine image. Once its complete you can verify everything completed correctly by listing out the boxes that vagrant is tracking.

```
vagrant box list
```

If you see **JujuBox** listed, we're ready to proceed to the next step.

#### Preparing our local charm repository

We will need to create a directory structure that reflects the current standard for juju charm repositories. I recommend putting this in $HOME

```
mkdir -p charms/precise
```
Feel free to add any other LTS based target directory, for example if you were to target Trusty Tahr as a release for your charm, the command would be

```
mkdir -p charms/trusty
```
For the remainder of this tutorial, I will assume we are targeting Precise, as its the current LTS target of choice.

#### Installing Charm-Tools

Now is a good time to fetch Charm Tools. But what are charm tools you ask?

> Charm Tools offer a means for users and charm authors to create, search, fetch, update, and manage charms.

These can be installed via homebrew.

```
brew install charm-tools
```

#### Creating our first charm

Lets charm up GenghisApp - a single page MongoDB adminsitration app.

```
cd charms/precise
charm create genghis
```

This will create a skeleton structure of a charm ready for you to edit and populate with your services deployment and orchestration logic.

```
├── config.yaml
├── copyright
├── hooks
│   ├── config-changed
│   ├── install
│   ├── restart
│   ├── start
│   ├── stop
│   ├── upgrade-charm
│   └── website-relation-joined
├── icon.svg
├── metadata.yaml
├── README
└── revision

```

##### Writing the Charm
We'll start by editing the metadata.yaml to populate the information about our charm.

> **No Code displayed? refresh, there seems to be a bug with Gists in my theme**

<script src="https://gist.github.com/chuckbutler/9393419.js"></script>

Now that juju knows something about our service we're ready to start writing the hooks.

I'll include a few brief gists of the hooks for brevity

<script src="https://gist.github.com/chuckbutler/9393551.js"></script>

#### Preparing Vagrant

Since vagrant is going to be our work horse, we'll want to make sure its aware of all our charms, not just the current charm we are working on. With that in mind, we need to switch feet and prepare the environment since we are ready to test our Genghis service.

```
cd $home/charms
vagrant init JujuBox
vagrant up
```

![Vagrant Bootstrap](/images/2014/Mar/charles_Bushido__10_0_5_136____byobu_028.png)

You now have a Juju installation ready to be used for testing your charm on OSX, and a slick Juju-Gui to interface with your services. Validate that the GUI is accessible from http://localhost:6080

The password is output in your console feedback from the juju bootstrap.

##### Some important things to note about our vagrant environment

- Live charm repository directory mapping (all your charms in $HOME/charms are available in the /vagrant directory of our JujuBox
- We are running juju 1.16.6 at the time of this writing
- To interface with charms in our vagrant environment, we will need to `vpn` all our traffic into this virtual machine (more on that later)

### Deploying our charm in vagrant

You'll need to enter the juju environment we just bootstrapped in $HOME/charms

```
vagrant ssh
juju deploy --repository=/vagrant local:genghis
```

We are now free to watch progress through the GUI

![juju-gui](/images/2014/Mar/Juju_Admin___Google_Chrome_029.png)

When the Genghis badge turns green, we are ready to vpn our traffic through the vagrant image and interface with the Genghis server

### Routing traffic with sshuttle

Ensure that you have sshuttle installed, once installed you can skip the `brew install` line

```
brew install sshuttle
sshuttle -r vagrant@localhost:2222 10.0.3.0/24
```

When prompted for the password enter `vagrant` and you should see output similar to the following:

![](/images/2014/Mar/charles_Bushido__10_0_5_136____byobu_030.png)

Now we are free to connect to genghis. Open up the Genghis running unit list and click on the Genghis host, then click on the port 80 link in the service detail.

![](/images/2014/Mar/Juju_Admin___Google_Chrome_031.png)


![](/images/2014/Mar/Genghis___Google_Chrome_032.png)
#### Celebrate!

You've officially become a juju jedi padewon working with vagrant on OSX. Feel free to modify your charm code, and update. No more SCP'ing files to your linux server, or paying expensive cloud bills for development. With the live directory mapping provided by this vagrant setup, any edits you make to your files on the HOST operating system, are reflected in the guest.

Happy Hacking!
