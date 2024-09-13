# 定义公用的 data 数据 以备调用
def get_all_data():
    import pandas as pd

    sales = {
        '季度': ['第一季度', '第一季度', '第一季度', '第二季度', '第二季度', '第二季度'],
        '区域': ['华东', '华北', '华南', '华东', '华北', '华南'],
        '长泰店': [90, 92, 88, 94, 92, 87],
        '人民店': [91, 85, 89, 92, 88, 82],
        '金寨店': [89, 98, 85, 82, 85, 95],
        '临泉店': [96, 90, 83, 85, 99, 80]
    }
    data = pd.DataFrame(sales)
    return data

def get_simple_data():
    import pandas as pd

    sale = {
        '长泰店': [90, 92, 88, 94, 92, 87],
        '人民店': [91, 85, 89, 92, 88, 82],
        '金寨店': [89, 98, 85, 82, 85, 95],
        '临泉店': [96, 90, 83, 85, 99, 80]
    }
    data = pd.DataFrame(sale)
    return data

def get_pure_data():

    sale = {
        '长泰店': [90, 92, 88, 94, 92, 87],
        '人民店': [91, 85, 89, 92, 88, 82],
        '金寨店': [89, 98, 85, 82, 85, 95],
        '临泉店': [96, 90, 83, 85, 99, 80]
    }
    return sale