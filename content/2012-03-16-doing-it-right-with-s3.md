Title: Doing it right with S3
Date: 2012-03-16 19:23
Tags: AWS, Cloud, Saving Cheddar, Jorge did it
Slug: doing-it-right-with-s3
Category: Web

> **Update 2014** Since this article, I've moved to Ghost => Pellican. Static site generation just seems to do the job better for me. And having a Python solution makes it easier for *me* to extend. YMMV

As some of you know, I'm an avid follower of the brilliant people at [Ask Ubuntu](http://www.askubuntu.com) and [Jorge Castro](http://www.jorgecastro.org) had an extremely excellent idea of hosting his [Octopress](http://www.octopress.org) blog out of AWS S3. This got me thinking - I'm paying upwards of $60 USD a month for hosting through Linode, and since I cut the Wordpress habit next to none of my projects require server side includes, so this was literally money down the chute.

Hosting my static sites, for example the vcard you see at the footer of my blog, would be an excellent place to start. Move this puppy over to S3, pilot the difficulty rating of just how hard it is and move forward with an execution of the rest of my pages. (Also, we can thank the fine people over at [GitHub](http://www.github.com) for powering this blog instance.)

![Challenge Accepted](/images/2012/March/challenge_accepted.png)

Since I have nearly no experience in working with AWS from a linux box, this was one of those moments where I knew it was time to tug on my bootstraps and learn something new.

My first task was to figure out just how I was going to interface with an S3 bucket on Ubuntu. A quick google search yielded s3cmd. This command line tool affords you loads of flexibility, and you guessed it, I can script an entire site deployment with this handy utility. Why thank you CLI programmers of the universe. You give me warm and fuzzy feelings all over.




####Great, I have the technology, now what?

If you dont currently have an AWS account you'll need to sign up for one.

Import your S3 Credentials into s3cmd as follows

    s3cmd --configure

s3cmd will prompt you for your AWS public and private keys. Ask about SSL encryption for data transfer settings and boom you're ready to start using s3cmd.

    s3cmd mb s3://<yourbucketname>

This will create your s3 bucket, basically just alotting a bin for you to start placing files. With the bucket created, you should enable serving of web-content from the bin - set the index document, and if you have an error page the optional error html. (this removes the AWS XML error page you'll get when users 404 your site structure)

I did that bit in the AWS management console itself - as depicted below.

![AWS S3 Console](/images/2012/March/s3_console.png)

With this step completed, you're free to upload your files. - One caveat that I discovered was if you dont implicitly define public Access, aws defaults to private ACL's. Read more on AWS S3 Access Control List (ACLs) [here](http://aws.amazon.com/articles/5050)

When pushing files to your S3 bucket, you can define the acl inline like so

    s3cmd put --acl-public --recursive <directory> s3://<yourbucketname>

Hopefully with this short introduction, you have a good enough overview to start moving your flat files into S3. With some light reading, 20 minutes, and a new resolve to not be wasteful, we can all put money back in our pockets and save on energy costs by utilizing datacenters around the globe efficiently.
