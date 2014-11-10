#!/usr/bin/env python2
# -*- coding: utf-8-*-


import requests
from recipepuppy import *

reso=query('omelet','')

print reso["results"][0]["title"]
print reso["results"][0]["ingredients"]
print reso["results"][1]["title"]
print reso["results"][1]["ingredients"]

print get_ingredients(reso["results"][0]["title"])
title=get_recipe(reso["results"][0]["ingredients"])
print title
print get_ingredients(title)
print get_link(title)