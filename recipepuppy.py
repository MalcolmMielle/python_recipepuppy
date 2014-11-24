#!/usr/bin/env python2
# -*- coding: utf-8-*-

import requests
import urllib2
import urllib
import string
import re

class Recipe(object):
	def __init__(self, dict_in):
		self.data=dict_in

def clean():
    """Contrôle le temps mis par une fonction pour s'exécuter.
    Si le temps d'exécution est supérieur à nb_secs, on affiche une alerte"""
    
    def decorateur(fonction_a_executer):
        """Notre décorateur. C'est lui qui est appelé directement LORS
        DE LA DEFINITION de notre fonction (fonction_a_executer)"""
        
        def fonction_modifiee(name):
            """Fonction renvoyée par notre décorateur. Elle se charge
            de calculer le temps mis par la fonction à s'exécuter"""
            
            return fonction_a_executer(name).strip() # On exécute la fonction
        return fonction_modifiee
    return decorateur
	
#Global search
def query(name='', ingredient='', page='1'):
	#Handling lists
	if isinstance(ingredient, list):
		li=iter(ingredient)
		obj=next(li)
		ingredient_fin=str(obj)+', '
		while True:
			try:
				ingredient_fin=ingredient_fin+str(obj)+', '
				obj=next(li)
			except StopIteration:
				 ingredient_fin=ingredient_fin+str(obj)
				 break
	else :
		ingredient_fin=ingredient
	try:
		r = requests.get("http://www.recipepuppy.com/api/?", params={'i':ingredient_fin, "q":name, "p":page}).json()
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

@clean()
def get_clean_ingredient(name):
	results=get_ingredients(name)
	
@clean()
def get_clean_recipe(name):
	return get_recipe(name)

#Make it a dictionnary
def get_full_info(name='', ingredient='', page='1'):
	results=query(name,ingredient, page)
	#Need to create a dict with all info
	all=dict()
	i=0
	while i<len(results['results']):
		all[results['results'][i]['title']]=results['results'][i]['ingredients']
		#all[results['results'][i]['title']].append(results['results'][i]['href'])
		i=i+1
	return Recipe(all)

	

"""Pour gérer le temps, on importe le module time
On va utiliser surtout la fonction time() de ce module qui renvoie le nombre
de secondes écoulées depuis le premier janvier 1970 (habituellement).
On va s'en servir pour calculer le temps mis par notre fonction pour
s'exécuter"""

