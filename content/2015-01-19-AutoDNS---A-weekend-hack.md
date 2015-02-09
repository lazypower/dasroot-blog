Title: AutoDNS - A weekend hack
Date: 2015-01-19 01:08
Tags: python, programming, dns, dyndns-replacement, planet
Slug: 2015-AutoDNS-a-weekend-hack
Category: programming
Status: published

This weekend I put together a quick and dirty python application to give me the functionality of a DynDNS client. While several of these services exist, something feels just a bit awry from the whole 'register so we can spam you about your DNS status - and UPGRADE TODAY!'. I'm already paying for DNS service from namecheap, as well as paying a minimal fee on AWS Route53... why not consume the Route53 API to accomplish the same thing at no additional cost, no marketing emails, and zero hassle?

### Skip the howto and go straight to the code? 

If howto's aren't your thing and you just want to look at the code - it's over on Github.
[github.com/chuckbutler/AutoDNS](https://github.com/chuckbutler/autodns)

MIT licensed so feel free to fork and modify as required!


# Overview
Perhaps you want to run a personal minecraft server, and would rather have a domain like minecraft.myhomelan.com vs the IP address. Or maybe you're like me and travel often enough that trying to OpenVPN home into your network is made a lot easier by having a DNS entry like 'itsasecret.mydomain.com' makes it trivial to remember while you're afar.

Regardless of your reasoning for wanting a dynamically updating DNS entry on a given host - you can do this now cheaply, effectively, and with a minimal time investment. 

## Pre-Requisites

You'll want an AWS account, and to generate some access keys via AWS IAM, that have the policy attached to update DNS records. There are excellent documents over on the [AWS Help](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_SettingUpUser.html). Its pretty simple.

### Sign into your AWS IAM Control Panel
![AWS IAM Control Panel](/images/2015/january/rt53_user_overview.png)

Sign into your AWS control panel, and select the USERS link. This will bring you to the
user management interface, where we can add our AutoDNS user.

### Create a New User
![Adding an IAM user](/images/2015/january/rt53_start_user_creation.png)

Select the blue `Create New Users` button

### Pick an appropriate and meaningful name
![Naming the IAM user](/images/2015/january/rt53_create_user.png)

Ensure you give your user a meaningful name - so as your IAM access list grows
you know exactly what each user is, what its for, and why you may or may not need
it in the future.

### Save the Credentials!
![Obtaining the Keys](/images/2015/january/rt53_save_credentials.png)

Once you have created the user, you are presented with Access keys. **SAVE THESE**.
The autodns client assumes these keys are exported in the environment as:

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY

so you may want to go ahead and place those in your `.bashrc` as exports now.


### Set the User Policy
![Setting the IAM Control Policy](/images/2015/january/rt53_attach_policy.png)

Before we're done in here, we'll need to inform AWS that this user should have
access to our RT53 domains. We get to the proper user management screen by clicking
on their name in the overview listing. From there, click on `Attach User Policy`

### Pick an appropriate policy
![Picking the proper policy](/images/2015/january/rt53_select_policy.png)

There are 4 possible RT53 access controls out of the default listing. We want to give
this user limited, full-control access to our domains. You can further scope this down
by building a specific policy to only edit certain domain resources - but thats outside
the scope of this tutorial.

## Installing AutoDNS

I haven't actually published AutoDNS to pypi yet - as there's a commercial project that exists
with the name. While the application is in this transitional state, I'm making it available as
as source project on github for you to install at your own leisure.

    git clone https://github.com/chuckbutler/autodns.git
    cd autodns
    python setup.py install

> **NOTE:** You may want to use a virtualenv to isolate dependencies, and not install autodns
> globally. There are several tutorials on the internet on how to do this, so I'll let you flex
> your google skills.

With AutoDNS installed, and our IAM credentials exported, we're ready to setup a configuration 
file.

    vim mydomain.yml


    ZONEID: P23QZY95VZHATG
    DOMAINS:
      - pad.autodns.net
      - minecraft.autodns.net
    TTL: 300

The required keys in this configuration are:

- ZONEID
- DOMAINS
- TTL

#### Where do I get the ZoneID?

This makes the assumption you already have the Domain as a Hosted Zone in AWS Rt53. The ZONEID can be found from the RT53 hosted zone listing like so:

![HostedZone Listing for ZoneID](/images/2015/january/rt53_zone_id.png)

### Run your first update!

    autodns path/to/config.yml -l $HOME/autodns.log

Refresh the listing for the hosted zone and you should see your DynamicDNS entries updated!

#### How do I do this automatically?

Glad you asked! This is exactly why I built AutoDNS. To get AutoDNS to run on a schedule you will need to place it in your users crontab:

    crontab -e

    * */1 * * * $HOME/run-dns.sh

with a shellscript that executes autodns like so:

    #!/bin/bash
    export AWS_ACCESS_KEY_ID=XXXXX
    export AWS_SECRET_ACCESS_KEY=XXXXX
    autodns /path/to/config -l /path/to/logfile.log

This will run AutoDNS every hour, and log the output to $HOME/autodns.log - effectively replacing any legacy DynDNS client functionality you may have had on your router. Note that this only gets run while the machine running AutoDNS is on.

Happy hacking!
