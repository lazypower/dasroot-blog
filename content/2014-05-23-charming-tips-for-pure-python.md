Title: 5 Tips for 'Pure Python' Juju Charms
Date: 2014-05-23 02:05
Tags: juju, charming, python, ubuntu
Slug: charming-tips-for-pure-python
---
![](/content/images/2014/May/charming_in_pure_python.png)

*Special thanks to Tim for use of his comic above*

When I'm prototyping charms, I tend to reach for the quickest tool to accomplish the task. Which is Bash. Unfortunately - Bash charms get unwiedly quick and are typically full of hacks to complete a given task where a touring complete programming language would lend itself really well. 'Why not use Chef, or Ansible, or one of the other framework's you've already blogged about?" you say. Simple, because **Juju gives you options**. And I'd like to present most of those to anyone looking to get started. 

> Again, sorry about the theme bug. If you don't see the Gists below, just refresh and they will show up.

### Tip 1: Use Charm Helpers

Charm Helpers is a community contributed and maintained library to assist in writing charms rapidly. All community contributions are gated through Code Review and show up in the Juju Review Queue like any other charm merge proposal.

![](/content/images/2014/May/charm_helpers_mp.png)

> To get started quickly using Charm Helpers, skip to Tip 3 and use make sync-charmhelpers in tandem with a charm-helpers.yaml

    branch: lp:charm-helpers
    destination: lib/charmhelpers
    include:
        - core
        - fetch
        - contrib/network



#### Charm Helpers exposes common tasks such as:

* Installing apt packages
* Determining the networking devices on the machine
* Using hook context within your python code
* Fetching configuration variables from the juju environment

#### Example Snippet of a Charm Helpers enabled source file

<script src="https://gist.github.com/chuckbutler/9ad5d92250f05481e008.js"></script>



### Tip 2: Unit Test Your Hook Code

Unit testing is a fundamental dicipline to ensure your code is doing what you expect it to do. There's a huge movement within the charming community to start testing charms, and lowering charm ratings for those contributions without tests. Simply stated, if we can verify your charm behaves in CI, you get bonus points for the effort and ease of management for the charmers.

You can accomplish this with typical python-unittest and python-mock libraries.

> If you're new to testing, I would start with the [unittest docs](https://docs.python.org/2/library/unittest.html)

#### An example test of the common code above:

<script src="https://gist.github.com/chuckbutler/40bd33844f9a614b2d05.js"></script>


### Tip 3: Use A Makefile

Makefiles are excellent for 'gluing together' a project's components and creating 'build recipes' for different tasks. I've compiled a few Makefile lines that I find myself reusing over and over.

<script src="https://gist.github.com/chuckbutler/04daa904e603215ff9e9.js"></script>

### Tip 4: Write Amulet Tests

**[github.com/marcoceppi/amulet](http://github.com/marcoceppi/amulet)**

Chances are your service isn't stand-alone and integrates with other services. Such as Wordpress has a dependency on MySQL. Amulet gives charm authors a way to test their deployment topology by validating data sent over the wire, and probing deployed systems. The Amulet README does a better job of explaining it, so I'll kindly point you in that direction.

### Tip 5: Resist All Temptation To Symlink Every Hook Against A Single .py File

Windows support is coming. If you want to avoid the headache (and by proxy save us headaches) during this porting effort as it emerges, **do not symlink every hook against a single .py file**. Windows does not support symlinks. This is not portable.

And as a minor point to the above, it's good practice to write OS independent code. (for example, when defining paths, use os.path.join() instead of hard-coding '/var/log/example.log') This will go miles in saved headache when tracking down issues during the porting process.


#### With these five ninja tips in mind you'll be hacking up a storm on your shiney new Python based Juju Charm in no time!
