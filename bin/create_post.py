#!/usr/bin/env python

import argparse
from datetime import datetime
from jinja2 import Template
import os
from subprocess import call
import sys


def create_post(title):

    template = Template("""Title: {{ title }}
Date: {{ date }}
Tags:
Slug:
Category:
Status: draft""")

    post_date = datetime.now().strftime('%Y-%m-%d')
    post_time = datetime.now().strftime('%H:%M')
    fulldate = "{} {}".format(post_date, post_time)
    escaped_title = title.replace(' ', '-')
    postname = "{}-{}.md".format(post_date, escaped_title)

    with open(os.path.join('content', postname), 'a+') as f:
        f.write(template.render({'title': title, 'date': fulldate}))
    EDITOR = os.environ.get('EDITOR', 'vim')

    call([EDITOR, "content/{}".format(postname)])


def main(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="Create a markdown template"
                                                 " and launch $EDITOR")
    parser.add_argument('title')

    args = parser.parse_args(args)
    create_post(args.title)

if __name__ == "__main__":
    main()
