Title: Juju Plugins AHOY!
Date: 2014-02-15 17:02
Tags: juju, juju-plugins
Slug: juju-plugins-ahoy
---
Recently [Marco Ceppi](http://marcoceppi.com) has started an initiative to aggregate all the relevant juju plugins on GitHub. This is an excellent reason why the Juju community is a stellar example of distributed collaboration. Historically Juju plugins were distributed via Gists, Pastebins, Email, and other non aggregated means. They were a "hobby" of sorts - scratching itches and monkey patching extra features into Juju that didn't make it into core or may not make sense living there.

### What is a Juju Plugin?

> Plugins are simply scripts that are prefixed with juju- which can be found within your system's $PATH. Whenever you type juju $cmd, and $cmd is not an internal command found in juju help commands, Juju attempts to execute juju-$cmd within the context of your system's $PATH which is how the plugin system in Juju works. 

### Where Do I find these awesome plugins?

I'm glad you asked. The repository is hosted on GitHub. [juju/plugins](https://github.com/juju/plugins) is a "master" repository, warehousing all of the known juju plugins.  Want to add your own? No problem! Just fork the repository, checkout a topic branch for your plugin, and issue a merge request.

#### Workflow
```
git checkout $your-juju-plugins-fork

git checkout -b your-plugins-name

git commit 

git push
```

Then simply open a Pull Request and someone from the juju plugins team will review your work.

![](/content/images/2014/Feb/Selection_017.png)


I look forward to seeing the new plugins roll in to make everyone's juju experience that much more awesome!