from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
    """根据指定的国家或地区，返回Pygal使用的两个字母的国别码"""
    for code,name in COUNTRIES.items():
        if name == country_name:
            return code
    return None