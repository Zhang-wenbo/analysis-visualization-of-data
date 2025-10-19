import requests
from operator import itemgetter

# 获取顶级故事的ID
top_stories_url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(top_stories_url)
print("状态代码:", r.status_code)

# 取得前30个故事的ID
submission_ids = r.json()[:30]

# 存储每个提交的信息
submission_dicts = []
for submission_id in submission_ids:
    # 对于每篇文章，都执行一个API调用
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    submission_r = requests.get(url)
    print(submission_r.status_code)  # 打印状态码，判断是否请求成功
    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': f'http://news.ycombinator.com/item?id={submission_id}',
        'comments': response_dict.get('descendants', 0)  # 如果没有评论，则默认为0
    }
    submission_dicts.append(submission_dict)

# 按评论数量降序排序
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# 打印结果
for submission_dict in submission_dicts:
    print("\n题目：", submission_dict['title'])
    print("讨论链接：", submission_dict['link'])
    print("评论：", submission_dict['comments'])