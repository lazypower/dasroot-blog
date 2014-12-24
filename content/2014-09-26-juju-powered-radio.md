Title: Juju Powered Radio! A protoduction experiment.
Date: 2014-09-26 19:09
Tags: juju, planet, radio, music, automation, experiment, video
Slug: juju-powered-radio
Category: Devops
image: /images/2014/Nov/juju_radio.png

September 26'th I undertook a rather daunting task of trialing something I strongly believe in that really took me out of my comfort zone and put me front and center of an audience's attention, for not only my talents, but also the technical implementation of their experience.


### The back story

I've been amateur [DJ](http://mixcloud.com/rahlgenesis/)'ing on Secondlife for about the last 7 months, and recently left the metaverse to pursue a podcast format of my show(s).  What I found was I really missed the live interaction with people during the recording of the set. It was great to get feedback, audience participation, and I could really gauge the flow of energy that I'm broadcasting. To some this may sound strange, but when your primary interaction is over text, and you see a feed erupt with actions as you put on more high energy music, it just 'clicks' and makes sense.

![](/images/2014/Sep/secondlife_dj.png)

The second aspect to this was I wanted to showcase how you can get moving with **Juju in less than a week** to bring a **production ready** app online and **ready for scale** (depending on the complexity of the app of course). It's been a short while since I've pushed a charm from scratch into the charm store - and this will definately get me re-acquiainted with the process our new users go through on their Juju journey.

So, I've got a habit of mixing my passions in life. If you know me very well you know that I am deeply passionate about what I'm working on, my hobbies, and the people that I surround myself with that i consider my support network. How can I leverage this to showcase and run a 'Juju lab' study?

### The Shoutcast charm is born

I spent a sleepless night hacking away at a [charm](https://code.launchpad.net/~lazypower/charms/trusty/shoutcast/trunk) for a [SHOUTCast DNAS server](http://www.shoutcast.com/BroadcastNow). They offer several PAAS, scaling solutions that might work for people that are making money off of their hobby - but I myself prefer to remain an enthusiast and not turn a profit from my hobby. [Juju](http://juju.ubuntu.com) is a perfect fit for deploying pretty much anything, and making sure that all the components work together in a distributed service environment. It's getting better every day - proof of this is the [Juju GUI](http://jujucharms.com) just announced [machine view](https://insights.ubuntu.com/2014/09/26/juju-machine-view-more-control-at-your-fingertips/) - where you can easily do co-location of services on the same server, and get a deep dive look at how your deployment is comprised of machines vs services.


### Observations & Lessons

#### Testing what you expect, never yields the unexpected
Some definate changes to just the `shoutcast charm` itself are in order.

- Change the default stream MIME from AAC to MP3 so its cross compat on *every* os without installing quicktime.
- Test EVERY os before you jam out to production - which may seem like a rookie mistake. I tested on Mac OSX and Ubuntu Linux (default configuration for 14.04) and everything was in order. Windows users however, that are not savvy with tech that stems from back in the 90's were left out in the cold and prompted to install Quicktime when they connected.  This is *not* ideal.
- the 'automatic' failover that I touted in the readme is dependent on the client consuming the playlist. If the client doesn't support multiple streams in the playlist, its not really automatic forwarding load balancing, but polling failure cases with resources.



#### Machine Metrics tell most of the story

I deployed this setup on Digital Ocean to run my 'lab test' - as the machines are cheap, performant, and you get 1TB of transfer unmetered before you have to jump up a pricing teir. This is a great mixture for testing the setup. But how well did the VPS perform?

I consumed 2 of the 'tiny' VPS servers for this. And the metrics of the transcoders were light enough that it barely touched the CPU. As a matter of fact I saw more activity out of supporting infra services such as LogStash, than I did out of the SHOUTCast charm. Excellent work on the implementation Shoutcast devs. This was a pleasant surprise!

![](/images/2014/Sep/ubuntu-do-prod-41c692c182e243318ebec209c576aff7---_116.png)
![](/images/2014/Sep/ubuntu-do-prod-22998e4b90d24ca682ce3892368139b1---_117.png)


#### Pre-scaling was the winner

Having a relay setup out of the gate really helped to mitigate issues as I saw people get temporary hiccups in their network. I saw several go from the primary stream to the relay and finish out the duration of the broadcast connected there.

The fact that the clients supported this, tells me that any time I do this live, I need to have at bare minimum 2 hosts online transmitting the broadcast.

Had this been a single host - every blip in the network would yield dead airspace before they realized something had gone wrong.

![Juju Scaled Shoutcast Service](/images/2014/Sep/Juju-Admin---Google-Chrome_127.png)

#### Supportive people are amazing, and make what you do, worthwhile

[Those that tuned in](https://plus.google.com/events/c00j89u3ipec61gmrlq11916fg8) genuinely enjoyed that I had the foresight to pre-record segments of the show to interact with them. This was more so I could investigate the server(s), watch htop metrics, refresh shoutcast, etc. However the fan interaction was genuinely empowering. I found myself wanting to turn around and see what was said next during the live-mixing segments.


### The Future for Radio Bundle Development


#### Putting the auto in automation

I've found a GREAT service that I want to consume and deploy to handle the station automation side of this deployment. [SourceFabric](http://sourcefabric.org) produces [Airtime](http://sourcefabric.org/airtime) which makes setting up Radio Automation very simple, and supports such advanced configurations as mixing in Live DJ's into your lineup on a schedule. How awesome is this? It's open-source to boot!

I'm also well on my way to having revision 1 of this bundle completed, since I started the blog post on Friday. Hacked on the bundle through the weekend, and landed here on Monday.

![](/images/2014/Sep/Workspace-1_126.png)

I'll be talking more about this after it's officially unveiled in Brussels.


## Where to find the 'goods'

The Shoutcast Juju Charm can be found on Launchpad: [lp:~lazypower/charms/trusty/shoutcast/trunk](https://code.launchpad.net/~lazypower/charms/trusty/shoutcast/trunk) or [ github](https://github.com/chuckbutler/shoutcast-charm)

The up-coming Airtime Radio Automation Charm can be found [on github](https://github.com/chuckbutler/airtime-charm)

> Actual metrics and charts to be uploaded at a later date, once I've sussed out how I want to parse these and present them.
