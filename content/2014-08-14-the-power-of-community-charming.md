Title: The power of community charming
Date: 2014-08-14 12:08
Tags: juju, charming, charm-maintainership, charms, charm-store, planet
Slug: the-power-of-community-charming
---
The Juju Charm Store has been in a bit of a spotlight lately, as it's both a wonderful tool and a source of some frustration for new charmers getting involved in the Juju ecosystem. We wanted to take this opportunity to cover some of the finer aspects of the Juju Charm Store for new users and explain the difference between what a **recommended** charm is vs a charm that lives in a **personal namespace**.


### Why is there a distinction?

Quality.  We want all the charms in the Charm Store to be of the highest quality so that users can depend on the charms deploying properly and do what they say they are going to do.

When the Charm Store first came into existance, it was the wild west. Everyone wanted their charm in the Charm Store and things were being promoted very rapidly into the store. There were minimal requirements, and everything was **new** and **exciting**. Now that Juju has grown into its toddler phase and is starting to walk around on it's own - we've evolved more regulations on charms. We have defined what makes a high-quality charm, and what expectations a user should have from a high quality charm. You can read more about this at the [Charm Store Policy doc](https://juju.ubuntu.com/docs/authors-charm-policy.html) and the [Feature Rating doc](https://juju.ubuntu.com/docs/authors-charm-quality.html)

The bar for some of the features, and quality descriptors may seem like extremly high hurdles for your service to meet to become a ~charmer recommended service. This is why Personal Namespaces exist - as the charmer team continues to add and expand the Charm Store with charms that meet and/or exceed these quality guidelines - we **encourage everyone** to submit their Juju charm for world wide consumption. You may disagree with FOSS licensing, or perhaps data-handling just isn't something you're willing to do with the service that you orchestrate. These are OK! We still want your service to be orchestrate-able with Juju. Just push your charm into a Personal Namespace, and you don't even have to undergo a charm review from the Charmers team unless *you really want* someone proofing your code, and service behavior.


### What differences will this have?

#### Deployment
We've all seen the typical CLI commands for deploying charmer recommended charms.

`juju deploy cs:trusty/mysql`

There will be a descriptor changed for your personal namespace

`juju deploy cs:~lazypower/trusty/logstash`

#### Charm Store Display
Personal namespace charms will display the charm category icon instead of a provided service icon. This is a leftover decision in the Charm Store that is subject to change, but at present writing - is the current status of visual representation.

#### Submission Process

To have your charm listed as a charmer team recommended charm, you have to under-go a rigorous review process where we evaluate the charm, evaluate tests for your charm, and deploy & run tests against the provided service with different configuration patterns, and even introduce some chaos monkey breakage to see how well the charm stands on its own 2 feet during less than ideal conditions.

This involves pushing to a launchpad branch, and opening a bug ticket assigned to ~charmers, and following the cycle - which at present can take a week or longer to complete from first contact, depending on Charmer resources, time, etc.

### I don't want to wait 
#### my service is awesome and does what I want it to do. Why am I waiting?

You dont have to! The pattern for pushing a charm into your personal namespace requires zero review, and is ready for you to complete today. The longest you will wait is ~ 30 minutes for the Charm Store to ingest the metadata about your charm.

`bzr push lp:~lazypower/charms/trusty/awesome-o/trunk`

Thats all that's required for you to publish a charm under your namespace for the Charm Store. To further break that down:

**lp:~lazypower** : This is your launchpad username

**/charms/** : in this case, charms is the project descriptor

**/trusty/** : We target all charms against a series

**/awesome-o/** : This is the name of your service

**/trunk/** : Only the /trunk branch will be ingested. So if you want to do development work in /fixing_lp1234  - you can certainly do that. When work is completed, simply merge back into /trunk! It will be available immediately in your charm listed in the Juju Charm Store.


### Charm Store: Personal Namespace (other)

In the Juju Charm Store as it exists today, there is a dividing bar below the recommended charms for 'other' - and this warehouses bundles, personal charms, and is a place holder for future data types as they emerge.

![](/content/images/2014/Aug/Selection_069.png)

As you can see by the image above, there is quite a bit of information packed into the accordion. Let's take a look at the bundle description first:

![](/content/images/2014/Aug/bundle-diagram.png)

As illustrated, no review process was done to submit this bundle, it has 0 deployments in the wild of 5 services/units.

![](/content/images/2014/Aug/namespace_charm.png)

Looking at a charm, we have the same basic level of information, and we see that the  charm itself is in my personal namespace.  trusty|lazypower - designates the series/namespace of the charm listing. 


### Charm Store: Recommended Charms

Recommended charms have undergone a rigerous testing phase by the Juju Charmer team, include tested hooks, and tested deployment strategies using the [Amulet testing framework](https://juju.ubuntu.com/docs/tools-amulet.html). You can read more about this at the [Charm Store Policy doc](https://juju.ubuntu.com/docs/authors-charm-policy.html) and the [Feature Rating doc](https://juju.ubuntu.com/docs/authors-charm-quality.html)

They have full service descriptor icons provided by the charm itself, and are deployable via juju deploy cs:series/service

![](/content/images/2014/Aug/Selection_070.png)

Notice the orange earmark in the upper right corner. This denotes the charm is a ~charmer recommended service, as it has undergone the review process and accepted into the charmer's namespace of the Juju Charm Store.

### Which is right for me?

When deciding how to get started working with Juju and what level you should start at for your charm - I can't stress enough. **Get started with your personal namespace**. When you feel your charm is ready (and this can take a while during R&D) Then submit your charm for official ~charmer review. 

The process of getting started with personal namespaces is cheap, easy, and **open to everyone**. It's still very much the wild west. Your charm will be in the hands of users 10x faster using personal namespaces, you still have the opportunity to have it reviewed by submitting a bug to the [Review Queue](http://manage.jujucharms.com/tools/review-queue), and you become the orchestrating master of your charmed service.

If you're an Independent Software Vendor and would like to start with your charm In the ~charmers recommended list, feel free to submit a review proposal, however - you are now agreeing to be subject to the Charm Store review policy, your charm must meet all the criteria of a good charm, and the review process can take some length of time depending on the complexity of your service.


### What is the future of charm publishing?

The Juju Ecosystem team has spent many hours discussing the current state of charm publishing and how to make this easier for our users. On the horizon (but with no foreseeable dates to be published) there are some new tools emerging to assist in this process.

`juju publish` is a command that will get you started right away by creating your personal namespace, and pushing your charm (and/or revisions) to your branch with the appropriate bugs/MP's assigned.

A new Review Queue is being implemented by [Marco Ceppi](http://marcoceppi.com) that will aid us in first contact, getting 'hot' review items out the door quickly, and triaging long running reviews appropriately. 


### Where do I go for help?

Should you have any problems getting moving with publishing your charm, you can always contact the [mailing list](mailto:juju@lists.ubuntu.com), join us in #juju on irc.freenode.net, or open a question on [Ask Ubuntu](http://askubuntu.com) tagged #juju

