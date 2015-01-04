Title: Container Networking with Flannel
Date: 2014-12-16 19:12
Tags: juju, networking, planet, flannel, lxc, video
Slug: container-networking-with-flannel
Category: Devops
summary: When leveraging juju with LXC in cloud environments - networking has been a constant thorn in my side as I attempt to scale out farms of services in their full container glory. Thanks to the work by [Hazmat](http://blog.kapilt.com/) (who brought us the [Digital Ocean Provider](/juju-digital-ocean-awesome)) - there is a new development in this sphere ready for testing over this holiday season.
video: bCvl-TsxVXA


When leveraging juju with LXC in cloud environments - networking has been a constant thorn in my side as I attempt to scale out farms of services in their full container glory. Thanks to the work by [Hazmat](http://blog.kapilt.com/) (who brought us the [Digital Ocean Provider](/juju-digital-ocean-awesome)) - there is a new development in this sphere ready for testing over this holiday season.

### Container Networking with Juju in the cloud

Juju by default supports colocating services with LXC containers and KVM machines. LXC is all the rage these days, as linux containers are light weight kernel virtualized cgroups. Akin to BSD Jails - but not quite. Its a awesome solution where you dont care about resource isolation, and Just want your application to run within its own happy root, and live on churning away at whatever you might throw at it.

While this is great - it has a major achilles tendon presently in the Juju sphere. Cross-host communication is all but non-existant. In order to really scale and use LXC containers you need a beefy host to warehouse all the containers you can stuff on its disk. This isn't practical in scale out situations where your needs change on a day to day basis. You wind up losing out on the benefits of commodity hardware.  

Flannel knocks this restriction out with great justice. Allow me to show you how:

### Model Density Deployments with Juju and LXC

I'm going to assume you've done a few things.

- Have a bootstrapped environment
- Have at least 3 machines available to you

Start off by deploying Etcd and Flannel


    juju deploy cs:~hazmat/trusty/etcd
    juju deploy cs:~hazmat/trusty/flannel
    juju add-unit flannel
    juju add-relation flannel etcd

> **Important!** You must wait for the flannel units to have completed their setup run before you deploy any lxc containers to the host. Otherwise you will be racing the virtual device setup, and this may misconfigure the networking.

With Flannel and Etcd running, you're now ready to deploy your services in LXC containers. Assuming the Flannel machine's provisioned by Juju are machineid 2, and 3:

    juju deploy cs:trusty/mediawiki --to lxc:2
    juju deploy cs:trusty/mysql --to lxc:3
    juju deploy cs:trusty/haproxy --to 2
    juju add-relation mediawiki:db mysql:db
    juju add-relation mediawiki haproxy

> **Note** We deployed haproxy to the host, and not to an LXC container. This is to provide access to the containerized services from the public interface - flannel only solves cross-host private networking with the containers.

This may take a short while to complete, as the LXC containers are fetching cloud images, and generating templates just like the Juju local provider workflow. Typically this is done in a couple minutes.

Once everything is online and ready for inspection, open a web-browser pointed at your Haproxy public ip, and you should see a fresh installation of Mediawiki.

Happy hacking!
