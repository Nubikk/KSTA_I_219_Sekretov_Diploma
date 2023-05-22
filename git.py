import git

repo_url = 'https://github.com/user/repo.git'
repo_dir = '/path/to/repo'

git.Git().clone(repo_url, repo_dir)
