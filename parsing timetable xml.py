import os
import pandas as pd
from collections import OrderedDict
from datetime import date


import xml.etree.ElementTree as et
tree= et.parse("k.xml")
root= tree.getroot()

q=[]
for child in root:
  for element in child:
    q.append(element.tag)
#print(q)
r=list(set(q))
print (r)
#print(pd.DataFrame(r))
print("\n")
print("\n")
def extract(tags):
  for i in tags:
  
    dd=[]
    for elem in tree.iter(tag=i):
      b=elem.attrib
      dd.append(b)
    df_dd = pd.DataFrame(dd)

    print(i)
    print(df_dd)
    print("\n")
    print("\n")
extract(r)


def find(mnode, node, att, value):
  w=[]
  test = tree.find(mnode)
  for info in test.findall(node):
      if info.get(att) == value:
        q=info.attrib
        w.append(q)
  df=pd.DataFrame(w)
  print(df)

p= input("enter main child node :")
q= input("enter sub child node :")
r= input("enter attribute :")
s= input("enter value :")
find(p,q,r,s)
