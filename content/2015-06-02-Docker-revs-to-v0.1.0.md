Title: Docker Charm revs to v0.1.0
Date: 2015-06-02 13:51
Tags: docker, juju, charms, planet
Slug: 2015/docker-charm-revs-to-v010
Category: devops
Status: published
Image: /images/2015/june/docker_release.png

Another quick post today about revving the Docker charm to v0.1.0 which is a
major feature release targeted at developers of the ecosystem consuming docker
as an underlying service. (Services such as SDN through calico-docker or flannel
as well as service discovery through consul).

### Release Notes

  - Support for docker tagging enabled ([prelim SWARM support](https://github.com/whitmo/swarm-charm))
  - [Docker Opts manager](https://github.com/chuckbutler/docker-charm/blob/master/modules/docker_opts.py)
    - Module to aggregate, store, and build the DockerOPTS string when several
      services are attempting to reconfigure the docker daemon.
  - New [Ansible charm](https://github.com/whitmo/ansible-charm) support (breakout from charmhelpers)
     - Cleaner interface to writing ansible based charms
     - Installs ansible from PIP to ensure we're riding the trending latest features
     - Pretext work for even more ansible goodness
  - Updates to tests for testing version upgrade (no longer relies on metapackage)

Big thanks to [@whitmo](http://bfh.whitmo.org) for these contributions


The release is currently pending
 [charm store review](https://code.launchpad.net/~lazypower/charms/trusty/docker/trunk/+merge/260867)
and as always if you're not afraid to run from GIT, the changes are available
immediately from the MASTER branch.

I've also ported this into my namespace for easy charm store deployment via:

    juju deploy cs:~lazypower/trusty/docker

From there, its as easy as 1,2,3 to stand up the rest of the docker ecosystem
we've been targeting in New Workloads. This release is our biggest to date, and
will be revving again in the next month or so.


### Whats Next?

There's a laundry list of issues over on the Docker Charm bug tracker. If you've
got a feature you cant live without - please feel free to swing by and file a
feature request.

The remaining bugs are targeted for a minor version release following today's
release.


