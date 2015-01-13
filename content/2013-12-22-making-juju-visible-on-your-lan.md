Title: Making Juju visible on your LAN
Date: 2013-12-22 09:12
Tags: juju, networking
Slug: making-juju-visible-on-your-lan
Category: Devops

> ## Note: This article has been updated and verified to work on 14.04 on 11/02/2014

As I continue exploring the depths of Juju and what it offers I've outgrown using lynx to test my setups. Now that I'm running a Juju lab locally I figured its time to break the chains of the sandbox and make the services I'm deploying on my network visible to the machines on my LAN.

> **WARNING:** These instructions are intended to be run *before* you bootstrap your local environment. Do not attempt this on a running local provider - as you will lose connectivity to your units, and possibly break your local provider environment.

### Setting up the Bridge Adapter

```
$ sudo apt-get install bridge-utils
```

Edit your /etc/network/interfaces to make the bridge adapter load from your network DHCP server

```
auto br0
iface br0 inet dhcp
    bridge_ports eth0
    bridge_stp off
    bridge_fd 0
    bridge_maxwait 0

```

**Note :** You may need to change eth0 to your primary network adapter.

After making the edit you will need to restart the networking services

```
$ sudo /etc/init.d/networking restart
```

Edit /etc/lxc/lxc.conf and set lxc.network.link=br0

```
lxc.network.type=veth
lxc.network.link=br0
lxc.network.flags=up
```
Edit /etc/default/lxc-net and set:

- LXC_BRIDGE,
- LXC_ADDR,
- LXC_NETMASK,
- LXC_NETWORK,
- LXC_DHCP_RANGE &
- LXC_DHCP_MAX appropriately

for my LAN (10.0.2.0/24 type settings) now juju status shows 10.0.2.0/24 addresses for my units and I can access them over the LAN from another machine

```
USE_LXC_BRIDGE="false"
LXC_BRIDGE="br0"
LXC_ADDR="10.0.2.20"
LXC_NETMASK="255.255.255.0"
LXC_NETWORK="10.0.2.0/24"
LXC_DHCP_RANGE="10.0.2.50,10.0.2.99"
LXC_DHCP_MAX="49"
```
> Its very important to set `USE_LXC_BRIDGE` to false, commenting it out wont have the effect of setting it to "false" implicitly.

You will also need to specify the network bridge in your `$HOME/.juju/environments.yaml` file

```
  local:
    type: local
    # ... snipped for space
    # Override the network bridge if you have changed the default lxc bridge
    network-bridge: br0

```

Special thanks go to [Popey](http://askubuntu.com/users/612/popey) for this excellent AskUbuntu [question](http://askubuntu.com/questions/281530/how-do-i-run-juju-on-a-local-server?rq=1) and [answer](http://askubuntu.com/a/282415/6807) on how to do this with a Precise host.
