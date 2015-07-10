Title: Automate DNS with Juju
Date: 2015-07-10 06:28
Tags: juju, devops, dns, planet
Slug: 2015-dns-automation-with-juju
Category: devops
Status: published
Image: images/2015/july/dns_charm.png

## Announcing Third Party Support for the DNS Charm

To anybody that followed the [DNS charm](https://github.com/chuckbutler/DNS-Charm)
development last year I had a lofty goal of introducing a third party plugin
framework, which allows the user to specify a third party DNS server, and
reconfigures the DNS charm to act as a proxy for all services in the environment,
shipping their DNS information off to the DNS provider.


### Starting with Rt53

Today, the DNS charm works with Rt53 based DNS. This was a quick integration
path and only supports a subset of the overall records that the DNS charm aims
to support. However, it works with the most common records you will typically
want to use in your deployments:

- CNAME
- A

This support landed in the `v0.2.4` of the charm - available
[here](https://github.com/chuckbutler/DNS-Charm/releases/tag/v0.2.4) along with
full documentation on how to get started with the [Rt53 Provider](https://github.com/chuckbutler/DNS-Charm/blob/master/contrib/rt53/README.md)

### A bit of history


The DNS charm by default assumes you want to work in an 'offline environment'
and will configure a bind9 single host to provide DNS to your LAN. This was to
scratch an itch I had for wanting a DNS server on my LAN, as well as providing
some simple DNS caching to speed up requests flying across my network.

This had further implications for [Metaswitch](http://www.metaswitch.com/) who
was working with us during the TADHACK event of 2014 to deploy their NFV solution
with Juju. The DNS charm provided them an easy way to get moving with the demo
and isolate the DNS to running in their environment. While the charm itself
doesn't yet support scale out, multi-host DNS with a BIND provider, this is on
the roadmap to eventually be triaged.

As this was a very limited in scope, and wasn't terribly useful to production
deployments (Most people dont manage their own DNS servers, they rely on the
DNS provider, or pay for hosted DNS to ensure a given SLA) - I needed to wrap
service API's which vary from provider to provider, and encapsulate that knowledge
in the charm.

Each provider will support a subset of records from the DNS spec, and expose
different data points - so a plugin system was necessary. Thanks to pythons
module loading, this became a trivial task.

### How does this work exactly?

** A note beforehand, if you want to contribute: **
> I have [documentation](https://github.com/chuckbutler/DNS-Charm/blob/master/docs/provider.md)
on writing a provider, and how to get started. The only requirement is that you
implement the common hooks, isolate your dependencies, and clearly document and
test the provider to be included.

By including the modules in contrib/ the charm will dynamically load *any*
module it can find in that path. This dependency injection overrides behavior
of the charm, and allows the charm to adopt many permutations of deployment.
Supporting many domain providers can be as simple as deploying the DNS charm to
a LXC container on the bootstrap node, and relating your requisit services to
the appropriate DNS charm.

### Integrate DNS with your charm today

To add DNS support to your charm, simply impelment the interface `dns` for a
single record per service, or if you require multiple-records per service
`dns-multi`.

The actual service data you send will be either a JSON object, or an array of
JSON objects, depending, and will look similar to the following:

    {'alias': 'test', 'ttl': 1600, 'rr': 'A', 'addr': '127.0.0.1'}

The DNS charm will handle proxying the data to the provider and your dns will
remain updated so long as the DNS charm is managing your service(s).


## This feature is still beta!

The entirety of the DNS charm is still considered beta quality, and should not
be used in production setup's as of yet. All bugs that are found should be filed
[here](https://github.com/chuckbutler/DNS-Charm/issues)

If you have any feedback, wants, requests, etc. now is a great time to join the
conversation and help set the roadmap for the future of this charm!

Deploy Happy!





