#!/usr/bin/env python2
# -*- coding: utf-8-*-

import requests
import urllib2
import urllib

	
#Global search
def query(name='', ingredient='', page='1'):
	try:
		r = requests.get("http://www.recipepuppy.com/api/?", params={'i':ingredient, "q":name, "p":page}).json()
		return r
	except urllib2.URLError, exception_variable:
		#prints the reason for failure out to help debugging
		print'Error'
		print exception_variable.reason
	except requests.exceptions.HTTPError, exception_variable:
		#prints the HTTP error code that was given
		print'Error'
		print exception_variable.code
	except requests.exceptions.ConnectionError, exception_variable:
		print'Error'
		print exception_variable.code
	except requests.exceptions.Timeout, exception_variable:
		print exception_variable.code
	except requests.exceptions.TooManyRedirects, exception_variable:
		print exception_variable.code
	return None

#get only ingredients
def get_ingredients(name):
	results=query(name=name)
	return results["results"][0]["ingredients"]

def get_recipe(ingredient):
	results=query(name='',ingredient=ingredient)
	return results["results"][0]["title"]

def get_link(name):
	results=query(name)
	return results["results"][0]["href"]