Title: GPG Made a comeback in my workflow
Date: 2015-03-15 00:46
Tags: cryptography, GPG, infographic, planet
Slug: 2015-gpg-made-a-comeback-in-my-workflow
Category: misc
Status: published
Image: /images/2015/march/cryptography-is-not-a-crime.png 

GPG (Gnu Privacy Guard) is a piece of software that can basically do two things:

- encrypt/decrypt every kind of data so that only you or the persons you choose are able to read/use it.
- sign/verify data so that you can be sure that the data originates from the person you think it originates from.

[Link to the official GPG project](http://www.gnupg.org/)

## Why use it?

Whether or not you want to use encryption is of course up to you. Something that many people don't seem to keep in mind is that E-mail is not confidential in *any way*. It's as if you were writing on postcards, not even using an envelope. Everyone who happens to handle the e-mail or access the account on the server can read the entire mail without you noticing. If you want any modicum of privacy in your email, tweets, documents, chats - you should defininately consider it. I encrypt my mail traffic and have started signing my mails so recipients have it on good faith that the email has originated from me.

Should they want to send me something in private, the fact I'm signing these e-mails with my public key affords them the opportunity to do so. It's a win/win - you know it's me, and you can talk to me in secret if you have some account credentials to mail over (for example).

## Keybase.io

I really have to applaud the efforts of [keybase.io](http://keybase.io), trying to make security through GPG a popular item again. I've recently seen the volume of PGP verified mail subside as we move to a more mobile web. Abandoning cryptography in the wake of convenience of swiping communications off screen, and not really caring who the originator was. We take full faith from the `From:` line assuming our *Big Provider* has done their due dilligence in keeping out the riff raff.

Keybase makes it easier for cryptography noobies to get started, by giving them a Browser based implementation of OpenPGP. There are some concerns there by security experts - as there should be. But there's nothing stopping you from using normal GPG with the service - and uploading only your public key to Keybase.

In Addendum, they also offer a public verification service - where you can sign messages with your GPG key and have them verified in keybase - to identify that you are who you say you are across some of the most popular online networks.

Pretty cool!

## Remembering GPG

I'm not one for digging through manpages every time I forget something. Call me strange - but I really like the format of an infographic, or a cheat sheet. So that's exactly what I did. Enjoy! It's released under a  Creative Commons By-SA license. Feel free to fork, modify, and re-distribute. Together we can put the "not a crime" back in "Cryptography is not a crime!"

![GPG Cheat Sheet](/images/2015/march/gpg-cheat-sheet.png)

### [Download the SVG](/images/2015/march/gpg-cheat-sheet.svg.zip)
