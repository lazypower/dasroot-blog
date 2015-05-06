Title: Juju App Containers, Build Services, and Continuous Delivery
Date: 2015-05-06 20:10
Tags: devops, juju, docker, build-pipeline, formation, bundles, pure-awesome, planet
Slug: containers-build-services-and-continuous-delivery-with-juju
Category: devops
Status: published
Image: /images/2015/may/docker-build-formation.png

It's no secret that we on the Juju Solutions team dogfood our charms that we're
producing. The Docker-Core ecosystem is no exception. I've been running with a
glorified `apt-get install docker` charm for a while now. Sure - it exposed
some nice things like being able to cross-host network with flannel via a simple
subordinate service, and drawing some relations... But I was ready to take it
a step further.

> Editors note: The charm actually served a deep seated core purpose, of being
> shareable, and occupies space in the Kubernetes deployment(s) and some
> work thats forthcoming. The above sentiment was for dramatic effect.

I set out this last Sunday to do exactly that. Re-energized by the Malta Planning
sprint where I heard about all the awesomeness we are coming up  with in the next
six months.


### How do you *really* model docker in Juju?

I've had several questions over the last month or so about the actual docker
charm itself, and just what value it adds to the Juju topology when the charm
is deployed. Until today, I pretty much replied with "The world is your oyster".

