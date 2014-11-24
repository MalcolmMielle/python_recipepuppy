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
print 'ingredient'
lst=list()
lst.append('Sour Cream') 
lst.append('Pasta')

print reso["results"][0]["ingredients"]
title=get_recipe(reso["results"][0]["ingredients"])
print title
print 'V2'
print get_recipe(lst)
print get_clean_recipe(lst)
print get_ingredients(title)
print get_link(title)