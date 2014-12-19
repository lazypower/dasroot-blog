Title: Helpful Juju Workflow One-Liners
Date: 2014-01-21 11:01
Tags: juju
Slug: helpful-juju-charming-one-liners
Category: Devops

While performing the great charm audit of 2014, I've encountered quite a few helpful charm commands that I didn't know existed. This won't be a comprehensive and exhaustive list of commands, but an aggregation of those I find the most helpful (consult the manpage/[docs](https://juju.ubuntu.com/docs/) if you require a full list).


###charm proof

 When initially looking at a charm, this runs a lint test against the charm. It will expose any issues from a syntax and presence standpoint against the following:

 - README
 - metadata.yaml
 - configuration.yaml

##### Example Output:

    $ charm proof
    W: Metadata is missing categories.
    W: No icon.svg file.
    W: config.yaml: option access-key does not have the keys: default
    W: config.yaml: option bucket-name does not have the keys: default
    W: config.yaml: option secret-key does not have the keys: default

###charm add readme

Generates the boilerplate README.ex - I use this for comparison against the existing README. (hat tip [@jorgecastro](http://jorgecastro.org)). This is extremely helpful as I often forget what's in the template, in terms of structure and examples. A side effect of this workflow is you are always checking against the latest README boilerplate updates.




###juju test -e $environment

Executes all found integration tests within `$CHARM_DIR/tests` in the given environment.



### lbox propose -cr -for lp:charms/$charm-name

Canonical uses the Rietveld tool during code reviews. This was an entirely new process change for me, as I'm used to [Gitlab](http://gitlab.org) or [GitHub](http://github.com) diff view for inline code reviews. The lbox utility is a go app, written to simplify the code review process, and provide developers a quicker access point to launchpad `Merge Proposals`.



Lbox is intelligent in design, the above command will do the following:

- Create a code branch under your user account: lp:~lazypower/charms/precise/mediawiki/tests  
- Create a `Merge Proposal` against lp:charms/mediawiki
- Push the diff to Rietveld tool

(Source: http://voices.canonical.com/tag/patch/)

Installing the lbox tool was fairly straight forward thanks in part to the nature of installing Go applications.

    go get launchpad.net/lbox
    go install launchpad.net/lbox

 You need to have the `go-golang` package installed, and have your `$GOROOT` and `$GOPATH` variables set accordingly. The installation procedure I encountered was in the `charm-tools` package in the `HACKING.txt` file.

##### Excerpt - HACKING.txt

    In order to submit code for review we use a tool called lbox. If you are using
    Ubuntu < 13.04 you can install lbox by::

    sudo apt-get install lbox

    If you are using a newer version you will have to build it from source. First
    step is to install Go lang, you can find the instructions on installing it
    here http://golang.org/doc/install#bsd_linux , making sure to set your GOROOT
    environment variable appropriately. After that, you should set up an install
    directory that you can access, such as $HOME/bin/go which you can set as your
    GOPATH directory (see `go help gopath` for more information). For ease of
    use, you can append $GOROOT/bin and $GOPATH/bin to your PATH environment
    variable. Then follow the instructions::

    sudo go get launchpad.net/lbox
    sudo go install launchpad.net/lbox

    To submit for review::

    lbox propose

    After review, to merge into trunk::

    lbox submit



## Code Snippets

    print(json.dump(d.schema(), indent=2))  

sometimes its handy to have the service schema printed out to the console during test execution for debugging purposes. This one liner prints the JSON schema of the deployment out during test execution.
