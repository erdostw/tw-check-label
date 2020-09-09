#!/usr/bin/env python3

import os
import re
import sys

from github import Github

valid_labels = set(['change:standard', 'change:impactful', 'change:emergency'])

repo_name = os.environ.get('GITHUB_REPOSITORY')
github_ref = os.environ.get('GITHUB_REF')

pr_number = int(re.search('refs/pull/([0-9]+)/merge', github_ref).group(1))

pr = Github(sys.argv[1]).get_repo(repo_name).get_pull(pr_number)

if (valid_labels & set(pr.get_labels())):
    exit(0)
else:
    exit(1)
