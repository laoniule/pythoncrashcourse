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
import pygal
from pygal.Style import LightColorizedStyle as LCS, LightenStyle as LS




URL = "https://api.github.com/search/repositories?q=language:python&sort=stars"

r = requests.get(URL)
print("Status Code: ", r.status_code)

reponse_dict = r.json()
print(reponse_dict.keys())
print("Total Count: ", reponse_dict['total_count'])

repo_dicts = reponse_dict['items']
names,stars=[],[]
names.append(repo_dictsp['name'])
stars.append(repo_dictsp["Stargazers_count"])

my_style = LS('#333366',base_style=LCS)
chart=pygal.Bar(Style=my_style,x_label_rotation=45,show_legend=False)
chart.title='Most-Starred Python Projects on Github'
chart.x_labels=names
chart.add(",stars")
chart.render_to_file("python_repos.svg")


print("repositories returned: ", len(repo_dicts))

# 取出第一个repository的内容，打印这个repository中的所有条目的数量
# repo_dict=repo_dicts[0]
# print("\nkeys:",len(repo_dict))

# for key,value in repo_dict.items():
#     print("\nkey:",key)
#     print("\tvalue:",value)

# 研究第一个repository
# print("\nSelected information about first repository:")
# print("Name:",repo_dict['name'])
# print("Owner:",repo_dict['owner']['login'])
# print("Stars:",repo_dict['stargazers_count'])
# print("Repository:",repo_dict['html_url'])
# print("Created:",repo_dict['created_at'])
# print("Updated:",repo_dict['updated_at'])
# print("Description:",repo_dict['description'])


# 查看每个repository的信息
print("Selected information about each repository")
for repos_dict in repo_dicts:
    print("----------------------------------------------------")
    print("Name:", repos_dict['name'])
    print("Owner:", repos_dict['owner']['login'])
    print("Stars:", repos_dict['stargazers_count'])
    print("Repository:", repos_dict['html_url'])
    print("Created:", repos_dict['created_at'])
    print("Updated:", repos_dict['updated_at'])
    print("Description:", repos_dict['description'])
