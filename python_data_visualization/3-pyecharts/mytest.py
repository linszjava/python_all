import json
import ijson
from pyecharts.charts import Graph
from pyecharts import options as opts
import pandas as pd

# with open('hanyu.json', 'r', encoding='utf-8') as f:
#     items = ijson.items(f, 'Package.PersonAuthority.PersonInfo.Person.item')
#     for item in items:
#         per_social_ass_nodes = item['PersonSocialAssociation']
#         break
# print(per_social_ass_nodes)
# #选出per_social_ass_nodes中的所有AssocName
data = pd.read_json('hanyu.json',encoding='utf_8')
print(data)



