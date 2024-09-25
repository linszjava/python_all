import json

from pyecharts import options as opts
from pyecharts.charts import Graph


with open("test.json", "r", encoding="utf-8") as f:
    j = json.load(f)
    nodes = j["nodes"]
    links = j["links"]
    categories = j["categories"]

c = (
    Graph(init_opts=opts.InitOpts(width="1000px", height="600px"))
    .add(
        "",
        nodes=nodes,
        links=links,
        categories=categories,
        layout="circular",
        is_rotate_label=True,
        linestyle_opts=opts.LineStyleOpts(color="source", curve=0.3),
        label_opts=opts.LabelOpts(position="right",is_show=True), # 默认不显示节点名称，设置为显示
    )
    #提示框配置项显示节点的name属性 节点的关系属性
    .set_global_opts(
        title_opts=opts.TitleOpts(title="人物关系图测试"),
        legend_opts=opts.LegendOpts(orient="vertical", pos_left="2%", pos_top="20%"),
        #提示框配置项显示节点A到节点B的关系属性
        tooltip_opts=opts.TooltipOpts(formatter="{b}:{c}"),
    )
    .render("test.html")
)
