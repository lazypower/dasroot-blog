Title: Charm Encapsulation
Date: 2015-01-09 00:04
Tags: juju, charming, theory
Category: devops
Slug: 2015-charm-encapsulation
Status: published
Image: /images/2015/january/shipping_container.jpg

When charming, I think it's important to remember that there are a few things worth
keeping in mind. If you approach charming with the following mind set, it will enable
you for success.

- Encapsulation
- Testing
- Keeping hook code simple

With these three listed above, lets dissect down into the first thing listed: **Encapsulation**

### Lets Find a good example

The first task for my team this new year has been to look into Kubernetes - with a few existing
prototype charms from [Hazmat](http://blog.kapilt.com/) we were set along our path of discovery.
A few man hours have already been spent writing the services, and getting things together - but
this just didn't bode well with me. To take a prototype, and run headfirst down the long hallway
of container orchestration. I'm goign to 'pick' on one charm in particular - the
[Flannel charm](https://launchpad.net/~hazmat/charms/trusty/flannel/trunk) I exhibited in a
[prior post](/container-networking-with-flannel.html)

It really is a brilliant piece of work. The primary directive of the Flannel charm was to Install
a container environment, either LXC or Docker - and add a Software Defined Network bridge that
enabled cross-host communication with the containers. And it did this rather well - but the one
thing that irks me is it was a mashup of concerns.

#### No Clearly Defined Boundaries
- Install a container provider
- Install a networking bridge for either provider
- Communicate with ETCD to enable SDN for either provider
- Handle updates for aforementioned container provider

These concerns being mashed into one charm, while they might be feesable for proto-ware, it
doesn't sit well with me for composability.

### Composability Illustrates Good Encapsulation

When green-field developing charms, the first thing I like to do after prototyping is to aggregate
facts and run down a checklist of concerns for the charm outline as so:

- Whats the intended / primary use case
- How does this relate to other charms
- How will that data-handoff look
- Which service does this data-interchange effect
- Does it make things easier to maintain if I do it another way?

In some cases, it may make sense to co-locate services in the same charm. For example, if I were
to deplay a LAMP stack - it makes complete sense to co-locate the database, webhead, and PHP
daemon on the same machine and manage those services. (I can argue the point, but its a very
familiar example)

What I would rather do, is separate those concerns into a microservice model, and relate/manage
them interchangeably. I may not always want a MySQL server with my App, and this becomes simple
to do with the JUJU model by changing the MySQL component out with say PostGRES and using the
proper relationship handlers. This illustrates *good* encapsulation. My concerns are independent
and it wont change anything but a database adapter on the webhead, which will be managed - by the
webheads relationships.

### Approaching Refactoring the Flannel Charm

Lets take a look at how we can split this apart. A Venn Diagram should outline the overlap quite
well, as we can clearly see when they intersect. A key thing to remember, is that these services
will continue to live on the same host, however they are completely separate services, with their
own concerns about what to do to the state of the host.

![Docker / Docker Flannel Ven Diagram](/images/2015/january/docker_flannel_ven_diagram.png)

> The above may not express the full extent of the charms concerns, but are good for the example
> case given.


Should there ever come a time where we want to move away from flannel to another SDN solution - we can now change out the service on each host, allowing for a live migration away from Flannel to &lt;Service&gt;. As well as taken a tightly coupled service definition, and changed it into a relation with simple datapass between then.

We have done a few things as a byproduct:

- Defined clear boundaries for each service
- Made the services related, but not dependent
- Made testing simpler per service
- Allowed for interchangeable components

Now lets look at the actual Implementation of this - which is where my **real discovery** began.

### Service Topology

![Juju Topology of Encapsulated Services](/images/2015/january/encapsulated_topology.png)

We see that we have 3 components.

- [ETCD](https://launchpad.net/~hazmat/charms/trusty/etcd/trunk)
- [Docker](https://github.com/chuckbutler/docker-charm)
- [Flannel-Docker](https://github.com/chuckbutler/flannel-docker-charm) (scope: container)

The interesting bit here is the relationship cycle/sequence that occurs during setup, lets take a look at how we do this:

    juju deploy cs:~trusty/hazmat/etcd --to 0
    juju deploy local:trusty/docker
    juju deploy local:trusty/flannel-docker
    juju add-relation flannel-docker:docker-host docker
    juju add-relation flannel-docker:network docker:network
    juju add-relation flannel-docker etcd

> **Pitfall** You may be asking why two relationships with the docker charm. Lets explore why.
>
> The docker-host relation is a juju-info interface relationship, which is special for making
> the subordinate connect and deploy within `scope: container`.

##### Fig 1.1 - metadata.yaml
[gist:id=10420566b629b6abbeed,file=metadata.yaml]

#### Pass Data between units, outside of the relationship context

Another advanced topic in charming here, is you have to pass data outside of the relationship
context. Normally we exchange all of this data because we have it up-front. But what if someone
were to relate flannel-docker:network after they related flannel-docker to etcd? This is where the
dependency chain gets interesting.

##### Fig 1.2 Snippet from ansible playbook
[gist:id=10420566b629b6abbeed,file=flannel-configuration.yaml]

We have data that we didn't have until the database relationship joined - this is what triggers
flannel to restart it self and populates /etc/flannel/subnet.ev with the proper information that
came back from etcd. We're clearly not in the network-relation-changed event, how do we send this
information back over the wire without breaking encapsulation?

THe magic is line 24 in Fig 1.2 - we aggregate facts, and pass them over the context of the network
relationship using `relation-set -r #id`. This took a bit more dancing of the juju jig to get the
data.

- Scan the relationship ids
- Scope our request to the relationship id
- transmit the data over the context of the relationship-id

#### Learning and Discovery - Avoid Pitfalls
> **Pitfall:** Juju-Info relations are reserved for Juju and should never be assumed that you
> can hand off data over this relationship. I ran into this and cycled for a few hours trying to
> discover why info-pass wasn't happening during development. This necessitated the new relationship.

> *note* If you want to keep the relationship limited to its co-located service, simply add
> `scope: container` to the relationship.

With all of these in mind - I'm confident we are building a good example for the community to follow
with regards to service encapsulation, proxying information, and building a better, more composeable
ecosystem for everyone to enjoy.

### Happy Charming!

