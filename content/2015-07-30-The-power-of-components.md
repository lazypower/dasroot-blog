Title: The power of components
Date: 2015-07-30 08:26
Tags: juju, kubernetes, planet
Slug: 2015-the-power-of-components
Category: devops
Status: published
Image: /images/2015/july/kubes-micro-cluster.jpg

While dogfooding my own work, I decided it was time to upgrade my distributed
docker services into the shiny Kubernetes charms now that 1.0 landed last week.
I've been running my own "production" (I say in air quotes, because my 20 or so
microservices aren't mission critical. If my RSS reader tanks, life will go on.)
services with some of the charm concepts I've posted about over the last 4 months.
Its time to really flex the Kubernetes work we've done and fire up the latest
and greatest, and start to really feel the burn of a long-running kubernetes
cluster, as upgrades happen and unforseen behaviors start to bubble up to the
surface.


### Considerations

One of the things I knew right away, is that our provivded bundle was way
overkill for what I wanted to do. I really only needed 2 nodes, and using
colocation for the services - I could attain this really easily. We spent a
fair amount of time deliberating about how to encapsulate the topology of a
kubernetes cluster, and what that would look like with the mix and match
components one could reasonably deploy with.

#### Node 1

- ETCD (running solo, I like to live dangerously)
- Kubernetes-Master

#### Node 2

- Docker
- Kubernetes Node (the artist formerly known as a minion)

> Did you know: The Kubernetes project retired the minion title from their nodes
> and have re-labeled them as just 'node'?

### Why this is super cool

I'm excited to say that our attention to requirements has made this ecosystem
super simple to decompose and re-assemble in a manner that fits your needs. I'm
even considering contributing a Single server bundle that will stuff all the
component services on a single machine. This makes it even lower cost of entry
to people looking to just kick the tires and get a feel for Kubernetes.

Right now our entire stack consumes bare minimum of 4 units.

- 1 ETCD node
- 2 Docker/Kubernetes Nodes
- 1 Kubernetes-Master node

This distributed system is more along the lines of what I would recommend
starting your staging system with, scaling ETCD to 3 nodes for quorem and HA/Failover
and scaling your Kubernetes nodes as required. Leaving the Kubes-Master to only
handle the API/Load of client interfacing, and ecosystem management.

I'm willing to eat this compute space on my node, as I have a rather small
deployment topology, and Kubernetes is fairly intelligent with placement of
services once a host starts to reach capacity.

### Whats this look like in bundle format?

> Note, I'm using my personal branch for the Docker charm, as it has a UFS
> filesystem fix that resolves some disk space concerns that hasn't quite
> landed in the Charm Store yet due to a rejected review. This will be
> updated to reflect the Store charm once that has landed.

<script src="https://gist.github.com/chuckbutler/f9218cc74ef8cfa07205.js"></script>


#### Deploy Today

    juju quickstart https://gist.githubusercontent.com/chuckbutler/f9218cc74ef8cfa07205/raw/3dd5a12a7d17b7d9c1b07d6a3b5b2f868681bdf4/bundle.yaml

Deploy Happy!
