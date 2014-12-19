Title: Juju expose my-experience
Date: 2013-12-25 22:12
Tags: juju, experience
Slug: juju-expose-my-experience
---
I'm right around the one month mark with my juju lab and I feel like I've progressed a long way in poking around in the space. I went from having watched and briefly interfaced with Juju to deploying clusters of apps to learn how they interface with one another.

Along the path I've been maintaining a self dialogue that I haven't been able to finish until now. My initial step into the Juju waters was configuration of the PaaS logging service Papertrail. This subordinate charm was more my depth charge to test the waters of the charm submission process. It was simple enough to fleshed out in a few hours having only written one very basic charm before, and came with a pre-existing charm request. 

After I reached the first submission of the Papertrail charm, I immediately set out to work on the Errbit charm using Marco Ceppi's bash driven Discourse charm as a guide. What I yielded was [a functioning](https://github.com/chuckbutler/errbit-charm/commit/c11c50785c4042933a39857f830100310340fd15) installation routine that utilized Marco's code as a base. It was fun, and survived a hdd swap, but I wanted to flex an area of my brain that I knew more intricately than Bash.
 

### Breaking the OPC habit

The core belief of chef is that you should write your own cookbooks for your organizational needs and deploy from your in house 'special blend' of configuration magic. In my day job, I have made a few low level dependency cookbooks that give me a 'base' system. Configured to provide clean slate deployment from the development staff, preconfigured server templates for more complex application deployments - typically Rails or PHP stacks, and Capistrano powered release deployment and lifecycle management.

In my capistrano deploy configurations I was making excessive use of plugins, and gems. Most of which I knew what they were doing, however I always relied on Foreman to manage my process voodoo for environment flags, and pid management. By using these tools I cut myself out of an opportunity to template and reduce deployment time. Foreman generates "OK" application upstart scripts, however I was continually running into corner case issues that wouldn't have happened had I written an upstart script myself, and deployed as a template that gets updated on every release-upgrade This is a prime example of where blindly consuming O.P.C. (Other Peoples Code) will stunt your effective learning. With the sheer volume of applications I was handling the tradeoff was moving fast in the name of progress. When something got in my way I turned instead of studying.  

With that in mind, I digress back to the theory on using chef, cookbooks, and juju's hooks ecosystem.  I can see chef as a boon in this, but only if there are a baseline set of community audited cookbooks. I feel that the ubuntu community has a high quality gating process through peer review. It feels more fluid, and accepting than the chef peer review process.



#### Orchestration is higher level than configuration management

Using chef in juju at first is a bit of a mindwarp. Typical chef server provisioning involves a manifest, and handles deployment of the entire server stack vs a responsive hook system. This may be an indicator that chef has larger object oriented capacity than I was using previously. 

One of the many tradeoffs I took with this approach is mixing and matching the hooks in bash and chef wrappers to prevent diving into the chef-solo agent when all I wanted to do was restart a service. I did however initially provision the start/stop hooks from within chef, and enjoyed watching my logs fill up with false positives from the NGINX upstart provider. Moving the logic into pure bash has removed this hurdle, but sacrifices a bit of the code maintainability. 
 


### Prototyping with Python is fun and fast

My lessons with Juju drove me to look at python. Its powering most of the core juju dev framework like `charm-tools` and `amulet`. I knew very little python coming into this experience so my first stop was the provisioning helper Fabric. I wrote a quick [deployment routine in Fabric](http://blog.dasroot.net/fabric-qemu-and-steamcmd/), and translated the routine to bash driven hooks for the [Starbound Charm](https://github.com/chuckbutler/starbound-charm/)


>I'm pretty excited about this, as it cuts a corner away from the chef depency. Moving into a Python first provisioner would cut down on the installation hook quite a bit. At writing deploying to an LXC container takes just under 4 minutes. The provisioning portion from time of first hook execution is hanging right around the 2 minute mark. This really makes me want to look into ansible as a provisioning framework.





### Documentation 

The juju documentation covered about 95% of my questions. Barring peer relation information not being where I expected to find it; everything else was covered with example cases and API docs.







