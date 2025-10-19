import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS#图表颜色设置

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)#创建一个柱状对象

chart.title = 'Python项目'
chart.x_labels = ['httpie', 'django', 'flask']

"""
Pygal根据与键'value'相关联的数字来确定条形的高度，并使用与'label'相关联的字符串给条形创建工具提示。
例如，一个字典将创建一个条形，用于表示一个获得了16101颗星、工具提示为Description of httpie的项目。
"""
plot_dicts = [
    {'value':16101,'label':'Description of httpie.'},
    {'value': 15028, 'label': 'Description of django.'},
    {'value': 14798, 'label': 'Description of flask.'},
]

chart.add('',plot_dicts)#向图表中添加数据和配置项,接收一个字符串和一个列表
chart.render_to_file('自定义工具提示的Python项目.svg')