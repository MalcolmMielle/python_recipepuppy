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
lst.append('milk') 
lst.append('cottage cheese')
lst.append('broccoli') 
lst.append('cheddar') 
lst.append('cheese')
lst.append('basil')
lst.append('onion powder')
lst.append('eggs')
lst.append('garlic powder')
lst.append('roma tomato')
lst.append('salt')

print reso["results"][0]["ingredients"]
title=get_recipe(reso["results"][0]["ingredients"])
print title
print 'V2'
print get_recipe(lst)
print get_ingredients(title)
print get_link(title)