Title: SteamCMD and SteamGuard
Date: 2013-12-24 03:12
Tags: gaming, steam
Slug: steamcmd-and-steamguard
Category: Devops

SteamGuard is a multifactor authentication mechanism for Steam. If Steam does not have a record of the pc you are attempting to sign in with, it will halt the request and leave it in a "pending" state requiring you to enter a passcode they email to you.

This is awesome!

Now, enter SteamCMD who's sole purpose in life is to handle the "steam side" of server configuration. This is really a cool concept.

Let's take a look at using SteamCMD to provision the StarBound server

> **Editorial Note**: In leu of pasting tons of code into Ghost, I'll just point you at the github repository if you want code examples. [https://github.com/chuckbutler/starbound-charm](https://github.com/chuckbutler/starbound-charm)


SteamCMD offers a nice scriptable way to provision services through runscripts. Looking over the documentation at the Steam Dev Center, it looks extremely straight forward

### update_starbound.txt runscript
```
// update_starbound.txt
//
@ShutdownOnFailedCommand 1 //set to 0 if updating multiple servers at once
@NoPromptForPassword 1
login $STEAMNAME $STEAMPASS
force_install_dir ../starbound
app_update 211820 validate
quit
```

Everything is fairly straight forward, the only thing to note is you will have to know the Steam AppID, and can be found at the tail of the community page url.

![](/images/2013/Dec/Selection_011.png)

## NOTE

**If your account has SteamGuard enabled, it will halt your installation asking for the passcode. When attempting to script the value sent to me from SteamGuard, it drops into the Steam CLI and halts the script**

Well, that was crappy. Is it acceptable to ask my users to disable SteamGuard for their game server?
