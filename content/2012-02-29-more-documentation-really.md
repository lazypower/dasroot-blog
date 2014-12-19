Title: More Documentation? Really?
Date: 2012-02-29 00:19
Tags: resolve, improving-weakness, being-technical
Slug: more-documentation-really
Category: Programming

Documentation, it's that often forgotten about portion of every developers existence that we either loathe, or embrace and do really intelligently. I have more people joining me in my efforts, looking over what I'm doing every day that have questions about the software that we write. This leaves me often times thinking "I really wish I had written at very least an overview of what this does..." Then, when I revisit things I see that I didnt comment my code well enough to give a layman an overview of what I'm doing. (To be completely honest, I've scolded myself in private for leaving just enough comments that even I as the author of the class/method/whatever has to really think about what the code is doing.) I'm stellar at giving the just enough info to make you angry that you bothered to look kind of developer. Yikes!

<!--more-->

The entire time I was going through school I was cutting corners and dropping comments from boiler plate code. Stripping every ounce of text that I didn't have to copy by hand. Looking back at this habbit; it's clearly carried over into my professional life. This is frustrating to say the least, to look back over the 200 thousand + lines I've written in just the last year alone. How many of those 200k lines should have been prefixed with //? Just yesterday I would have said "maybe 10%?" Now i'm more inclined to beleive it should be 50%.

The developers following me will start thanking me after I've gone through and re-commented my steps. And I think I'll gain a pat on the back from myself for doing it. But why should the buck stop there? That solves a very small portion of the problem. What about the non-technical people that dont look at the code on a daily basis and want to use a portion of my system? Right now they can't unless they ask me a million questions and expect me to sum up a usage guide in 2 paragraphs or less without being least bit technical, or they are tuning me out and moving on in true TL;DR fashion.

Enter Markdown and Github Wiki's. I'm toying with the idea of the following workflow

The great idea of workflow
---

1. Adopt the habbit of signing EVERY method with an autodoc compatible signature
2. Generate API reports with every milestone
3. Parse said XML api documents - and translate into markdown
4. Embed markdown pages in Github Wiki - with an properly indexed list of sub-pages with per-class documentation
5. Spend 20 minutes a day at the end of my shift and document changes in the changelog
6. Stop depending on git history for *everything*

Here's to hoping this helps.
