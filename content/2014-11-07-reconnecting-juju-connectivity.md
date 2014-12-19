Title: Reconnecting Juju Connectivity
Date: 2014-11-07 11:11
Tags: juju, planet
Slug: reconnecting-juju-connectivity
---
When disaster strikes, the first instinct is to panic right? You don't need to panic just yet when your IT staff has come to you, the devopsy admin sent from the future with cool tools, and tells you that there is a new networking policy change. And every one of your units are going to under go an IP Refresh, and domain change. 

Juju uses flat files to store configuration on your workstation, and the nodes, so all you need to do is do some note taking on what the IP is to your bootstrap node - and juju will take care of the rest for you.

---


### Restoring connectivity to the state server from your client workstation

You will need to edit the `jenv` that juju created for the environment during `juju bootstrap` which will be located: `$JUJU_HOME/environments/<environment_name>.jenv`

The `jenv` has a yaml file format, so be familiar with that so you know what to look for:

    state-servers:
    - 173.173.4.187:17070
    - 172.187.3.21:17070

Each line item below `state-servers` will need to be updated with the new state servers address. You may have one or more listed here depending on if you did `juju ensure-availability` - which will turn a single node state server into a High Availability state server.

### Restoring connectivity to the state server from juju-agents

There will be 2 or more configuration files to edit per agent. 

 - 1 for the machine
 - 1 for each unit-agent of service you deploy to the machine

Given the scenario:

    juju deploy elasticsearch

You will have 2 files to edit - the Machine conf, and the elasticsearch conf. If you have co-located any services on the machine you will have an additional config per service added to the machine. (Dont forget about KVM and LXC containers, as this also increases the number of conf files to edit, and will reside in that services container)

You will find the Machine configuration in `/var/lib/juju/agents/machine-1/agent.conf` 
You will find the service configuration in `/var/lib/juju/agents/unit-elasticsearch-0/unit.conf`

 then kill jujud and let upstart restart it


This has all been documented on [AskUbuntu](http://askubuntu.com/questions/540209/ip-domainname-of-juju-master-or-slaves-changes) with the user that joined #juju on irc.freenode.net - trying to discover how to do this themselves. If you've got the time, give them a quick upvote for a great question/answer

