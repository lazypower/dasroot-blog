Title: Starbound with Fabric, Qemu, and SteamCMD
Date: 2013-12-22 02:12
Tags: fabric, python, deploy, qemu, steam
Slug: fabric-qemu-and-steamcmd
Category: Devops

Today has been quite a productive day for exploration of new tech. **Warning :** this post is going to be all over the place - and scoped to using fabric to bootstrap a host environment, install qemu, and setup a Game Server using SteamCMD.


## Fabric

Most of the juju tools are written in either python or go. This has lead me down the path of researching Python gearing up for my new position at Canonical on the Juju team. During that research I came across Fabric. A tool thats is by no means new to the sysadmin side of linux, but new to me.

#### What is fabric?

From the Fabric documentation:

> Fabric is a Python (2.5 or higher) library and command-line tool for streamlining the use of SSH for application deployment or systems administration tasks.

>It provides a basic suite of operations for executing local or remote shell commands (normally or via sudo) and uploading/downloading files, as well as auxiliary functionality such as prompting the running user for input, or aborting execution.

Fabric is essentially a system automation framework built in Python. As I'm starting to wrap my brain around Python, I realize that the tools provided are intended to be as light weight as possible. This really resonates with me, as I felt like Ruby + Gems were a really bloated way to gain functionality at the price of bringing the kitchen sink with you.

## Stitching server setup with Fabric

One thing I've found really annoying since I've landed back in Ubuntu land from a year long hiatus in Mac land is my serious lack of proficiency with shell scripting. I've attempted to write my own setup scripts for automating my [environment](https://github.com/chuckbutler/dotfiles/blob/master/scripts/bootstrap.sh) [setup](https://github.com/chuckbutler/dotfiles/blob/master/scripts/bootstrap.rb) a [few](https://github.com/chuckbutler/dotfilesv2/blob/master/setup_symlinks.sh) times. Each time I've tried to leverage something new I've learned like git submodules...

![What a disaster](/images/2013/Dec/disaster.jpg)

I really needed a one stop shop for bootstrapping both workstations and servers without going through the hassle of setting up complex chef-solo cookbooks and ensuring I had all those packed up into a git repository. Most of the time I just need pure ubuntu packages, some dotfiles and a handfull of applications I leverage to effectively maintain my servers.

Fabric lends itself really well to this. Lets write some bootstrap code for my newly installed Ubuntu Server

```
#!/usr/bin/env python

from fabric.api import env, run, sudo, local

env.hosts = [ '10.0.2.158' ]
```
We have the python shebang, importing modules from the fabric api, and setting our network hosts to execute commands on.

Now let's add tasks for upgrading the server remotely, and bootstrap our user on the remote machine.

```
def bootstrap_server():
    sudo('apt-get install vim git-core htop python-software-properties -y')
    run('git clone https://github.com/chuckbutler/dotfilesv2.git .dotfiles')
    run('ln -s .dotfiles/dotvim .vim')
    run('ln -s .dotfiles/dotvimrc .vimrc')
    run('ln -s .dotfiles/gitconfig .gitconfig')
    run('ln -s .dotfiles/githelpers .githelpers')


```

This function fetches a handfull of utilities I require on most of my systems, and clones my dotfiles repository on the machine, sets up the symlinks to get everything working.

###### What you should see:

```
$ fab bootstrap_server
[10.0.2.158] Executing task 'bootstrap_server'
[10.0.2.158] sudo: apt-get install vim git-core htop python-software-properties -y
[10.0.2.158] out: sudo password:
```

Paydirt! Its executing and has halted on the remote system in interactive mode, prompting me to enter the sudo password before it installs the packages. I like where this is going.

![Devops Borat says Great Success!](/images/2013/Dec/devops_borat_tells_it_like_it_is.png)

Skipping ahead through some dev cycle debugging, we know our next step is to get QEmu installed and running.

#### Criteria
- Install the QEmu packages
- Add user to libvirt security group so we can manage QEmu VM's remotely

