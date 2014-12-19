Title: Moving Papertrail from Bash to Ansible
Date: 2014-02-10 20:02
Tags: charming
Slug: moving-papertrail-from-bash-to-ansible
---
When I initially wrote the PaperTrail(tm) Charm, I thought to myself "Lets get moving as quickly as possible for a MVP, and iterate after its done so I've got a basic blueprint on how it should function." As my first charm, it was extremely simple, fun to write, and functioned well enough that I used it in my own production environment.

There are some long standing issues I had with how I put it together. Mostly it's pretty hacky in the conditionals, and as I started to extend the functionality it looked pretty gross.

This was a prime opportunity for me to dust off my reading glasses and take [Ansible](http://www.ansible.com/home) out for a trial run. This was a fairly major rewrite, and took about an hour from start to finish. Even with referencing the [Module/API docs](http://docs.ansible.com/list_of_all_modules.html) every step of the way. To make things *even* easier there is a [github repository](https://github.com/absoludity/charm-bootstrap-ansible) that provides you with an Ansible boilerplate charm skeleton.  


If you would like to follow along at home, and see how many lines of code went into the rewrite, take a look at the open Pull Request (at the time of writing, pending unit/integration tests before I send a Merge Proposal to launchpad)

[Rewrite Pull Request](https://github.com/chuckbutler/papertrail-charm/pull/4/files)


![](/content/images/2014/Feb/Workspace_1_003.png)