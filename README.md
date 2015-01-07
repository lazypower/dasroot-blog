# My Blog

Allo, this is my blog. There are many like it, but this one is mine.


#### Pulling the source

Simply clone the repository

    https://github.com/chuckbutler/blog.git

Initialize the theme submodule(S)

    git submodule update --all

Install any python dependencies:

    make virtualenv

#### Submit a Guest article

Create a new post in `content/yy-mm-dd-title`

You will need to set the required meta-data in the post markdown:

    Title: Pondering on Devops and Security
    Date: 2015-01-05 13:30
    Tags: security, infosec, metasploit, docker, devops, planet
    Category: devops
    Status: draft
    Author: <Your Name>
    AuthorBio: <Your Short Bio>

Notice the three fields that will be especially pertient to you:

 - Author
 - AuthorBio
 - Status: draft

This allows you to set up your own information on the blog post giving you credit for your work. Additionally if you would like to have a photo embedded, ensure you place an image in `content/images/first_last.jpg` that is appropriately sized. See the existing image in the images directory for guidelines.

When I have reviewed the content, I will approve the post and remove the draft status. This allows you to see the content while you are developing, without being concerned that a merge will show an in-progress publication. You can view your work in a phaux live-update fashion by running:

    make devserver

Follow the typical [Fork & Pull](https://help.github.com/articles/using-pull-requests/) development workflow.

