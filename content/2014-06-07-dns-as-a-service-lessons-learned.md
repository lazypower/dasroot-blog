Title: Juju DNS As A Service
Date: 2014-06-07 03:06
Tags: untagged
Slug: dns-as-a-service-lessons-learned
Category: Devops

I had the opportunity to plan and hack on a charm over the last few weeks that provided DNS as a service to supporting charms. (which subsequently has come between myself and the revamping of the [RAILS charm](/adopt-a-charm/)) This was a great opportunity to flex and test some of the boundaries within the Juju ecosystem to provide a solution out of the box.

#### Planning

This is the first charm I've followed a traditional planning phase of aggregating requirements and putting together a spec document. Which I found extremely helpful when it came time to implement the functionality of the charm. Normally I would spin up a fresh charm template, enter debug-hooks and just hack away at getting some MVP together to express what I feel it should provide. What I've found by doing a planning session first is I'm not a domain expert of any sense when it comes to DNS. I have a very vanilla experience with them by using the most common DNS entries: **A, CNAME, TXT**.

##### Gathering Reviewers (stakeholders)

I started by defining Stakeholders of the application suite. Meaning: Who's going to be using this, and why do they want to use it?

While my use case is very vanilla, not everybody will have this clear cut definition of how to use DNS. I encountered a great resource along my journey of planning - Matt Williams from Metaswitch. They use DNS to accomplish building a fault tolerant load balancer by stressing the limitations of a DNS Configuration using **SRV** and **NAPTR** records. Which is a great use case I had not even considered!

Among the engineers, I was also tasked with providing a solution that would appeal to CTO's - who may or may not be engineering experts, but understand the overarching goals of a network topology. This yields a certain 'ease of use' aspect - that it must be flexible in design to apply to an engineer, yet be simple enough for a business user to consume.

##### What should it do?

When defining what the charm itself should do, I found it useful to write user stories to define this kind of behavior. This not in turn gives me a definitive goal, but also helps shape any kind of planning when looking at the engineering aspect of the charm.

Below is a snippet of the user stories compiled that can be found in [doc/spec-document.pdf](https://github.com/chuckbutler/DNS-Charm/blob/master/docs/spec-document.pdf)


    As CTO (theoretical), I want to have the capability to have DNS management of my solutions done in minutes instead of weeks by creating simple Juju relations so that different charms get domains assigned and complex charms domain rules can be automated in a similar fashion to Route53 but work on any cloud instead of only AWS.

    As a Deployment Engineer (Matt Williams, Sean Feole), I want to MANAGE A RECORDS AND CNAMES WITH A CHARM so that MY POINTS OF ENTRY HAVE DOMAIN NAMES AND EACH UNIT OF A SCALED CLUSTER HAS A NODE DNS ENTRY.

    As a CHARM AUTHOR (Marco/Chuck/Maarten), I want a PROGRAMMABLE DNS WRAPPER WITH A CONSISTENT INTERFACE so that I CAN USE ANY SERVICE I HAVE PURCHASED DOMAIN NAMES FROM.

    As a Deployment Engineer (Matt Wiliams, Sean Feole) I want to have the ability to manage DNS in an Offline Environment, so that I’m not forced to remember/use ip addresses of my units.


This simple suite of user stories is very telling in the following regards:

##### Established Goals

- Simplicity is key. Distill away common blockers such as API Keys, API Routines, and manual intervention
- Make it extensible so it works on N providers, not just 1 or 2.
- Make contributing additional providers simple through documentation, and a clearly defined method to achieving the goal - relation based DNS
- Have the services define their DNS, and the provider be the gateway. I don't know how end users will be consuming the service, so give them the ability to define this subset of records.
- Make it programmatic, or automatic depending on the relationship.
- Have it work in isolated labs by providing the full suite service, and not dependent on a third party

With these goals in mind, we are ready to move into implementation specifics.
