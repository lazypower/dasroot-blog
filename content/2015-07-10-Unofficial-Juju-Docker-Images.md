Title: Unofficial Juju Docker Images
Date: 2015-07-10 02:51
Tags: docker, juju, tooling, planet
Slug: 2015-unofficial-docker-images
Category: devops
Status: published
Image: images/2015/july/docker_hub_images.png

## Using Juju in Docker for your projects

Early this year the juju-solutions team has been experimenting with Juju in
Docker - namely for isolation, and portability reasons. The Vagrant image gives
a nice isolated and rebuildable environment - however the overhead of the
bootstrap every time, spinning up the GUI, and etc - caused a latency that we
just didnt want or need in our CI environment(s) - as well as when [running the
review queue](/2015-local-isolation-with-docker-and-juju.html).

Up until this point, the images have all been distributed under various
namespaces in the Docker hub registry - and one thing we wanted to ensure was
that these images were accessable, and under a high standard for quality.

### Where do I find these magical images?

We're aggregating our project images under the [jujusolutions](https://registry.hub.docker.com/repos/jujusolutions/)
namespace on the docker registry for now. A star would go a long way towards
helping discoverability. In addition, the source repositories are available for
bugreports and feature requests in our [Github Organization](https://github.com/juju-solutions)

- [Jujubox](https://github.com/juju-solutions/jujubox)
- [Charmbox](https://github.com/juju-solutions/charmbox)


Both images are shipped with 2 possible tags.

- `:latest` (recommended) - will pull the latest stable Juju release baked into the image
- `:devel` (experimental) - will pull the latest development Juju release baked into the image

I will be working hand in hand with Aisreal to get a :nightly tag added for
those wanting to explore the current Juju built from tip of the Github archives.

This is really handy when testing new features, and not wanting to pollute your
system with the dev dependencies for compiling Juju from source, or breaking
an existing installation.

### Whats the difference between Jujubox and Charmbox?

`Jujubox` is a bare-bones juju image, shipped and configured for the Ubuntu user
as the primary juju user. You can use this image to run automated deployments
from say a CI/CD server. It doesn't ship with any additional tooling.

- juju
- juju-quickstart
- juju-plugins

`Charmbox` is a fatter package, but ships with all the tooling needed to perform
the daily tasks of a Juju Charmer. It ships by default with:

- git
- bzr
- charm-tools
- juju-plugins
- juju-deployer
- juju
- juju-quickstart
- build-essential
- amulet
- bundletester

### How often are they updated?

As new juju releases are shipped, these images are now rebuilt every night at
3 am EDT.

### Whats the catch?

Using the local provider in these docker images is extremely tricky, and is
covered in the [Charmbox repository README](https://github.com/juju-solutions/charmbox/blob/master/README.md)


### How is the Juju Solutions team using these images?

We're currently using these images in house in our Jenkins CI system that powers
our review testing of incoming charms, and charm updates.

Another CI based Usecase has been a Drone.io Implementation i've been working on
to run our Kubernetes upstream validations as they cut new revisions. I will
be sure to post an in-depth follow up post once this particular use case has been
classified as stable. But this shows the extensibility of these images, and how
they can be applied for your own CI setup, to run express, upstream integration
jobs.

Here's a snippet from the Dockerfile:

    FROM jujusolutions/charmbox
    ADD install-gvm.sh /tmp/install-gvm.sh
    RUN /tmp/install-gvm.sh

    ADD kubes-ci-run.sh /kubes-ci-run.sh

    ADD requires/ssh /home/ubuntu/.ssh
    ADD requires/juju /home/ubuntu/.juju

    ENTRYPOINT
    CMD sudo -u ubuntu /bin/bash -c "/kubes-ci-run.sh"

When doing Review Queue we also like to isolate our reviews using these images
and running them with the --rm to ensure any development dependencies are wiped
when we exit the context of the image. I posted about this in-depth in
[Expediting Isolation with Juju and Docker](/2015-local-isolation-with-docker-and-juju.html)


And finally, we find these images are great for a portable Juju installation on
any distro/platform - regardless of it being windows, OSX, or Linux based. The
fact these containers are light enough weight to spin up in a second or less means
you can get to hacking on your cloud deployments faster than our shipped Vagrant
image.

### We <3 feedback!

If you're doing anything interesting with these images, we'd love to hear about it!


Deploy Happy!
