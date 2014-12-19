Title: Breaking the Rubrik habit
Date: 2012-02-12 04:10
Tags: untagged
Slug: breaking-the-rubrik-habit
Category: Web


After setting up octopress it was brought to my attention that every geek from Singapore to LA has an octopress blog that sports the default theme. There was an excellent article that I seem to have misplaced. However the overall premise: "While your blog should focus on quality content, you have to have a desireable stage to present your information. " So I started looking into rapid frameworks for front end design.

<!-- more -->

The twitter bootstrap framework came to mind. I've wanted to try it for its clean looks vs using the 930 grid layout. It sports custom form elements, ready to rock javascript elements, and an extremely nice collection of style elements out of the box. Its officially one of the most impressive front end RAD frameworks I've used to date. The class tags are very clear cut and easy to work with.

It took about 30 minutes to gimp out the header image, and build out the template by hand. Bootstrap makes the markup so much cleaner than I'm used to. Looking at the semantic markup below - (or via view-source) You define your elements with a span# and you have sized grid-ready boxes. The kit comes with several modifier classes as well such as pull-right floats your content to the right of its parent container.  


The following was the machup I produced in about 30 minutes.

[gist:id=1807500]

To impelement this as your blog theme - you edit the _includes directory templates. Its all logically broken down into a parent calling object (next list):

  - _includes/head.html
  - _includes/header.html
  - _includes/navigation.html
  - _includes/footer.html

Octopress has a few parent display controllers listed in _layouts

  - category_index.html
  - default.html
  - page.html
  - post.html

Edit your templates and make sure the proper includes are being called in those layout controllers and you should be up and running in no time! What made this so easy is having built the machup first and then including the files in _include/header.html - snipping bits of style into the _include's as well. All in all - I'm very excited to be hacking away on this project.
