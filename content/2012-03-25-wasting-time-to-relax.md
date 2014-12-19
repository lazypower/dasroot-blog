Title: Wasting time to relax
Date: 2012-03-25 22:48
Tags: saving-cheddar, gaming, mono, open-source, post
Slug: wasting-time-to-relax
Category: Misc

This weekend I tasked myself with "not working so hard". After having spent so much time at the grind I was ready for something fresh. The excitement of developing for fun has worn thin. I wasn't about to reach for the familiar MMO's. Those are literally a timesink I have to battle myself away from every time I get started. Starcraft has gone to the hardcore players, and Diablo3 isn't here yet. What do I do?

  I hit my usual sources in Google Reader for gaming news, and ran across a gem. [Terraria](http://www.terraria.org) is an indie game published on steam for $10 USD. Its recipe is simple. Dig up materials, craft awesomeness, unlock NPC's, fight bad guys. You can play it at your own pace - it has some solid Multiplayer support (I'm running my own dedicated server at this point I'm so addicted already). Did I mention its addictive?

  You don't have to take my word for it. Check out the official gameplay trailer.

  <iframe width="420" height="315" src="http://www.youtube.com/embed/w7uOhFTrrq0" frameborder="0" allowfullscreen></iframe>


  If you want to setup your own linux dedicated server, read on!
  <!-- more -->

  First and foremost, let me warn you. Mono is a hog - if you think you'll get away with running this on a bare-bones server, you might as well play on a public Terraria server or host it off your gaming rig. ~~Dedicated servers are goign to require at BARE MINIMUM 1 gig of ram to run well. Mono will crash out with any less than this.~~ _note_ I've since discovered that when you use the TShock packaged bin without all of the debug hooks, you *can* run a dedicated server on an AWS micro instance - ~ 625 megs of ram. I have a server cap of 8 players and only use a medium sized world. World generation will take circa 10 minutes with this configuration - YMMV.

  Assuming you're using Ubuntu 11.10 - just run the following commands: (if you're running a 10.04 or prior you will need to compile mono from source)

  ` sudo apt-get install mono-complete`

  this takes about 5 minutes to fetch and install an on AWS Small instance

  Once you have completed this step - grab the TShock server binaries. TShock is a repack of the official Terraria server that comes with administration modifications, and thuse ease the setup process.

[TShock Github Project Page](https://github.com/TShock/TShock/downloads)

  `wget https://github.com/TShock/TShock/tarball/master
   tar xvfz master
   cd TShock-TShock-ed6b95c && screen mono TerrariaServerBinaries\TerrariaServer.exe `

   _NEW!_ OR use this handy dandy script
{% gist 2332154 %}


   at this point you will need to create and name your new world, assign it a port, and setup is complete!
