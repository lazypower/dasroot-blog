Title: Fail2Ban Blacklisting
Date: 2013-12-05 14:12
Tags: firewall, admin-post, fail2ban
Slug: fail2ban-blacklisting
Category: Devops

Fail2Ban is a great daemon that monitors log files and bans offending IP when under a brute force attack.

> This information is woefully out of date. You should probably be referencing a better tutorial such as the tutorial provided by [Digital Ocean](  https://www.digitalocean.com/community/tutorials/how-to-install-and-use-fail2ban-on-ubuntu-14-04)

Let’s say that you don’t want to apply a permanent ban as the default rule (because it is possibile, setting the bantime at -1 in the relative filter of the jail.conf file). However there is a host that keeps showing up and you're positive its bot related and should not be allowed a "cooldown" period before resuming the attack.

To permanently ban an IP add the following line under the “actionstart” rule (the actions used when fail2ban starts/restarts):

```
cat /etc/fail2ban/ip.blacklist | while read IP; do iptables -I fail2ban- 1 -s $IP -j DROP; done
```

in the configuration file used as default ban action. For example, if your default ban action is “iptables-multiport” (the default rule) you need to add the previous line to the configuration file:

```
/etc/fail2ban/action.d/iptables-multiport.conf
```

After that, you need to manually add the offending IP, one IP per line, to the file /etc/fail2ban/ip.blacklist
