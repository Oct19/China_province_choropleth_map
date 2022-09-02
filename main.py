import pandas as pd  #pandas Is a powerful data processing library
from pyecharts.charts import Map
from pyecharts import options as opts

# import data
data = pd.read_excel('data/1052_province_data.xlsx')
province = list(data["省份"])
data_num = list(data["样本数"])
list = [list(z) for z in zip(province,data_num)]

# print(list)

c = (
    Map(init_opts=opts.InitOpts(width="1000px", height="600px")) #Switchable theme
    .set_global_opts(
        title_opts=opts.TitleOpts(title="俊俊调查问卷各省份数量"),
        visualmap_opts=opts.VisualMapOpts(
            min_=0,
            max_=175,
            range_text = ['样本数量:', ''],  #Interzone
            is_piecewise=True,  #Define legend as segmented type, default to continuous legend
            pos_top= "middle",  #Segment location
            pos_left="left",
            orient="vertical",
            split_number=5  #Divided into 10 sections
        )
    )
    .add("爱你",list,maptype="china")
    .render("Map2.html")
)