While there have been [examples](https://github.com/bcsaller/juju-docker) of
[what you can do](https://github.com/chuckbutler/docker-nginx-charm.git) using
the Juju Modeling language to describe docker container services - I don't think
it really sank in just how much *raw power* this exposes to you, the developer,
building your infrastructure as peer-orchestrated services.

Let's examine a scenario where I, as the developer - want to setup a staging
environment. I may have a pre-built image on my desktop - but perhaps it would
be more prudent to build my container in a centralized location, so I can poke
and probe the environment that has a high-parity with my Production environment.

> If this sounds familar to you - It's core tenant of Modeling with
> Juju. Gain high feature parity between environments, enabling you to ship
> infrastructure as code between your environments - staging, qa, prod
> [reference](https://speakerdeck.com/chuckbutler/service-orchestration-with-juju?slide=13)

#### I'm a developer, and I use docker. I like staging off of builds - what now?

Lets start off with the Assumptions of this particular dissection of services:

- You use some Git hosting provider that has webhook support
- You build your containers with Dockerfiles, so they are repeatable
- You understand the basics of Juju, that services will be related to one another
- You want to consume services both IN and OUT of containers
- You want a logging nexus to capture all your logs, and run queries against them later.
- You dont mind co-locating charms on a single machine, even though we tell you not to.

Are you on board so far? Great! Lets break down the charms we have vs what we
need.

1. ELK - We have an elk stack in the charm store - nothing to do here. check.
2. Docker exists, thats half the battle right? check.
3. Build on git-deploy... that sounds almost like a PAAS... but I don't want to
build or leverage a full-blown PAAS.

### To PAAS or not to PAAS, that is the question

PAAS or Platform as a Service can often times be involved. I'm already using a
modeling language that allows me to abstract away a lot of complexity through
the use of charms and relations. To keep things simple, we'll need some python
glue and a bit of hackery.

##### Hooked - WebHooks as a service courtesy of Python

The [Hooked](https://pypi.python.org/pypi/hooked/0.1) module looked exactly like
what I wanted. Dynamic, config-file driven, and supports arbitrary build hooks.

With this bit of magic, I decided I needed a little more intelligence in my
system and wrote a bit of Python myself to manage building images from a 
Dockerfile.

> Script TL;DR - It builds containers from a filepath, and can kill existing
> containers if any, fire up the new build in its place. Its very much a one-shot
> process and likely to fail at some point.

<script src="https://gist.github.com/chuckbutler/dc8998499603f2789856.js"></script>


Great, with hooked and this bit of Python - I can pretty much do everything I need
and avoid the PAAS space... but, I kind of turned Juju into a PAAS. However thats
a conversation better left for suds and more pedantry than I have at the moment.

Ok, back to the list:

4. Webhook integration - check
5. Docker charms for my repositories...

## Dynamic Docker Charms? Really?

This sounds too good to be true... because right this minute - it is. If you have
a very vanilla, single container service with light requirements on relations or
no relations at all - This charm will be right up your alley:

[The Dockerfile Charm](https://github.com/chuckbutler/dockerfile-charm)

Weighing in at 47 lines of pure BASH - this gives us enough glue to fetch a
git repository to a specified location, relate to our docker-build-hook service
and self-register the project. The rest of the magic is *in* the repository
itself. [View a sample build script](https://github.com/chuckbutler/docker-selfoss/blob/master/build.sh)

Awesome!

##### What would you do differently for a production charm?

Each charm would get the branding of the contained application, and all required/optional
relationships would be added. When it comes to proper peer to peer orchestration there
are concerns that need to be encapsulated that a "genericized" charm just wont do for you.

This is a good start, and a candidate for template generation, but not what I would
recommend you run in production.

However, that being said - if you're writing a charm - include the project relation
and give it some config so you can deploy/build directly from git! There's no reason it
cannot do both!

### Step 2 - Deploying and validating

> To follow along at home, I suggest you fork the repositories listed, so you
can enable webhooks and kick the tires a bit. Also, the --to 1 assumes you've only
deployed your bootstrap node. This can be any `docker` host.

> - [docker-selfoss](https://github.com/chuckbutler/docker-selfoss.git)
> - [docker-mumble](https://github.com/chuckbutler/docker-mumble)

    juju deploy trusty/docker
    juju set docker latest=true version=1.6.0
    juju deploy cs:~lazypower/trusty/docker-build-hook
    juju add-relation docker-build-hook:docker-host docker
    juju deploy cs:~lazypower/trusty/dockerfile docker-selfoss --to 1
    juju set docker-selfoss repository=https://github.com/chuckbutler/docker-selfoss.git build-script:build.sh
    juju deploy cs:~lazypower/trusty/dockerfile docker-mumble --to 1
    juju set docker-mumble repository=https://github.com/chuckbutler/docker-mumble build-script=build.sh
    juju expose docker-build-hook


The resulting deployment should resemble the following:

![docker build core formation](/images/2015/may/docker-build-core.png)


### What did we get from all of this?

Obtain the public-ip of your docker host from `juju-status` and visit port `8080`

You will see JSON output similar to the following, signifying that your projects
are successfully registered.

<script src="https://gist.github.com/chuckbutler/0082e2055784421e6455.js"></script>

If you see the JSON above, you're ready to integrate with your git host.

Head over to your forked repository, click on settings => webhooks/services => Add a webhook

Plug in the public IP and port 8080 of your service, as outlined below:

![Github Docker Build Integration](/images/2015/may/github-docker-build-integration.png)


Finally, clone the repository, make an edit and push.

When you deploy, you will see a container build process pop up on the unit. You
can verify this by ssh'ing into your docker unit, and running `watch docker ps`

![docker builds in paralell](/images/2015/may/docker-build-paralell.png)

Note that the build is running concurrent with the container thats actively
running below it. Pretty neat huh?

It will effectively kill, and cycle with the new image upon
successful completion of the build. Ensuring we have a minimal downtime
deployment of sub-1-second. Thats acceptable for staging I think!


### Concept Breakdown

I took some screenshots and edited them as diagrams for really grokking whats
going on here in terms of conceptual realization.

There are 2 hosts represented in the over-all topology, 1 machine that's
responsible for running my Docker infrastructure (this could easily be 2 -> infinity)

I broke this down into separate machines, so I had confidence that my logging
infrastructure would not be subject to ephemeral containers, and have a semblance
of disaster introspection should something go wrong on my container provider.

![docker build host breakdown](/images/2015/may/docker-build-host-breakdown.png)

When we introspect the Docker provider host, I see a few different layers
represented here.

- Container Infrastructure
- Meta layer that sits between the two to provide the 'ops glue'
- Containers

![docker build layer breakdown](/images/2015/may/docker-build-layer-breakdown.png)


### THIS IS GREAT!

It's a pretty great example of what you can do with docker and modeling your
deployments in Juju. There's most definately more to come. The space is fairly
large with several services to choose from.  But this should be enough of a primer
to get your creative mind moving as to whats possible here.

While these charms are simply Proof of Concepts - I plan on iterating over them
in my spare time to integrate with CI systems, and provide a great template
to get started charming up your existing docker containers. It would be awesome
to consume something like a compose.yaml and generate charms based on that spec.

Another day, another time :)


## What about Logging and the ELK stack?

This sounds like a great topic for a part 2 - so make sure you stay hungry and
keep an eye out for how we're goign to jack into the existing Logstash infrastructure
and reap the benefits of juju by adding a single charm to the deployment topology.



