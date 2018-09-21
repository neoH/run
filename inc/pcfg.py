#! /usr/bin/env python3

"""
---------------------------------------------------------------------------------------------
# File    : pcfg.py
# Author  : Neo.H
# Date    : Sep 14, 2018
# Version : v1.00
---------------------------------------------------------------------------------------------
This file store classes that can process all configures, containing program cfg and project
cfg
---------------------------------------------------------------------------------------------

"""

class proj_cfg: ## {
	"""
	The project configure process class, storing and processing the project configures.
	"""

	__cfg = None;


	def __init__(self,cfg): ## {
	## }

## }


class prog_cfg: ## {
	## the option description dict.
	__opts_desc = {};

	## the example usage description, it is a list for using.
	__usgs = [];


	## the dict stores all supported options and their features.
	## the format of this var is:
	## {'name'}: <name>_opt_dict_handler.
	## TODO
	__sopts = {};


	## the func. to add an support option to option list
	def __add_opt(self, name, desc): ## {
	## }


	## func. to describe one option according to the specified option name.
	def opt_desc(self, name): ## {
	## }

## }



class fgen_cfg(prog_cfg): ## {



	def __init__(self): ## {
		## initialize the fgen tool information.
		self.__opts_desc['-eda'] =
	## }



## }
