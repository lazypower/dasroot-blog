Title: Continuous Integration with Juju and Drone CI
Date: 2015-07-15 10:33
Tags: devops, build pipeline, ci, drone, docker, juju, video, planet
Slug: 2015-continuous-integration-with-juju-and-drone-ci
Category: devops
Status: published
video: ZIcf4mefX14


### Preamble

Delivering your Charms to the community can seem like an uphill climb when you
have minimal and manual testing around your project. The ~charmer review process is
pretty rigerous and as anyone who has run the Gauntlet to attain ~recommended
status can attest, we really stress the service before approval. One of the
ways to have your review expedited is by including a full suite of tests that
deploy, configure, and stress the workload it is deploying. 

A little known fact about Juju Charms, is each Charm is a software project. Often
involving many developers from different focus groups, committing against different
features. The fact you *can* write a prototype  charm in about 20 minutes is a great byproduct
of our language freedom - but when it comes to delivering a consistent high
quality experience, you really need to adopt a delivery pipeline that rigerously
tests your charm quality through fast running individual unit tests, but also
you should be testing a full deployment scenario on the cloud.


I had a requirement of my CI Service being rapid to deploy, always configured
for all my projects (so version controlled CI config like Travis-CI), hosted
on premise so I can take my toys with me without worrying about data ownership,
and be flexible enough for me to extend via an API.

## Introducing Drone

Drone is a Continous Integration server written in GoLang by a team of dedicated
individuals centered around this Open Source project. Its light weight, built
on top of Docker to provide test isolation, and supports delivery of artifacts
to several providers, as well as deployment options for Modern PAAS providers
as well as git based delivery mechanisms.

It comes in 2 flavors, a hosted version over at [http://drone.io](http://drone.io)
as well as a deployable on premise edition, which will be covered in this post today.


## Prerequisits

In order to follow along, you will need to gather a few things.

- Cloud Credentials for your Integration Server (per project preferrable)
- A Juju environment
- A charm with Unit Tests and Amulet tests


## Standing up the CI Service

I'll be keeping the versions of Drone published in lock step with all the tags
present in the [Github Repository](http://github.com/chuckbutler/drone-ci-charm).


    juju deploy cs:~lazypower/drone


This charm will pull and configure the latest docker daemon, install the Drone-CI
binaries, and expose the DroneCI service on port 80.

What you will be greeted with when loading the Drone application URL is a single
button link to Documentation.

## Configuring Authorization


Drone requires an Authorization Provider in order to 'activate' itself. Drone
fully integrates with the API's as a consumer leveraging the service you login from.

### Setting up GitHub

#### Generate Client and Secret

You must register your application with GitHub in order to generate a Client and Secret. Navigate to your account settings and choose Applications from the menu, and click Register new application.

Please use **/api/auth/github.com** as the Authorization callback URL path.

![Github App Credentials for Drone](/images/2015/july/drone_github_setup.png)


Once you have your application configured in GitHub, set these API credentials
on the charm

    juju set drone github_client=XXX github_secret=XXX github_enabled=true

## Config Helper

This is beta, has very little error checking, and may or may not work given the
input you feed the script. Please use with caution. The charm ships with a
script to assist in configuring jobs. This is best run locally

    git clone https://github.com/chuckbutler/drone-ci-charm drone
    cd drone/scripts
    ./config -e {{environment}} -r {{repository https clone url}} -c {{charm name}}

You will receive output that is copy/pasteable to both the drone-ci repository
configuration, and the .drone.yaml to be embedded in the git repository.

#### Run the config helper
![Drone Script Helper](/images/2015/july/drone_script_helper.png)

#### Populate the project secrets
![Drone Repository Config](/images/2015/july/drone_repository_config.png)

#### Populate .drone.yml in your repository

As an example, i'll paste in some pseudo configuration. This is not 1:1, and
I did give a stellar breakdown over the format of this job in the explainer
video.

To investigate further on your own, consult the format doc for the `.drone.yml`
in the [upstream docs](https://github.com/drone/drone/blob/v0.2.1/README.md#builds)


    image: jujusolutions/charmbox
    env:
        - JUJU_TEST_CHARM='{{charm}}'
        - JUJU_REPOSITORY='/var/cache/drone/src/{{provider}}/{{username}}/'
    git:
        path: {{provider}}
    script:
        - sudo apt-get update
        - juju init
        - echo $ENVYAML | base64 --decode > ~/.juju/environments.yaml
        - juju switch $CIENV
        - mkdir ../trusty
        - cd .. && mv {{repo}} trusty/{{charm}} && cd trusty/{{charm}}
        - bundletester -F -l DEBUG -v



## Profit!

Simply make a commit and enjoy the results of using the cloud to run integration
suites of your project against the cloud provider configured.

Juju + Drone sitting in a tree :)

## Future

This is still very much beta quality in terms of exploration of what we can do
here. As in, how do you white list contributors so only certain PRs / Master
branch is run with a full integration suite, otherwise - only unit tests are
run?

Matrix builds against multiple cloud providers (v0.4 pending, will enable this)

If you've got any feedback, questions, comments about this - I'm happy to talk
with you about leveraging this setup for your own projects. You can find me
in #system-zoo on irc.freenode.net, as well as #juju.

All issues found should be filed against the [project on GitHub](https://github.com/chuckbutler/drone-ci-charm/issues).

#### Deploy Happy!
