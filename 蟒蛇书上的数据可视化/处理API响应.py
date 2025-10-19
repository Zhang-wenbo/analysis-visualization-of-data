#执行API调用，找到GitHub上星级最高的python项目
import requests

#执行API调用并存储响应
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("状态代码:",r.status_code)

#将API响应存储在一个变量中
response_dict = r.json()#response响应字典
print("存储库总数:",response_dict['total_count'])

#探索有关仓库的信息
"""
与items相关的是一个列表，里面包含许多字典，每一个字典都存储着一个python库的信息
"""
repo_dicts = response_dict['items']
print("返回的仓库数:",len(repo_dicts))

#研究第一个仓库
repo_dict = repo_dicts[0]

print("\n有关第一个存储库的选定信息：")
for repo_dict in repo_dicts:
    print('名字：',repo_dict['name'])
    print('所有者：',repo_dict['owner']['login'])#访问所有者的登陆名
    print('星级：',repo_dict['stargazers_count'])
    print('储存库：',repo_dict['html_url'])
    print('描述：',repo_dict['description'])