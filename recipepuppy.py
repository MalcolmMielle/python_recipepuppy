#!/usr/bin/env python2
# -*- coding: utf-8-*-

import requests

#query
def query(name=None, ingredient=None, page=None):
	p=PuppyRecipe()
	return p.query(name, ingredient, page).json()

class PuppyRecipe(object):
	def __init__(self):
		self._url = "http://www.recipepuppy.com/api/?"
		self.ingredient=''
		self.page=''
		self.name=''
		
	@property
	def url(self):
		pass
	
	#Global search
	def search(self, post_data_dictionary):
		try:
			r = requests.get(self._url, params=post_data_dictionary)
			return r
		except URLError, exception_variable:
			#prints the reason for failure out to help debugging
			print'Error'
			print exception_variable.reason
		except HTTPLError, exception_variable:
			#prints the HTTP error code that was given
			print'Error'
			print exception_variable.code
		except ConnectionError, exception_variable:
			print'Error'
			print exception_variable.code
		except  Timeout, exception_variable:
			print exception_variable.code
		except TooManyRedirects, exception_variable:
			print exception_variable.code
		return None
	
	#query
	def query(self, name=None, ingredient=None, page=None):
		if name is None:
			self.name=''
		else:
			self.name=name
			
		if ingredient is None:
			self.ingredient=''
		else:
			self.ingredient=ingredient
			
		if page is None:
			self.page=''
		else:
			self.page=page

		return self.search({'i':self.ingredient, "q":self.name, "p":self.page})