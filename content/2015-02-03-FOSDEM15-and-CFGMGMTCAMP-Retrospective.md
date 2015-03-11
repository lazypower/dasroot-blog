Title: FCM2, FOSDEM15, and CFGMGMTCAMP Retrospective
Date: 2015-02-03 03:44
Tags: conference, devops, retrospective, planet, video
Slug: fcm2-fosdem15-and-cfgmgmtcamp-retrospective
Category: community
Status: published
Image: /images/2015/feb/lp-fosdem.jpeg

The first trip in 2015 was a huge conference circuit. I was given 3 weeks notice that I had to
prepare for the largest FLOSS conference in Belgium - FOSDEM. This was my first interaction with
any European organization that comes together in the name of Free as in Libre software. I have to
admit that the entire experience was way beyond anything I had expected. The culture surrounding
Free Software in Europe appears to be much greater than anything in the US.

## FLOSS Community Metrics

The community connection made with FLOSS Community Metrics was great. A gathering of about 50 people
that are interested in measuring community health, engagement, and gleening insights out of these
metrics to assist in shaping how they interact with the community.

Puppet had a great showing of their community dashboard built by Bitergia. The fine folks behind
Metrics Grimoire. Which is a highly compelling suite of tools for rapidly moving through your ETL
phase and just 'getting the data' into a format that is ready to be re-used in a database; ready
for visualizations to be created around the data.

This was a brilliant lead in to my Lightening talk which represented the state of the Juju community
and our efforts to measure how well we are doing in terms of interaction. We have spent some time
inventing a system to pull this data ourselves and have built a custom dash to show us the metrics
internally. We call it our "scorecard" and evaluate the metrics during our weekly standup where we
re-hash the major accomplishments and targets for the 2 week interation we are on.

This garnered arguably the most buzz during my stay in Belgium. I don't think many people had the
insight prior into how much we at Canonical genuinely care about our community, and how much we are
either measuring, or intend to measure - to ensure we maintain a high level of interactivity and
health of our growing communities.


<script async class="speakerdeck-embed" data-id="7d35a182958e424b85e036a4f89f8fb2" data-ratio="1.33159947984395" src="//speakerdeck.com/assets/embed.js"></script>

## FOSDEM

<iframe width="560" height="315" src="https://www.youtube.com/embed/JOq8YrRUFFc" frameborder="0" allowfullscreen></iframe>

FOSDEM was a gathering of over 5,000 hackers - both project contributors and fans consuming the
software, at the university de libre in Brussels. With tracks covering nearly every aspect imaginable
in the field:

- Programming
- Network Security / Infosec
- Licensing and Legal
- Web standards
- Configuration Management

Just to name a few of the larger topic tracks. I attended several talks and was literally blown away
by the raw passion of this meeting. Every single hacker there had the spark in their eye of 'this is
where I belong'.

When I took the stage on Saturday to deliver the introduction to Juju talk, I was fairly apprehensive
as this was the larges  crowd I had ever spoken in front of. Not something I took very lightly.
However in typical LazyPower fashion I burnt through my slides in just under 20 minutes, and spent
the remainder of the hour answering questions about the concepts of service orchestration, and
answered some highly insightful questions about the product, and our approach to providing the
ochestration patterns in a declarative model. I got the feeling that a majority of the audience were
still very much focused on Configuration Management, and hadn't quite reached the point where they
were looking for ways to solve complex application deployments through orchestration - but the fact
that I saw lightbulbs starting the shine in the crowd, and growing intelligent questions being asked
I feel that I left them with enough information to start their journey with some food for thought.

<script async class="speakerdeck-embed" data-id="be46af6ba8e14b6984a893227340d9b9" data-ratio="1.33159947984395" src="//speakerdeck.com/assets/embed.js"></script>


## CFGMGMTCAMP

Configuration Management Camp was held in the cozy town of Ghent. This was a brilliant change of pace
compared to the crowded city of Brussels. For two days I stepped off the train and had a nice 10
minute walk down into the streets of a college town, with narrow streets and heavy dutch influences.

Of course this meant that with me travelling I missed the introductory talks both days, which is a
shame. However - I did catch @littleidea's talk over Bosh. It was amusing and had a fair level of
inappropriateness - not enough that I personally was offendned - but it was edgy enough. To see a
top engineer of Pivotal take time explaining their approach to an orchestration tool that mixes some
concerns of Config Management, and exposes a level of Orchestration if you buy into the Bosh patterns
(not unlike Juju's declarative model) - the system appears really complex. Enough that @littleidea
gave an illustration of the chart having a learning curve that is 90 degrees. 

This talk was followed by a panel discussion with some of the greatest minds behind the companies
building the Configuration Management toolchains and communities. Chaired by SaltStack, Puppet, Chef,
and Ansible. All of which had great insight into the current status of the ecosystem, and things they
wish they had done differently in the past. The biggest of which, that caught my ear:

> Nobody is building on top of our tools, and this is where we have an opportunity for change.
> I wont be the guy to make that change, because I'm just not like that.
>
> - (paraphrased) @PuppetMasterD

Which really intrigued me. Juju as a tool-chain exposes the capacity to build on top of *any* given
configuration manangement tool - through our languge independent approach, and I feel like we were
grossly under-represented for him to make that claim.

But alas - in a perfect world we would all play together in the same sandbox of exploration and learn
from one another, and tool-warfare would be a thing of the past.


The workshops I ran in Ghent were well received, and I saw over 60 people between those that stopped
in day one, and those that came in and out during the second day where I was running scoped
deployments.

## Summation

All in all the entire experience was amazing, and I feel that there is so much
more to write about - but simply stated, it would turn this post into a wall
of text that maybe an 1/8 of the people stopping by would read.

I look forward to next year, and attending the largest conferences in Europe in the
name of Free an Libre software.

<iframe class="imgur-album" width="100%" height="550" frameborder="0" src="//imgur.com/a/euHTs/embed"></iframe>


