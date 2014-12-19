Title: CRM's and why they suck
Date: 2012-02-19 00:20
Tags: untagged
Slug: crms-and-why-they-suck
Category: Opinion

CRM's - Who needs them anyway?
-----------------------------

I was recently tasked with setting up a CRM solution for my job. I for one, want to point out that every last single CRM system I've demo'd has suffered from negligence in implementation, and it just plain sucks when you're trying to white-label a CRM.  No one single CRM will scratch every itch you require as a business entity. You have to modify your workflow across the board to make it worth while.

Now don't get me wrong. CRM's serve a purpose, and it's a lofty goal that they are attempting to achieve. For most companies you need some system in place to keep track of contacts and what the status is with the last contact. 100+ contacts a day can get EXTREMELY confusing for any one single department to keep track of. For the new readers that don't know; I work for an online marketing agency. We come in contact with circa 300 potential leads a day. Not to mention our 40+ clients, hundreds of affiliates, and other channels.

So, if every CRM sucks... What do you do? You write your own. How many of us honestly need Email list management as our CRM? My company doesnt. Does yours? How many of us need to manually enter every contacts details? I dont, should _YOU?_ I want to give back to this space, and offer a cruft-less version of Customer Management. Leads to affiliates to accounts - lets push back in a space that has otherwise been dominated by stale projects demanding too much money for what they offer.

Who's with me?

<!-- more -->

The following is an example flowchart of how I perceive this to work - using Web to Lead as an example.

<script src="http://www.gliffy.com/diagramEmbed.js" type="text/javascript"> </script>
<script type="text/javascript"> gliffy_did = "3311664"; embedGliffy(); </script>

The beauty in this system is simplicity by design. Currently our reporting system is clunky. We dont have any way to track "first page submits" other than Google Analytics and in page event tracking.. We track page clicks, conversions, and exit traffic. This leaves gigantic gaps in our intelligence reporting. This is where CRM would come into play - we assign leads in the CRM and track its conversion process through the system. Since most of the "white label" CRM solutions are geared towards E-Mail and phone campaigns - this leaves us with an interesting conundrum being nearly web-to-lead exclusive. How do we accomplish this in a SANE method that is flexible enough to support web to lead while not bloating it into a juggernaut that really accomplishes goals we didn't set out to complete? By cutting out the cruft and hoops you would have to jump through - we can establish this as a plugin for our existing systems in a post-receive-hook style HTTP Post - and keep tabs on the data.

Since we have a Call Center backend to consider as well - specifically Five9 solutions Hosted callcenter softare - through connectors we can achieve the same level of data redundancy. I'll be moving forward with this soon - and posting my findings.
