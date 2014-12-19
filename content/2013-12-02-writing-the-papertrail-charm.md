Title: Writing the papertrail charm
Date: 2013-12-02 02:12
Tags: juju, charming
Slug: writing-the-papertrail-charm
---
This is a continuation of [My Weekend with Juju](/my-weekend-with-juju).



To get started, we need to invoke a helper provided by *charm-tools* to build our charm skeleton.

	juju charm create papertrail
    
This will create the following directory structure:

- charms
  - precise
     - papertrail
     - config.yaml
     - metadata.yaml
     - README.ex
     - hooks
         - config-changed
         - install
         - relation-name-relation-broken
         - relation-name-relation-changed
         - relation-name-relation-departed
         - relation-name-relation-joined
         - start
         - stop
         - upgrade-charm
         
I find the most useful practice is to dive right into the README and place some sane defaults for charm creation. It provides a focus during development, this style is called "[Readme Driven Development](http://tom.preston-werner.com/2010/08/23/readme-driven-development.html)" 

Rename README.ex to something a little more fitting of our writing style:
	
    mv README.ex README.markdown
    
Open it up in your favorite editor and lets set the context for our charm:

	#Papertrail Charm



    Overview
    --------
    
    This charm provides Papertrailapp logging from [Papertrail](http://www.papertrailapp.com). Papertrail provides instant log visibility. Use Papertrail's time-saving log tools, flexible system groups, team-wide access, long-term archives, charts and analytics exports, monitoring webhooks, and 45-second setup to ship your rsyslog logs, application output, and much more to Papertrail's logging service.
    
    
    
Excellent, the overview is the first thing presented to a potential user in the store. We've covered the base of explaning what papertrail is, and where I can view more information about the service. 

Think about the principals of juju and identify your configuration properties. 

	Configuration
	---------------------
	options:
  	port:
      type: int
      default: 0
      description: Papertrail syslog port
  	monitorall:
      type: boolean
      default: false
      description: Tail and ship all files in /var/log
  	applicationlogs:
      type: string
      default: ""
      description: Space separated list of paths to application logs (eg: /opt/app.log /var/log/mylog.log  )
    

Great, we have our first 2 feature sets, and a configuration constraint. 

 - Constraint 
 	- Papertrail's port is unique to each account, sometimes each application in the instance of hosted applications like Heroku. Therefore we cannot operate reliably directly after running <br> `$ juju depoy papertrail ` 
 - Feature 
	- if we want 100% coverage on all logs in /var/log there is a predicate feature to enable tailing everything in /var/log
 - Feature
  - for those apps that dont output logs to /var/log, provide the user a means to ship those logs as well.

Looking at how juju implements these relationships, lets get started on writing our first hook. The ` install ` hook.

### Install Hook

The installation hook takes care of the pre qualifications for running the charm.

*Commentary left inline as comments

<script src="https://gist.github.com/chuckbutler/7745943.js"></script>



### Start Hook

<script src="https://gist.github.com/chuckbutler/7746141.js"></script>


### Stop Hook

<script src="https://gist.github.com/chuckbutler/7746179.js"></script>

### Configuration Changed

<script src="https://gist.github.com/chuckbutler/7746188.js"></script>


#### Now, go forth and deploy!
Great, this is enough to start hacking around in the juju gui and see how this works with services deployed from Juju

In your shell, go ahead and deploy the charm from the local repository

` $ juju deploy --repository=charms local:papertrail `

This will push the charm from my local charms repository to the Juju controller unit, and deploy the papertrail subordinate service to your application canvas. 



## Charm Configuration

![](/content/images/2013/Dec/Screenshot_from_2013_12_02_01_49_51_5.png)

Expand the charm inspector on the Papertrail charm, and lets set up the port. 


## Charm Relations
![](/content/images/2013/Dec/Screenshot_from_2013_12_02_01_45_17_3.png)

Save the configuration changes, and draw lines to each container application we want to monitor.

![](/content/images/2013/Dec/Screenshot_from_2013_12_02_01_48_54_2.png)

Inspecting the charm of minecraft reveals the juju-info link relation drawn to papertrail, and lists the dependency chain.

### Validation

![](/content/images/2013/Dec/JuJu_Systems___Papertrail.png)



Awesome. Now we are ready for submission to the charm store after we tidy up the charm a bit, and place in the license


## Submission to the review queue

First and foremost, read the submission guidelines: [Charm Store Guidelines](https://juju.ubuntu.com/docs/authors-charm-store.html)

#### An aside on the charm submission process

Juju charms live in launchpad. For those that are unfamiliar, Launchpad is Canonical's public tool for software development projects. It provides repository support, bug tracking, and even a build system for personal package repositories.

With that being said, you should be familiar with Bazaar and the launchpad navigation. 


### Proof the charm

The goal is to have no output from charm proof.

	bushido precise/papertrail ‹master*› » charm proof
	E: Includes template icon.svg file. `

Looks like we need to tidy up and remove the boilerplate icon.

`$ rm icon.svg `

    bushido precise/papertrail ‹master*› » charm proof                                                                                 
    W: No icon.svg file.
    
Warnings are better than errors right? Now lets push this up to our launchpad bzr branch

	bzr init
    bzr ignore .git .gitignore
    bzr add .
    bzr commit
    bzr push lp:~lazypower/charms/precise/papertrail/trunk
    

### Start the review process

![](/content/images/2013/Dec/Bug__1023665__Charm_Needed__Papertrailapp____Bugs___Juju_Charms_Collection_15.png)

And now we wait!