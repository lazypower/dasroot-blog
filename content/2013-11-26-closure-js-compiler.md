Title: Closure JS Compiler
Date: 2013-11-26 20:11
Tags: untagged
Slug: closure-js-compiler
---

[Nathan Osman](https://plus.google.com/109692134350783862945) asked me a while back about what I knew of the [closure compiler](http://code.google.com/closure/compiler/). At that time, I had _no_ idea what I was missing. 

>The [Closure Compiler](http://code.google.com/closure/compiler/) is a tool for making JavaScript download and run faster. It is a true compiler for JavaScript. Instead of compiling from a source language to machine code, it compiles from JavaScript to better JavaScript. It parses your JavaScript, analyzes it, removes dead code and rewrites and minimizes what's left. It also checks syntax, variable references, and types, and warns about common JavaScript pitfalls.
><small>The official [closure compiler](http://code.google.com/closure/compiler/) page</small>

<!-- more -->

Sounds fairly interesting right? As a full time developer, I find myself writing deploy scripts, augmenting continuous build servers, and planning a ton of deployment automation. The [company](http://www.level-interactive.com) I work for has a TON of managed client sites. We extend their frameworks and augment the front-end elements on a daily basis - akin to the optimization services we offer. I found myself at the eventuality of needing to automate the minification and testing of our javascript. Enter my need for the closure compiler - as jslint and jsminify just wasnt enough. This needed to be light weight and always available - ding! plug it into a webservice.

While plotting how to do this - I discovered python was an excellent language for this. Instead of messing around with the powershell bits - a python script seems to carry less overhead and perform the same goal with less convoluted syntax. Google provides a default script that reads the script from stdin and prints out the compiled code - the following script is my first attempt at python and a simple modified version of googles own [compile.py](http://code.google.com/closure/compiler/docs/api-tutorial1.html)

I set out to write a script that I can use in our Continuous Integration server *powered by [jenkins](http://jenkins-ci.org/)* since it's already running our jsunit tests. Add a trigger for once a test-suite is complete and marks the library as good - run this little gem and auto-minify your javascript.

{% gist 1812994 %}

Since I bundled this up for our company deploy scripts - you can follow its evolution [here](https://github.com/University-Bound/UBound-Utility)