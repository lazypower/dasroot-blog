Title: ETCD Charm updates to v2.0.11
Date: 2015-05-26 12:57
Tags: juju, etcd, charms, planet
Slug: 2015/etcd-charm-updates-to-v2011
Category: devops
Status: published
Image: https://coreos.com/assets/images/media/etcd2-0.png

Just a quick update today. Some major refactoring has happened on the ETCD charm
to update it from the 0.x series into 2.0.11.

Along with these updates, there are also some new features added to the charm
such as integration with leader election, to ensure we have a leader in the
etcd service that juju knows how to interrogate for the full status of the
cluster, and to report that information back to the system.

This also resolves an interesting issue in terms of cluster data being trapped
int the raft log, that is now exposed via the peering relationship.

As a final addition in the feature set, it now has a health action to report the
health status of your cluster. (Useful during scale-up and scale-down scenarios
to validate your cluster reconfigured correctly)

    juju action do etcd/0 health
    <job uuid response>
    juju action fetch <uuid>

    results:
      result-map:
        message: |-
          cluster is healthy
          member 729756339f73f34f is healthy
          member df173b6013fde4bf is healthy
    status: completed

The work being landed is currently under review, and can be obtained/commented
on here: [https://github.com/whitmo/etcd-charm/pull/7](https://github.com/whitmo/etcd-charm/pull/7)
