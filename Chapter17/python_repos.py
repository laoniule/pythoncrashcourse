#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   python_repos.py
@Time    :   2019/09/25 10:26:27
@Author  :   Niu Xiaodong 
@Version :   1.0
@Contact :   xniu@msn.com
@License :   (C)Copyright 2017-2018
@Desc    :   None
'''

# here put the import lib

import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"

r = requests.get(url)
print("Status Code: " , r.status_code)

reponse_dict=r.json()
print(reponse_dict.keys())
print("Total Count: ", reponse_dict['total_count'])

repo_dicts=reponse_dict['items']
print("repositories returned: ", len(repo_dicts))

## 取出第一个repository的内容，打印这个repository中的所有条目的数量
# repo_dict=repo_dicts[0]
# print("\nkeys:",len(repo_dict))

# for key,value in repo_dict.items():
#     print("\nkey:",key)
#     print("\tvalue:",value)

## 研究第一个repository
# print("\nSelected information about first repository:")
# print("\nName:",repo_dict['name'])
# print("\nOwner:",repo_dict['owner']['login'])
# print("\nStars:",repo_dict['stargazers_count'])
# print("\nRepository:",repo_dict['html_url'])
# print("\nCreated:",repo_dict['created_at'])
# print("\nUpdated:",repo_dict['updated_at'])
# print("\nDescription:",repo_dict['description'])

print("----------------------------------------------------")
## 查看每个repository的信息
print("\nSelected information about each repository")
for repos_dict in repo_dicts:
    print("----------------------------------------------------")
    print("\nName:",repos_dict['name'])
    print("\nOwner:",repos_dict['owner']['login'])
    print("\nStars:",repos_dict['stargazers_count'])
    print("\nRepository:",repos_dict['html_url'])
    print("\nCreated:",repos_dict['created_at'])
    print("\nUpdated:",repos_dict['updated_at'])
    print("\nDescription:",repos_dict['description'])