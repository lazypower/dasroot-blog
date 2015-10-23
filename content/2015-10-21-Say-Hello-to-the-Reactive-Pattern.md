Title: Charming 2.0 - Now with 100% more awesome
Date: 2015-10-22 10:41
Tags: devops, juju, reactive, charms, charming, layers, planet
Slug: 2015-charming-2-point-oh
Category: devops
Status: published
Image: /images/2015/oct/reactive-hero.png


<iframe width="420" height="315" src="https://www.youtube.com/embed/aRQcERLnbIQ" frameborder="0" allowfullscreen></iframe>

> Editors Note: This post is one of many in a series covering the new
> patterns in charming. This first post will be information heavy and
> cover a walkthrough of the techonologies at play. Video content and
> additional tutorials will follow.

It's been an exciting couple of months for the Juju Charmers. If you've been
following the Juju mailing list, you've undoubtedly seen some mention of the
newest features landing for writing charms which takes aim at easing the
maintenance burden for charm authors by exposing a pattern of layering and
reacting to charm events. This packs a one two punch at complexity and has
literally re-defined charming in a very short span of time.

If you've written charms before now, you'll know that it requires a fairly deep
knowledge of the hook environment, how these hooks are run, and what sequence
they may be run in. This hook execution pattern is deeply tied to how we model
services in Charms and lends itself to a barrier to entry for new charm authors.
There's not inherently wrong with the pattern, it was just a steep learning
curve to ask newcomers to learn. The newest framework - The Reactive Pattern -
allows charm authors to perform actions in familar hook contexts, or to surface
events - such as a database coming online, and then subscribe to those events
with decorators on plain ole methods.



## Setting the Stage, the Players

Each is a stand alone component, and almost certainly should be used in tandem.
Like the unix philosophy, this tooling/library has been written in mind to perform
only its job, and to do it well. I'd also like to take a moment to point out
these features were developed by [Ben Saller](https://github.com/bcsaller) and
[Cory Johns](https://github.com/johnsca) of the Juju ecosystems team. If you see
them in IRC or on the Mailing list, be sure to give them a friendly hi5 for
their awesome work.

### Charm Layers

Charms can be seen as a build-time artifact on the workstation machine. As a
developer of many charms, its surfaced that when charming in a particular domain,
say PHP website creation, I constantly need to setup apache (or nginx) and the
php5-fpm daemon. Tuning these can be application specific, but normally I just
set them up, and start modeling the application deployment. But I cannot do
anything until this plumbing is complete.

Charm Layers solve for the complexity of abstracting away these common tasks
into their own modules, which can then be called, included, and
overridden in complimentary layers. I know this is an exercise in spacial thinking.
So lets take a look at how this fits together, first by looking at how we can
eliminate boiler plate. (this has a minor overlap with Reactive Charming, as
this example will illustrate layering a reactive based charm)

    includes: ['layer:basic']

Fig 1.1 - `layer.yaml`

By having a directory with only a layer.yaml, we can now build a charm that
does nothing, however we've elminated the need for `charm create` and editing
boilerplate code. This allows us a far simpler declarative syntax to write charms.

To assemble this noop boilerplate charm, we simply run `charm build -o path/to/juju_repo`

    builder: Continuing with known changes to target layer. Changes will be overwritten
    builder: Processing layer: layer:basic
    builder: Processing layer: test

Fig 1.2 - Charm Builder Output

We now see that it pulled in the `layer:basic` charm layer (or in other words
boilerplate) and its applied our test layer on top. Pretty neat! Using a domain
that I am commonly involved with, Charming with Docker, I placed a diagram
in the [Documentation](https://jujucharms.com/docs/stable/authors-charm-with-docker)
that helps illustrate exactly how this looks. Included below in Fig 1.3.

![](https://jujucharms.com/static/img/jujudocs/1.24/charm-layers-decomposed.png)
Fig 1.3 - Layer Diagram

We see that there are dependent, and extensive layers. This is the best
representation I could put together to show how the nginx container layer
extends the "middle" docker layer. To explore how these concepts work, we
need to look to our next utility - the **Reactive Pattern**

##### Inspecting Assembled Charms

By running `charm layers` in the directory of the assembled charm, you will be
presented with a color coded map of where the files being included came from.
This is particulary handy when inspecting a charm to see which layers were
included, and how it impacted the overall architecture of the charm.

![Charm Layer Inspector](/images/2015/oct/charm-layers.png)



### Payload Management

> This is a new feature as of juju 1.25 beta2 and is not currently in any of the
PPA branches for distribution (stable, or devel). This should be landing soon
for mass consumption.


The Juju Core Moonstone team has been working dilligently to deliver a new
feature that is exciting to me as a charmer of dockery type things. Payload
Management is a suite of hook utilities to register launched payloads, such as:

- LXD Containers
- Docker Containers
- KVM Guests
- Tomcat WAR files

And a myriad of other arbitrary payload classes in charms. While the charm
surfaces a service to the topology, its often important to me as an admin to
know what exactly is running on the machine underneath this service abstraction.
Perhaps 4 complete microservices make up a single service endpoint in my topology.

`juju list-payloads`

    [Unit Payloads]
    UNIT           MACHINE PAYLOAD-CLASS STATUS  TYPE   ID             TAGS
    unit-idlerpg-0 1       slackbot      running docker 6dd92ba0
    unit-idlerpg-0 1       application   running docker 5cfde4b5
    unit-idlerpg-0 1       monitoring    running docker db3as541

In this particular example, there are two services comprising the IdleRPG service,
launched on machine 1. The Slackbot container, and an NGINX application container
serving up the rules and the map, and finally a monitoring process - CADVISOR
listening to the docker socket and tracking resource usage.

I now have at a glance statistics of whats happening with my delivered payloads.
Pair this in an update-status hook to provide constant updates on the service
to know if the payload has stopped, is stopping (in error cycle state) and more.


> The Moonstone team has assembled a good documentation resource for the feature:

The new payload management feature allows charmers to more accurately define
 large and complex deployments by registering different payloads, such as
 lxc, kvm, and docker, with Juju. This lets the operator better understand the
 purpose and function of these payloads on a given machine.

You define these payloads in the metadata.yaml of the charm under the payloads
 section. You create a class for the payload, “monitoring” or “kvm-guest”, and
 assign the type.

    payloads:
      monitoring:
            type: docker
         kvm-guest:
           type: kvm

From your charm hook you can manage your payload with the following commands:

    payload-register <type> <class> <ID> [tags]
       payload-unregister <type> <class> <ID>
       payload-status-set <type> <class> <ID> <starting, running, stopping, stopped>

From the Juju command line you can view your payloads like this:

    juju list-payloads <filter>

For more information run:

    juju help payloads


### But Wait, there's more!

If you're still reading, and cant wait to see the rest of the outlined features
in the video, part2 has been published
[here](/2015-charming-2-point-oh-pt2.html)



Stay tuned for a video overview of charming with layers. And if you've got any
questions be sure to send them to the [mailing list](mailto:juju@lists.ubuntu.com)
or to drop by on IRC in #juju on irc.freenode.net

Happy Hacking!


