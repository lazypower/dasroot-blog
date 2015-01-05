Title: Juju + Digital Ocean = Awesome!
Date: 2014-09-21 23:09
Tags: juju, digitalocean, planet, video
Slug: juju-digital-ocean-awesome
Category: Devops
summary: Juju on Digital Ocean, WOW! That's all I have to say. Digital Ocean is one of the fastest cloud hosts around with their SSD backed virtual machines. To top it off their billing is a no-nonsense straight forward model. $5/mo for their lowest end server, with 1TB of included traffic. That's enough to scratch just about any itch you might have with the cloud.
video: 1igZWnCi8Ac


> Syndicators, there is a video above that wont make it into syndication. Visit the source link to view the video.

> Additional note - this is now part of the [official juju documentation](https://juju.ubuntu.com/docs/config-digitalocean.html)

Speaking of scratching itches, if you haven't checked out Juju yet, now you have a **prime, low cost cloud provider** to toe the waters. Spinning up droplets with Juju is very straight forward, and offers you a hands on approach to service orchestration thats affordable enough for a weekend hacker to whet their appetite. Not to mention, Juju is currently the #1 project on their API Integration listing!

![Juju #1 in API Integration for Digital Ocean!](/images/2014/Sep/Selection_103.png)




In about 11 minutes, we will go from zero to deployed infrastructure for a scale-out blog (much like the one you're reading right now).


#### Links in Video:

- Juju Docean Github - [https://github.com/kapilt/juju-digitalocean](https://github.com/kapilt/juju-digitalocean)
- Juju Documentation - [http://juju.ubuntu.com/docs](http://juju.ubuntu.com/docs)
- Juju CharmStore - [http://jujucharms.com](http://jujucharms.com)
- Kapil Thangavelu - [http://blog.kapilt.com/](http://blog.kapilt.com/)
- The Juju Community Members on DO - [http://goo.gl/m6u781](http://goo.gl/m6u781)

### Text Instructions Below:

Pre-Requisits:

- A Recent Ubuntu Installation (12.04 +)
- A CreditCard (for DO)


##### Install Juju
    sudo add-apt-repository ppa:juju/stable
    sudo apt-get update
    sudo apt-get install juju

##### Install Juju-Docean Plugin
    sudo apt-get install python-pip
    sudo pip install juju-docean
    juju generate-config

##### Generate an SSH Key
     ssh-keygen
     cat ~/.ssh/id_rsa.pub

##### Setup DO API Credentials in Environment
    vim ~/.bashrc

You'll want the following exports in $HOME/.bashrc

    export DO_CLIENT_ID="XXXXXX"
    export DO_API_KEY="XXXXXX"

Then source the file so its in our current, active session.

    source ~/.bashrc

##### Setup Environment and Bootstrap
  vim ~/.juju/environments.yaml

Place the following lines in the environments.yaml, under the `environments:` key (indented 4 spaces) - ENSURE you use 4 spaces per indentation block, NOT a TAB key.

     digitalocean:
          type: manual
          bootstrap-host: null
          bootstrap-user: root


##### Switch to the DigitalOcean environment, and bootstrap

     juju switch digitalocean
     juju docean bootstrap


Now you're free to add machines with constraints.

     juju docean add-machine -n 3 --constraints="mem=2g region=nyc3" --series=precise

And deploy our infrastructure:

    juju deploy ghost
    juju deploy mysql
    juju deploy haproxy

    juju add-relation ghost mysql
    juju add-relation ghost haproxy

    juju expose haproxy

From here, pull the status off the HAProxy node, copy/paste the public-address into your browser and revel in your brand new Ghost blog deployed on Digital Ocean's blazing fast SSD servers.


### Caveats to Juju DigitalOcean as of Sept. 2014:

> These are important things to keep in mind as you move forward. This is a beta project. Evaluate the following passages for quick fixes to known issues, and warnings.

Not all charms have been tested on DO, and you may find missing libraries. Most notably python-yaml on charms that require it. Most "install failed" charms is due to missing python-yaml.

A quick hotseat fix is:

    juju ssh service/#
    sudo apt-get install python-yaml
    exit
    juju resolved -r service/#

And then file a bug against the culprit charm that it's missing a dependency for Digital Ocean.

While this setup is amazingly cheap, and works really well, the Docean plugin provider should be considered beta software, as [Hazmat](http://blog.kapilt.com) is still actively working on it.

All in all, this is a great place to get started if you're willing to invest a bit of time working with a manual environment. Juju's capable orchestration will certainly make most if not all of your deployments painless, and bring you to scaling nirvana.

Happy Orchestrating!
