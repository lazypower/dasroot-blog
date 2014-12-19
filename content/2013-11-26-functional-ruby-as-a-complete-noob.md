Title: Functional Ruby as a complete noob
Date: 2013-11-26 20:11
Tags: ruby, pdf, markdown
Slug: functional-ruby-as-a-complete-noob
---
Just for fun, I wanted the ability to hack up a quick document in markdown, which seems to be my new flavor of choice for writing practically anything from notes to full blown documentation sets. Problem being, not everybody or everything can read markdown. 

### Scenario: ###
I'm writing a tech spec for a service at work. Its really easy to whip up a document complete with code samples in markdown. 

### Problem: ###
It doesn't look professional AT ALL to distribute a markdown file as documentation. That and most of the business guys in windows land haven't even HEARD of markdown. 

### Solution: ###
Use ruby to convert the markdown to pretty HTML, then pipe that HTML into a PDF creation library to spit out a PDF of the documentation. 


I've only been dabbling in ruby for a few days. I took some TDD lessons using RSpec from my good friend [Jesse](http://www.jessedearing.com) so this small script seemed like a great starting point to apply what I have learned. 

{% gist 2347985 %}

Using the gemset RedCarpet (thanks GitHub!) and PDFKit, this was 13 lines of ruby goodness. 

_Example Usage_
```
ruby generator.rb /path/to/file.markdown /path/to/optional/css_for_pretty_html.css
```