```
def setup_qemu(user="charles"):
    sudo('apt-get install qemu-kvm libvirt-bin bridge-utils -y')
    sudo('adduser' + user + 'libvirtd')
    local('sudo apt-get install virt-manager')
```

**Note :** You don't need to have the `local('sudo apt-get install virt-manager')` line to install QEmu on your server. I added this as it stands to reason if I'm running this against a server its on a workstation and will only be run once. May as well grab 2 tasks with a single function.

## QEmu - Virtualization


#### Setup ISO Repository

We will need to import ISO images for QEmu to install virtual machine images from. I don't like to script this portion of setup as the images will invariably change, and I don't really need to keep a mass repsoitory on every QEmu machine. Your needs may vary, and fabric makes this dead simple.

```
$ ssh nexus mkdir iso
$ ssh nexus wget http://releases.ubuntu.com/precise/ubuntu-12.04.3-server-amd64.iso`
```

#### Setup Bridged Networking

###### The following instructions are to be treated as a generic overview of how I enabled bridged networking and is in no way comprehensive or complete. You could break your networking if this is done improperly. You have been warned.

Following the Ubuntu Community documentation [here](https://help.ubuntu.com/community/KVM/Networking) You will need to make some minor system edits:

```
$ sudo apt-get install libcap2
$ sudo setcap cap_net_admin=ei /usr/bin/qemu-system-x86_64
```
*note* I'm not positive this is required according to [this](http://askubuntu.com/questions/179508/kvm-bridged-network-not-working) AU post.


You will need to create the Bridged device for QEmu to route requests through. This is achieved with the `bridge-utils` package and adding the following to `/etc/networking/interfaces`

```
auto br0
iface br0 inet dhcp
    bridge_ports eth0
    bridge_stp off
    bridge_fd 0
    bridge_maxwait 0

```
Reboot and your newly made QEmu images will be able to be independent units on the network.



Lets bootstrap a new machine for the Starbound Server. Fire up virt-manager

![Start up VirtManager](/images/2013/Dec/virt_manager.jpg)


Connect to your QEmu server
![Connect to QEMU](/images/2013/Dec/Selection_002.png)

**Note:** You may need to enter the IP Address of your remote server in the Hostname field unless you have mapped them via DNS, /etc/hosts or through other means of DNS Resolution.

Create a new machine
![Create new machine](/images/2013/Dec/Selection_003.png)

Set the Installation Media
![Set installation media](/images/2013/Dec/Selection_004.png)

Set your hardware constraints
![Set Constraints](/images/2013/Dec/Selection_005.png)

Allocate Space for the root disk
![Root Disk space](/images/2013/Dec/Selection_006.png)

Finalize Settings including our Bridged networking device
![Finalize w/ bridged networking device](/images/2013/Dec/Selection_007.png)

Click Finish and install Ubuntu Server as normal


### Starbound Dedicated Server via SteamCMD

Now onward with the real reason we started this adventure. To setup a dedicated Starbound Server.

Steam is my preferred method of fetching updates for Starbound since it uses the SteamPipe CDN its quick and painless. SteamCMD makes setting up dedicated servers a snap for updates.

If you are unfamilar with SteamCMD, go read [this](https://developer.valvesoftware.com/wiki/SteamCMD) first.

#### Installing SteamCMD with Fabric


```
def bootstrap_starbound(username="",password=""):
	sudo('apt-get install lib32gcc1')
	run('wget http://media.steampowered.com/installer/steamcmd_linux.tar.gz')
	run('tar xvfz steamcmd_linux.tar.gz')
	run('$HOME/steamcmd.sh +login ' + username + ' ' + password + ' +force_install_dir ./starbound/ +app_update 211820 validate +quit')
```

To do this proper you will need to set your env.hostnames like we did above to include the IP of our newly provisioned starbound virtual machine.

With all this completed. you now have your own dedicated Starbound server provisioned by steam.

**-- Will update later with fabric config to start/stop the starbound server --**


Until then, Go Forth and Conquer traveller.
![Starbound](/images/2013/Dec/starbound.jpg)
