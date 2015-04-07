Title: Expediting local isolation with Docker and Juju
Date: 2015-04-07 11:30
Tags: devops, docker, juju, workflow
Slug: 2015-local-isolation-with-docker-and-juju
Category: Shell
Status: published

As a Juju charmer, I often find myself irate at the level of dependencies I'm 
installing on my workstation just to review OPC (Other Peoples Code). Though
there are usually systems to isolate these dependencies like virtualenv and
tools of this nature - nothing really beats having your own isolated system
to catch all these dependencies and nuke them from orbit when you're done with
them.

### Charmbox - A boon in my workflow

A couple weeks ago we announced the GA of our experimental Docker images for
testing the latest TRUNK and to isolate your charm development experience. The
docker images are much lighter weight than the vagrant counterpart (even though
most systems that are not linux leverage vagrant in some fashion - boot2docker
is actually spinning up docker containers in a VM - nifty right?)

Leveraging charmbox has helped alleviate me from tainting my system with all
the testing dependencies introduced by the review queue. Each charm can run the
`00-setup` script as root and install whatever unholiness is required to really
leverage the charm. Most often this is as simple as just the amulet packages
but some charms go even further and install full API SDK's so they can really
root around in the deployed service and validate we have a good configuration.

While this is excellent in theory - in practice - I wound up with > 8 GB of
extra cruft installed, that I won't be using in my own every-day charm
development.

### Workflow Enhancement

Since we have this nifty isolation story - lets look at how we can somewhat
supercharge the workflow, and what this looks like. I'll only make 2
assumptions here.

1. you're using bash
2. you have docker installed

#### Manage Charm Context (Review, Work, Personal)

I have 3 particular contexts in which I will be focused on charms.

- My personal network of services (in home services)
- My obligations to canonical to develop interesting new workload charms
- My obligations as a charmer to review incoming charms

With these clearly defined "scopes" of charms, I find it often handy to keep
a repository of charms isolated in each context, and to work out of that 
particular repository until I have reached the end of my objective, and then
I can switch contexts.

#### Show me the code

<script src="https://gist.github.com/chuckbutler/4fb6d46a46cb48537e0d.js"></script>

#### How this works

The repositories setup in `$HOME/.bash_exports` manage the pointers to my charm
repository directories, and resemble any other charm repo, separated out by
`series/service`

The methods declared allow me to run a single command to switch the context
of my exported `$JUJU_REPOSITORY` - and set a sentinel file that is read on
each new shell execution.

The bits in `$HOME/.bashrc` are run on each new shell, and correctly set the
context of my `$JUJU_REPOSITORY` without any manual intervention. What I set
as my last context, will be the context of my next shell.

#### Thats great, but what does this have to do with Docker?

Really glad you asked! I spoke to the isolation, and contexts earlier - now
lets see how we can bridge the gap here to make this as seamless as possible.

<script src="https://gist.github.com/chuckbutler/e58ac6f206073016029f.js"></script>

The following alias when added to `~/.bash_aliases` will give you the `charmbox`
command. Which will spin up the appropriate docker container, and mount your
charm archives in the charmbox environment. Whats nice is you didn't have to
do any further fuddling with commands, and you automatically get the context
you're in mounted into the charmbox. With the --rm passed to docker, anything
we have done in the image is immediately removed once we exit the context
of the docker container, so we get fresh results, every time.

Deploy happy :)




