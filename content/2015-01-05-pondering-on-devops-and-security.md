Title: Pondering on Devops and Security
Date: 2015-01-05 13:30
Tags: security, infosec, metasploit, docker, devops, planet
Slug: 2015-pondering-on-devops-and-security
Category: devops
Image: /images/2015/january/infosec.jpg
ImageCredit: Special thanks to Dan Tentler for his CreativeCommons shot from Defcon19 https://www.flickr.com/photos/vissago/6033405562/
Status: published

Security research has an interesting culture, and its not entirely unlike devops. They are typically kept as a separate entity of the organization and left to do their work supporting the other areas of business. Pen testing reports are published and work items are assigned - but what if we could take that a step further and make infosec a real part of the process?

I've been thinking about this subject quite a bit recently, and it has evolved from the original concept of leveraging devops toolchains in infosec research. Pen Testers typically have a set routine of vulnerabilities to check, and this tedious process has been automated by a few toolkits like [Metasploit](http://www.metasploit.com/). The original idea was to take toolkits like metasploit, and develop a suite of routines using the Juju Relationship system to test common vulnerabilities, such as:

 - Framework CVE's
 - Known Rails Injection tactics
 - Session Hijacking leveraging peering hosts
 - SQL Injections of User Input Fields leveraging kits like splinter or selenium

to name a few examples.

This has great implications on time reduction, reusablility of existing code/practices, and become part of the deployment pipeline for testing for known security vulnerabilities. Freeing up pen testers to resume research on new and interesting ways to default security practices.

With technologies like Docker reducing the overall surface attack area and the rise of containerized computing - this leads me to the next step in evolution of this thought process.

### The Pitch

> What if we made full container pentesting part of the modern deployment pipeline?

#### The proposed Workflow:

- Developer commits Code to Repository
- CI pulls code and runs unit tests
- CI builds a containerized deployment artifact
- Integration tests are run against the container(s) in a testing environment
- Automated Pentests are then run against the container artifacts
- - Relationships establish the constraints of the test
- - If HTTP interface/relation is joined - kicks off a suite of browser automation attacks
- If all test suites pass, container is then delivered to target environment

The use of Containers ensures the testing surface reflects an accurate representation of the production environment. After all - most container hosts are extremely light weight installations to support a maximum density deployment of applications. The fact that container context's in the Docker etho's are immutable also allows us to tightly control the scope, versions, and attack surface under load. The artifacts from a failed Pen Test would also allow post-mortem metrics to be collected against the test. If this were all being built with a juju bundle - a developer/infosec specialist could then pull the bundle, redeploy on their laptop and get a full 360 degree view into the failure and make the required adjustment.

Imagine the scenario that you are a Rails shop, running a long-standing Rails3 application. A developer adds a gem that introduces a large scale SQL injection bug that has the possiblity of a user dropping all tables in your database. These are the kinds of situations your organization wants to catch in testing vs in the wild. Automated pen-testing that crawls a website, inspects every input and attempts to force submit sql injections, and can then validate database entries were indeed altered that were not intended - would be extremely invaluable.

While this won't prevent your users from choosing poorly formed passwords, often less than 8 characters and/or single word variants in plain english - this can prevent the next wave of catastrophy from striking your app.

Leveraging technologies like Docker to warehouse and build/ship your app, then placing juju orchestration on top of this stack, you can automate away several layers of pain with charms. "Servers attacking servers" so to speak. Making this process automated ensures repeatability and sustainability of the work that your infosec team does on a routine basis, and makes the process more approachable, digestible, and understandable to everyone involved from the infosec team, to the developers, to ops.

But this is only the beginning, there's certainly more to this that I haven't touched. I'm very interested to hear your thoughts about this, and what you feel are the strengths and weaknesses of this pattern.


