#!/bin/env python
from bs4 import BeautifulSoup

import sys
import json

def makers_block(tag):
    return (tag.name == 'div') and tag.has_attr('id') and tag['id'] == "review-body"


def devicenames(tag):
    return (tag.name == 'span') and tag.has_attr('class') and ('devicename' in tag['class'])

with open(sys.argv[1]) as f:
    soup=BeautifulSoup(f, 'html.parser')

makers=soup.find(makers_block)
# print(makers)
devices_ul=makers.find('ul')
devices=[]
# print(devices_ul)
for device_li in devices_ul.find_all('li'):
    # print(device_li)
    img_tag=device_li.find('img')
    description=img_tag['title']
    a_tag=device_li.find('a')
    span_tag=a_tag.find('span')
    device_name=span_tag.text
    manufacturer=span_tag.contents[0]
    model=" ".join(span_tag.contents[2:])
    devices.append({'manufacturer': manufacturer, 'model': model, 'name': device_name, 'description': description})

print(json.dumps(devices))