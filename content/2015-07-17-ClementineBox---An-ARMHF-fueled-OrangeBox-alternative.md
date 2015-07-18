Title: ClementineBox - An ARMHF fueled OrangeBox alternative
Date: 2015-07-17 21:08
Tags: rpi2, docker, lxd, weekendhacks, planet
Slug: 2015-clementinebox-an-armhf-fueled-orangebox-alternative
Category: projects
Image: /images/2015/july/clementine_box.jpg
Status: published

The name "Clementine Box" is a bit of a namegrab. Let me lead with that. This
is in no way affiliated with an official Canonical project, just something I'm
doing in my spare time to experiment with mixing LXD and Docker services to
prove that building a container based cloud in something that fits in the size
of a kleenex box is completely doable, and yields real world benefits.

> This is a homebrew hacker project. Sorry if you got excited.

### How does it differ from the real Orange Box?

Lets talk about what actually powers the official Orange Box so we can draw
some conclusions here about how it actually differs.

#### Orange Box Hardware Stack
- Intel NUC's with AMT based boot support
- I5 - I7 processors
- SSD's typically ~ 120gb per node attached via SATA
- Full hardware enclosure including Boot LEDS of each node
- Gigabit Ethernet
- 12 node GBE switch
- 15 - 25 V DC power draw per unit

#### Orange Box Software Stack

- Ubuntu MAAS provisioning and Network Control
- Juju Service Orchestration
- KVM support on nodes
- LXC/D support on nodes
- Full Ubuntu LTS OS images (read: apt-get support)

The takeaway here, is the Orange Box has the ponies to run OpenStack, and full
workloads contained therein.

