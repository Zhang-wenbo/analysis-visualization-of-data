import pygal

wm = pygal.maps.world.World()
wm.title = "在世界地图上呈现数字数据"
wm.add("北美",{'ca':34126000, 'us': 309349000, 'mx': 113423000})#传入字典

wm.render_to_file('在世界地图上呈现南美数字数据.svg')