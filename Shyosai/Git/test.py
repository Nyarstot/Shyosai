from git import Repo

rp_1 = "C:/Users/winte/source/repos/Nyarstot/GitShyosaiTestRepo"
rp_2 = "C:/Users/winte/source/repos/Nyarstot/GitShyosai"
repo = Repo(rp_2)
repa = Repo(rp_1)

# print(repo.active_branch)
# print(repo.branches)

# print(repo.git_dir.title())
print(repo.git.execute('git status'))