As a 10k foot view, this is what comprises an Orange box. There's several posts
out there about building the Orange Box, specifically over on [Dustin Kirkland's
blog](http://blog.dustinkirkland.com/2014/05/the-orange-box-cloud-for-free-man.html).

#### Clementine Box Hardware Stack

- 4 Raspberry Pi2 Model B's
- Armv7 Quadcore procesors
- Gigabit Ethernet
- 5 port Netgear gigabit switch
- 4 8gb Kingston MicroSD's
- Anker 6 port USB Charger Hub with IQ
- ~5V power draw per unit

See the [Shopping List](http://amzn.com/w/11FJ54YX5HBHX) for full product details.

#### Clementine Box Software Stack

- Ubuntu Snappy Core (read, snappy only, no apt)
- Docker
- LXD

So, knowing that we're changing complete CPU Architecture, we've lost quite
a few things in this setup. Namely the entirety of the apt archive found in
distributions like Raspbian. Everything I want to run will have to be compiled
to armhf and loaded via [snappy](https://developer.ubuntu.com/en/snappy/tutorials/build-snaps/).

Also we lose quite a few CPU cores when compared against an i7, but we have reduced
the overall MilliAmp draw of the cloud drastically.

There is no Auto-Refresh of the nodes as this cluster has no concept of PXE booting
and flashing images to the SD card on first boot. All the systems will have to
be pre-flashed on the SD Cards prior to boot.

We're also losing out on running full VM containers - but that seems like an
acceptable rise considering the popularity of containers, and cleaning up after
containers should be a fairly quick and simple process.


#### Proposed future modifications:

Grabbing some stubby USB storage, and plugging in 30GB+ storage to operate our
containers on so we get faster performance than an SD Card, and have more than
8GB to work with.


## What are you going to do with it?

The entirety of this project is to illustrate building an ARM powered cluster
that is not only portable, but also has support for both FULL OS containers, and
what has been aptly dubbed 'app containers' or 'process containers' in docker,
and allowing both of these technologies to operate in the same network/hardware
space and have those services working in harmony.

#### This seems like a lot of trouble...

It may be, but we've got two golden technologies here. LXD is growing support
for a lot of interesting things dealing with containers, and also sort of serves
as the origin of Docker. When Docker first started it was basically tooling around
LXC before they wrote and adopted libcontainer. I don't think this drives a wedge,
I actually think this allows both container technologies to innovate in their own
domain and compliment one another.

Docker has a great Image based workflow, and promotes skinny containers that only
hold the bare essentials to run a process. LXD has greatly flexible containers that
contain a full operating system, including init services, and the full gambit of
services you would come to expect from a posix operating system. This sounds
like an ideal container solution for some applications such as Databases where
you *want* to have a fully featured OS available, and able to snapshot, backup,
and restore the full container knowing that your data wont be blown away by
a stray command.

I'm sure there are more delivery reasons to use one vs the other - but this
post is more about the ecosystem of the Clementine Box, than to spark a deep dive
into the container technologies it will be wrapping.

#### Snappy? Really? Why not just use Raspbian

Snappy-Core is a new darling OS from Canonical that's primary focus is to deliver
a light weight Operating System akin to those of NixOS, CoreOS, and other micro
distros. The lack of the apt-archive will be a challenge, but with some time
and dedication - the packages required to run this can and will be converted into
snaps which allow fast and easy rollback.

Whats nice about this, is you gain the flexibility of transactional packages
and it makes installation/rollback of the entire cluster - "A snap"! No pun intended.

This also has the side-effect of all contributed snaps being submitted to the
snappy store to help users along that are just getting started, and provide
some of the basic tooling for anyone interested in building their own snappy
based micro-cloud.

#### Show me the Money! I mean build!

This project was like any other project, assembled one component at a time. I
took the first Raspi2 and plugged in the spacers after hollowing out the board
holes a bit. The spacers were exteremly snug and needed some coaxing, so instead
of leaving them tight and filling the threads with plastic - it was a smarter
idead to hollow them out a bit, allowing the board to slide over the threads and
be secured with another spacer providing the layer above it.

![clementine box stage 1](/images/2015/july/clementine_box_stage_one.jpg)

The next step was prepping all of the SD Cards for first time boot.

    wget http://people.canonical.com/~platform/snappy/raspberrypi2/ubuntu-15.04-snappy-armhf-rpi2.img.xz
    unxz -c ubuntu-15.04-snappy-armhf-rpi2.img.xz | sudo dd of=/dev/sdX bs=1M

> This process took ~ 5 minutes per SD Card for me.

In typical geek fashion I checked each SD after I attached the board by plugging in a
Logitech KB/Mouse combo, plugged in the SD Card, and attached it to the TV over
HDMI to ensure everything booted properly.

![Clemetine Box stage 2](/images/2015/july/clementine_box_stage_two.jpg)


Once the entire tower was assembled, the next step was to crimp and attach the
CAT6 ethernet cables, and attach the switch to my router.

![Clementine Box Final](/images/2015/july/clementine_box.jpg)


## First Boot

First step is to install Docker on each rpi. This was pretty simple considering
there's a snappy package available

    snappy install docker

> As an aside, I found out later you can install packages from WebDM which is
> the snappy store. Its enabled on port 4200 by default with these images.

![Snappy Store](/images/2015/july/snappy_store.jpg)

> Another node, I really missed `juju run` here, repeating this across 4 nodes
> was rather tedius.

One thing however, is in order to run Swarm we will need to expose the TCP port
for the docker daemon.

    vi /var/lib/apps/docker/1.6.1.002/etc/docker.conf

And you will need to extend the DOCKER_OPTS line with:

    DOCKER_OPTIONS="-H tcp://0.0.0.0:2375 -H unix:///var/run/docker.sock"

This will expose the Docker Socket, as well as a TCP daemon. However I didn't
find an easy way to recycle the service, so I simply rebooted the Pi.
You can verify this worked by checking with netstat.

    (RaspberryPi2)ubuntu@rpi4:~$ netstat -nlp
    tcp6       0      0 :::2375                 :::*                    LISTEN      -

the TCP6 line there shows port 2375 is open and listening on IPV6. Good enough!

The next step is to load up Swarm on the Cluster.

    docker pull nimblestratus/rpi-swarm
    TOKEN=$(docker run --rm nimblestratus/rpi-swarm c)
    docker run --name="swarm-agent" \
        -d nimblestratus/rpi-swarm join \
        --addr=`ip -f inet addr show dev eth0|grep inet|awk '{print $2}'|sed -e 's#/.*##'`:2375 \
        token://${TOKEN}

Rinse and repeat on all nodes. For the record, I'm running the Swarm Manager on
my desktop for now, and only running the agents on the Pi's.

    docker run -d --name=swarm-manager -p 3456:3456 swarm manage token://${TOKEN}

You can verify each node is active in the cluster once you've loaded all 4 nodes
and attached your swarm-manger via:

    $ docker run --rm  swarm list token://${TOKEN}
    10.0.5.25:2375
    10.0.5.26:2375
    10.0.5.27:2375
    10.0.5.28:2375

## Swarms up, What about LXD?

Sadly, there is no snap for LXD - and this will be the first project I have to
build or obtain some help from my friend stgraber. That sounds like a great
topic for part 2 of the series.

More to come once we've got a successful load of the LXD snap.

Happy Hacking!
