Title: Adopt a Charm
Date: 2014-05-09 17:05
Tags: charm-maintainership, ubuntu
Slug: adopt-a-charm
Category: Devops

As a Juju Charmer, I really care about the Juju Ecosystem. I want all of our building blocks, or amino acids in your deployment DNA to be solid pieces for everyone to use, benefitting from the shared knowledge of the global community.  This post is an abstract about community building, and how my experience went looking to contribute to the juju ecosystem as a whole.


You've been poking around in the juju ecosystem for a while. You've found your pain points or 'papercuts' as we call them. You've opened bugs and received minimal feedback on them because the author has moved on. What do you do?

## Adopt a charm!

This is _literally_ nothing new. The juju ecosystem was built around this concept, which is very prevalent in other Open Source Software projects. We have a **mandatory open source licensing model** on the charm code itself to be accepted into the Juju charm store specifically for this reason. Imagine if your charm code was proprietary, and licensed with some angry "do not modify" license, and it broke on you a year after deployment because the maintainer won the lottery and moved to an island.

![Devops Borat on the beach](http://static.guim.co.uk/sys-images/Film/Pix/pictures/2008/07/02/borat460.jpg)

> Devops Borat has won the lottery, very nice!

Well, I've encountered something similar. a community template had a typo in the README and I opened a merge request against the maintainers branch... the maintainer had moved on and was no longer maintaining the code. Which you can see [here](https://github.com/Altoros/juju-charm-chef/pulls)

#### I want to contribute - it's my turn to drive.

The first step is to e-mail the [juju list](https://lists.ubuntu.com/mailman/listinfo/juju), to ensure someone else hasn't stepped into the position without announcement, or give the maintainer a chance to toss their hat back into the ring. That and it's just good manners.

![](/images/2014/May/email_the_juju_list.png)

##### Success, it's my time to shine


My first task is to poke around in the [rails-charm bug tracker](https://bugs.launchpad.net/charms/+source/rails) where I discovered there were several action items left that had not been resolved.

### Before
![](/images/2014/May/rails_issues_before-1.png)
### After
![](/images/2014/May/rails_issues_after.png)

As you can see, the simple presence of [bug maintenance](https://wiki.ubuntu.com/Bugs/Bug%20triage) will go a long way towards helping a projects apperance. But this is only a cosmetic fix a this point.

This is step 1, and I will continue to document and publish about my experience.
