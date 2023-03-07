# Students by default have admin permissions to their own repositories
# when they create the org repository
# this goes through all the "2022-23-w2-midterm" repos
# removes all the non admin users
# re-adds them back with "pull" permissions (aka read permissions)
# this prevents any more changes to the repository after the exam

import os

import github3
from github3 import login
import pandas as pd

github3.__version__

org = "DSCI-310"
orgname = org
team = 'students-2022-23-w2'
team_name = team

admins = ["chendaniely", "ttimbers", "a-kong", "tonyliang19", "gzzen"]

token = "XXXXXX"

# log in
self = login(token=token)


self.org = self.organization(orgname)

org_repos = list(self.org.repositories())
org_repos

org_repos_df = pd.DataFrame({
  "short_repo": org_repos
})

org_repos_df["name"] = [sr.name for sr in org_repos_df["short_repo"]]
org_repos_df.head()

midterm_df = org_repos_df.loc[org_repos_df.name.str.match(pat="2022-23-w2-midterm")].reset_index(drop=True)
midterm_df.shape

midterm_df["student_portion"] = midterm_df["name"].str.replace("2022-23-w2-midterm-", "")
midterm_df

# remove all non admins from the repository
# add them back with "pull" permission which is "read" in the github web interface

for repo in midterm_df["short_repo"]:
  print(type(repo))
  print(repo)

  # all collaborators including admins
  collaborators = [c.__str__() for c in list(repo.collaborators())]
  print(collaborators)
  assert len(collaborators) == 5

  # just get the student collaborators
  student_collaborator_list= list(set(collaborators) - set(admins))
  assert len(student_collaborator_list) == 1

  student_collaborator = student_collaborator_list[0]
  print(student_collaborator)

  repo.remove_collaborator(student_collaborator)
  repo.add_collaborator(username=student_collaborator, permission="pull")
