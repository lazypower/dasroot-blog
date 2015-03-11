Title: Charming with Docker
Date: 2015-03-11 09:27
Tags: docker, juju, documentation, planet
Slug: 2015-charming-with-docker
Category: devops
Status: published
Image: /images/2015/january/docker_charm.png
ImageCaption: Delivering the Docker Infrastructure with Juju

## Docker Dancing for Juju

Earlier this year, we had a fairly significant discussion in the New Workloads team about Docker, and the implications it has on application delivery, and system orchestration. [Matt Bruzek](http://bruzer.net), [Whit Morriss](http://twitter.com/whitmo), and I set out to distill some of the best practices in charming to bring the docker infrastructure to Juju. While this has been done before - it seemed a bit open ended and incomplete. One of the things I noticed right away was most of the 'Docker Charms' had one of two identified patterns:

- Deploy everything under the sun in a single charm to provide both docker, and the service container.
- Deploy only the docker binary of the authors choice and no-op.

Nothing about these patterns really stood out in terms of reference architecture for getting moving with Docker. This is where we decided to step in and start to implement the ecosystem as we feel it should be deployed. Leveraging the existing documentation, patterns published on docker.io and CoreOS's SDN network stack - we set out to get a cross host docker cluster up and running.

## The Docker Components of Today

I want to highlight that we have done an excellent job of illustrating composability and [concern encapsulation](/2015-charm-encapsulation.html) in these charms. These charms are also fully documented on each of their respective repositories over on Github.

### The Docker Charm

![The Docker Charm](/images/2015/march/docker_charm.png)


The docker charm supports installation from 2 sources. Fetching from the ubuntu distro archive, or fetching from the Docker provided PPA for the latest and greatest. The configuration is nice and simple with a single option to define which installation resource you would like to consume.

There are included comprehensive test suites to deploy docker, pull a docker image from the docker registry, and subsequently execute commands inside docker. These integration tests help us to ensure the charm will be stable throughout revisions to the charm as we continue to grow the ecosystem and add relationships to other services.

The interfaces that are implemented (and some future planned interfaces) can be found in the [Documentation](http://chuckbutler.github.io/docker-charm/user/configuration.html) including what expected data is to be consumed or sent during the relationship exchange.



- [Docs](http://chuckbutler.github.io/docker-charm/)
- [Find it in the Charm Store](https://jujucharms.com/u/lazypower/docker/trusty/)

#### Deploys with
- ` juju deploy cs:~lazypower/trusty/docker`

> These instructions will change once the charm has been accepted to the recommended charm store 

This delivers a single host ready to run your containerized workloads. Try it today on [Digital Ocean](http://digitalocean.com) for as little as $5 USD/month.

### Flannel-Docker Charm

![Flannel and Docker](/images/2015/march/docker_flannel.png)

Flannel has been [covered before](/container-networking-with-flannel.html) in length in another post.

The flannel-docker charm is scoped to deploy flannel specifically into the docker host. It no-ops until it has a relationship with ETCD - that warehouses its subnet data and keeps track of the distributed network. 

- [Docs](http://chuckbutler.github.io/flannel-docker-charm)
- [Find it in the Charm Store](https://jujucharms.com/u/lazypower/flannel-docker/trusty)


#### Deploys with

- `juju deploy cs:~hazmat/trusty/etcd --to 0`
- `juju deploy cs:~lazypower/trusty/docker`
- `juju deploy cs:~lazypower/trusty/flannel-docker`
- `juju add-relation flannel-docker:docker-host docker`
- `juju add-relation flannel-docker:db etcd:client`
- `juju add-relation flannel-docker:network docker:network`

> These instructions will change once the charm has been accepted to the recommended charm store


This delivers the ETCD service co-located on your bootstrap node, a single Docker host ready to run your containerized workloads, and Flannel software defined networking - ready for a scale-out workload. To scale services simply `juju add-unit docker` and the networking will configure itself - enabling cross host container communication. Try it today on [Digital Ocean](http://digitalocean.com) for as little as $5 USD/month per server.

### The Docker Core Bundle

![Docker Core Bundle](/images/2015/march/docker_bundle.png)

Get a best practice docker cluster ready for scale out workloads out of the box with our Docker Core bundle. This bundle deploys:

- Docker
- Flannel-Docker
- Etcd

All pre-configured, and related - ready to go with Juju quickstart.

#### Deploys with

- `bzr branch lp:~lazypower/charms/bundles/docker/bundle docker-bundle`
- `juju quickstart -c docker-bundle/bundles.yaml`

> These instructions will change once the bundle has been accepted to the recommended charm store 


# What's Next

These charms provide the infrastructure to run your dockerized applications, and are only responsible for keeping the docker runtime up to date, and configured. There is a lot of room for improvement here in terms of lifecycle management, and ease of use for end users.

#### Juju Actions

Ideally Juju Actions will provide a brilliant method to interact with your docker cluster. A few ideas we've come up with are:

- Listing running containers
- Managing Images that are on the host (cleanup)
- Launching an arbitrary container from the docker registry
- Performing health checks
- Creating storage container volumes


#### Ambassador Pattern App Delivery

Using the [Ambassador Pattern](https://docs.docker.com/articles/ambassador_pattern_linking/) to link your services together, we can achieve new levels of service switching among containers and your application runtime.

Regardless of that service living in the docker runtime, or being provided by an existing Juju deployed service. Using the listed example: 

- Redis from a Docker Container
- Redis from a Juju Charm


#### Docker Charm Templates

We're talking about prototyping Docker App Delivery in charms. This poses some interesting and unique challenges that we'd like to combat in a way that doesn't involve (possibly) hundreds of lines of  duplicated boilerplate code for each service you wish to represent as a container.

Looking at how Juju works today, we've come up with the following sketch notes to start building this template.

- Subordinates are not a prime candidate for app delivery. You may or may not want to deploy the container to every running docker host in the cluster.
- juju deploy --to works,  but is messy and relies heavilly on the Machine View listing of the GUI to determine runtime placement. Scaling is a concern with this method as well.


#### New / Additional Services for the ecosystem

Flannel is a great SDN solution for doing L2 over L3 networking, but they aren't the only kid on the block. Perhaps you have organizational expertise in socketplane and would prefer to use their SDN. This leaves me to believe we should have a rich ecosystem with the remaining services. Due to limitations of having a single author writing/testing/maintaining these applications - this is a prime opportunity for someone that is interested in Juju to pick up the banner and help make this a rich experience for everyone.


#### Limitations of the implementation today

As it stands, Docker is not a first class citizen in Juju. The charms are providing the infrastructure layer, similar to how Juju deploys Open Stack. However, there is not a notion of juju deploy --to docker:<machine id>, as it doesn't have first class citizenship in Juju-Core. We're working around this in interesting ways, and trying to prototype a uniquely story around the tools that are emerging.

##### Virtual Services

Virtual Services is a notion that has just emerged, and is still being planned and running the paces of pre-approval. Virtual services would allow a charm to be deployed and register key/value pairs that denote its configuration, endpoints, and possible API consumption to a service that is not directly under Juju's management. This provides us a great way to interface with existing infrastructure, as well as emerging technologies - like docker. Deploy a container, register it as a virtual service - and you now have ways to relate the service to other services without writing tons of duplicated code just to deliver a single container. Thus reducing development overhead, and exposing the full range of Juju integration with the container.

> Without a finalized spec to point to, this should be treated as "possibly coming - and it might never happen." However, I feel the idea has serious merit, and is worth mentioning.


## Docker Dancing with Juju

#### Jujubox for docker

- Fork this project on [Github](https://github.com/whitmo/jujubox)

Speaking from the mindset of a consumer of all things Juju - including test dependencies... I for one welcome the efforts of Whit Morriss who built a Juju docker container for use on the workstation. This has a few implications that have really resonated with me.

- Test dependency isolation. No longer will bundletester be installing whatever unholy business we need to test the infrastructure of a charm deployment. (I'm talking about you - python modules)
- Landing Juju cross-distro without any fuss (On centos? no rpm? no problem! run the docker box image!
- Strives for parity with the juju vagrant image
- Lighter weight than a VirtualBox box - the JujuBox docker image boots sub-second, while the jujubox vagrant image takes ~ 3 minutes to boot, prepare, and return execution on my SSD i7 rig (with 6gb of ram allocated to the VM instance)

If you're interested in testing out the Jujubox - I encourage you to try, test, and file any feedback you may have to us on the [Mailing List](mailto:juju@lists.ubuntu.com)
