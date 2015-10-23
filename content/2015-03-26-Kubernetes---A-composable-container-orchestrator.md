Title: Kubernetes - A composable container orchestrator
Date: 2015-03-26 23:57
Tags: devops, kubernetes, docker, juju, flannel
Slug: 2015-kubernetes-a-composable-container-orchestrator
Category: devops
Status: draft
Image: /images/2015/march/kubernetes-cluster.png
ImageCredit: Juju GUI Showing off a composed kubernetes cluster

Juju has an innate ability to orchestrate with containers - specifically LXC
based containers. They are first class citizens in the ecosystem, and really
helped me to grokk why containerization of applications is the future
of isolation, density, and workload management. The New Workloads team has
been working dilligently on bringing Docker to the Juju ecosystem - both in
practice on the client, as well as scale-out workloads deployed with Juju.
I've already blogged about this however, and you can read that article
[here](#).



## Kubernetes - Orchestrating docker containers

> Kubernetes is a powerful system, developed by Google, for managing containerized applications in a clustered environment. It aims to provide better ways of managing related, distributed components across varied infrastructure.

-- Cited: [Justin Ellingwood](https://www.digitalocean.com/community/tutorials/an-introduction-to-kubernetes)

Kubernetes is a compelling solution within the Juju Ecosystem. As it stands
today there's a very short sidewalk to what you can do with Docker. The docker
charm only provides the Docker runtime, as in - the capacity to
deploy containers on a set of host(s). In order to do cross-host networking
you have to layer in a SDN solution or bind the networking to the host. Both
of which are acceptable solutions - but what about scheduling? Service
monitoring and clustering? Scaling the containers? A lot of these same concerns
exist in "traditional" docker farms as we know them today.


By combining the framework stack of the Docker ecosystem, we have written a
solid baseline of indepedently versioned components to provide the plubming for
Kubernetes. As it stands today - we have Docker and Flannel SDN; with more
components and alternatives incoming. (First stop is Weave SDN as a pluggable
replacement for Flannel).

#### Enter Kubernetes



