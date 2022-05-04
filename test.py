#!/usr/bin/env python

import os

from github import Github
from github.GithubException import GithubException

github = Github(os.environ["GH_TOKEN"])
repo = github.get_repo(os.environ["GITHUB_REPOSITORY"])

# branches = [b.name for b in repo.get_branches()]
branches = list(repo.get_branches())
print(f"BRANCHES: {branches}")

# Merge merge-me into main
# repo.merge(base=branches[0], head=branches[1])
try:
    print("=================== BY NAME")
    repo.merge(base=branches[0].name, head=branches[1].name)
except GithubException as ge:
    print(ge)

try:
    print("=================== BY SHA")
    repo.merge(base=branches[0].name, head=branches[1].commit.sha)
except GithubException as ge:
    print(ge)
