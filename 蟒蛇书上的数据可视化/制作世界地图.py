import pygal

wm = pygal.maps.world.World()
wm.title = "中美，北美，南美地图"
wm.add('北美', ['ca', 'mx', 'us'])
wm.add('中美', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('南美', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])
wm.render_to_file('美洲.svg')
