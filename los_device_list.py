#!/bin/env python
from bs4 import BeautifulSoup

import sys
import json


def vendor_block(tag):
    # return (tag.name == 'div') and tag.has_attr('class') and ('devices' in tag.attrs) and tag.has_attr('data-vendor')
    return (tag.name == 'div') and tag.has_attr('class') and tag.has_attr('data-vendor')

def device_block(tag):
    res=(tag.name == 'div') and tag.has_attr('class')
    if res:
        return 'name' in tag['class']
    return False

def devicenames(tag):
    return (tag.name == 'span') and tag.has_attr('class') and ('devicename' in tag['class'])

with open(sys.argv[1]) as f:
    soup=BeautifulSoup(f, 'html.parser')

devices=[]
for vendor_chunk in soup.find_all(vendor_block):
    # print("===> Vendor chunk")
    # print(vendor_chunk)
    vendor=vendor_chunk.attrs['data-vendor']
    for device_chunk in vendor_chunk.find_all(device_block):
        # print("===> Device chunk")
        # print(device_chunk)
        device_find=device_chunk.find(devicenames)
        if device_find:
            # device=device_find.contents
            device=device_find.text
            # print("{}: {}".format(vendor.capitalize(), device))
            devices.append({'manufacturer': vendor, 'model': device})
        # print(device_chunk)

print(json.dumps(devices))