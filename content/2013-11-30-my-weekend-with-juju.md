Title: My Weekend with JuJu
Date: 2013-11-30 13:11
Tags: juju, weekend-hacks
Slug: my-weekend-with-juju
Category: Devops

<center>![Ubuntu Juju](http://design.canonical.com/wp-content/uploads/2011/10/juju-464x252.png)</center>

This Thanksgiving weekend I'm experimenting with Juju. I fell in love with the web based configurator with all its relation dragging goodness. Its awesome to know that the recipe's building the services underneath have been audited by a very dedicated community to ensuring I'm running worry free with the most up-to-date standards in installing this particular application stack.



For those of you that dont know Juju is Canonical's cloud orchestration framework. It sits a layer above any particular provisioner (meaning you can consume chef-solo, puppet, bash scripts, docker, or salt to name a few) to build scalable application stacks.

The side of Juju that really 'clicks' with me is the flexibility to use whatever language you're most comfortable with. If you've got a ton of experience in spinning up your application servers with Bash, you can keep doing what you're doing. Re-tool the script to run within Juju's hook system and you're ready to start hacking around.

Before this turns into an elevator pitch, I'm going to assume you're interested and want to get started. Head on over to the [Official Juju Installation Instructions](https://juju.ubuntu.com/docs/getting-started.html) and spin up your local development environment powered by LXC containers (use the local provider).  

#### TLDR; Install Ubuntu 13.10

## Step 1
### Install juju, and setup for Local Deployment

    sudo add-apt-repository ppa:juju/stable
    sudo apt-get update && sudo apt-get install juju-core
    sudo apt-get install juju-local


    juju generate-config
    juju switch local
    sudo juju bootstrap


To understand what just happened - see [LXC provider Juju documentation](https://juju.ubuntu.com/docs/config-local.html)



## Step 2
### The spiffy Gui

	juju deploy juju-gui

This will deploy the Graphical configuration tool for Juju, allowing you to "shop" for applications within the Charm Store. You can deploy any of the offerings to the Local Provider from this Gui with Drag and Drop simplicity.

![](/images/2013/Nov/Screenshot_2013_11_30_13_20_44.png)


While the GUI is not a requirement for using Juju, I like the visibility it provides into the stack's I'm creating. I've come to lean on using the GUI and the watch command with juju status.

## Step 3
### Don't forget the tools!
You'll also want to grab a copy of the latest charm tools for assiting in charm authoring.

	sudo apt-get install charm-tools




### Information Radiator

Pairing the watch command with juju status will continually monitor the information that juju status spits back to STDOUT - this effectively turns your console into an information radiator of whats going on within your Juju environment.


	watch juju status

![](/images/2013/Nov/Screenshot_2013_11_30_17_46_58.png)




#### *observation
So far I see a 100% improvement in documentation coming from my experience with Juju in 2011. The documentation has covered everything we needed to get started:

- Adding the Juju PPA
- Installation of charm-tools from the official repository
- Deploying the GUI.

### Picking a Charm


Juju has a ton of requests for charms already. This is a great place for new charmers to get started in their quest to join the Juju ecosystem.

#### [Open Charm Queue](https://bugs.launchpad.net/charms/+bugs?field.searchtext=&orderby=-importance&field.status%3Alist=NEW&field.status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INCOMPLETE_WITH_RESPONSE&field.status%3Alist=INCOMPLETE_WITHOUT_RESPONSE&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_commenter=&field.subscriber=&field.structural_subscriber=&field.component-empty-marker=1&field.tag=&field.tags_combinator=ANY&field.status_upstream-empty-marker=1&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field.affects_me.used=&field.has_no_package.used=&field.has_patch.used=&field.has_branches.used=&field.has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&field.has_blueprints.used=&field.has_blueprints=on&field.has_no_blueprints.used=&field.has_no_blueprints=on&search=Search)

If you notice an open request for a charm, assign it to yourself and prepare to get your hands dirty. For the purpose of this tutorial I chose the charm [Papertrail](https://bugs.launchpad.net/charms/+bug/1023665)

Looking over the charm, it makes perfect sense to integrate this as a Subordinate Charm. As a little background, papertrailapp is a hosted log management service. They utilize rsyslog style log routing, and aggregate logs for major players like GitHub, AirBrake, and more. Its easy to setup, provides awesome retention and a powerful searchable dashboard across all of your tracked logs.

#### An aside on subordinates

The following excerpt from the [Juju documentation](https://juju.ubuntu.com/docs/authors-subordinate-services.html) explains this nicely:

>Services are composed of one or more service units. A service unit runs the service's software and is the smallest entity managed by juju. Service units are typically run in an isolated container on a machine with no knowledge or access to other services deployed onto the same machine. Subordinate services allows for units of different services to be deployed into the same container and to have knowledge of each other.

What this means to you: You don't have to provision another server to run this charm. It "bolts" on to an existing container, providing the functionality of the charm within that running container.

[Read part 2 >> ](/writing-the-papertrail-charm/)
