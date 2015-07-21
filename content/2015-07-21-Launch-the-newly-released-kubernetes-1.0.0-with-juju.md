Title: Launch the newly released kubernetes 1.0.0 with juju
Date: 2015-07-21 11:00
Tags: video, kubernetes, juju, devops, containers, cluster, planet
Slug: 2015-launch-kubernetes-with-juju
Category: devops
Status: published
Video: UUFGoWMPXWE

## Kubernetes 1.0 launched today!

And in the spirit of Kubernetes reaching this major milestone, we've been
tracking upstream development to enable a strong story across the two perspectives
a user can enter the container cluster management space: as a consumer, and as
a contributor.

### Deploying Kubernetes as a Consumer

We've vendored the Kubernetes charms into the charm store under the ~kubernetes
namespace for immediate launching into your cloud environment of choice. Where
might that be you ask? Anywhere that  supports Juju (so any data center, public
or private. If you include the manual provider, we are everywhere!)

#### For the impatient

To deploy right away, if you have the `juju-quickstart` package installed, simply
copy and paste the following into a terminal and enjoy the magic

    juju quickstart u/kubernetes/kubernetes-cluster

This will deploy the reference core of Kubernetes 1.0.0 for you, consisting of:

- Kubernetes Master
- Docker Engine x2
- Kubernetes Nodes driving the docker engines
- Flannel overlay networking between nodes
- ETCD as a shared configuration/coordinator

Total machine cost: 4

![Kubernetes 1.0.0 Bundle](/images/2015/july/kubes_1_dot_oh_bundle.png)

#### Extend your infrastructure

Since Kubernetes was modeled with Juju, you gain the instant benefit of adding
complimentary services to your stack, such as log aggregation with
Logstash/Elasticsearch/Kibana - the ELK stack. You can deploy ELK right alongside
your Kubernetes deployment, and using `Logspout` - aggregate all the logs from
your containers and gleen insights into your cluster using kibana searches.

The fun doesn't have to stop there however, there's tons of services in the
juju charmstore (~ 250 at last count, not including namespaces) for you to
bolt into your infrastructure and instantly gain benefits. Integrate full
host monitoring with Zabbix, attach Landscape to apply internal policies to the
machines and get monitoring as added benefit, the possibilities literaly end
at your imagination. With a little bit of charming, you can drive your infrastructure
your way. And that, is where you find the happiness.

### Deploying Kubernetes as a Contributor

As an ISV or core Kubernetes contributor - you can gain instant benefit from the
work we've landed in Kubernetes upstream. Every clone of the Kubernetes git
repository ships with Juju deployment scripts that enables you as the developer
to make modifications and ship that into a reference deployment of Kubernetes.

    git clone http://github.com/googlecloudplatform/kubernetes.git
    cd kubernetes
    *hack hack hack*
    export KUBERNETES_PROVIDER=juju
    cluster/kube-up.sh

This will compile the binaries for Kubernetes, and "fat pack" the charms with
the modified bins from your developer workstation. the `kube-up` script will
do the heavy lifting of deploying the architecture and re-use the shipped bins
and distribute them across all the nodes for you.

This is excellent not only for checking modifications, but also to deploy from
HEAD of the Kubernetes repository. Did you land a PR and want to verify them
in a high-parity environment to your production setup? Simply set the
Kuberentes provider to juju, and enjoy the consistent configuration of your
deployment.

### Where do we go from here?

We will continue to track the upstream Kubernetes project and offer instant
value to consumers and contributors alike. Join us on the Juju Mailing list
to discuss the future of our integration with the Kuberentes project.

You can also find us in #juju on irc.freenode.net - the primary drivers of the
Kubernetes charms are:

- whitmo
- mbruzek
- lazypower

Deploy Happy!
