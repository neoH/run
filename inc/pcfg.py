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
	"""
	The program configure class. it is a base class used to store program configurations.
	And this class will provide several APIs for all extending classes.
	"""

	## the example usage description, it is a list for using.
	__usgs = [];

	##

	## the dict stores all supported options and their features.
	## the format of this var is:
	## {'name'}: <name>_opt_dict_handler.
	## *_opt_dict format:
	## {'param'}: the parameter of this option
	## {'fmt'}: format of the option, valid in string type: '-', '++', '+='
	## {'desc'}: description, for display and examples.
	__sopts = {};

	## the func. to add an support option to option list
	def __add_opt(self, name, fmt, desc, param = None): ## {
		opt = {
			'param': param,
			'fmt' : fmt,
			'desc': desc
		};
		self.__sopts[name] = opt;
	## }


	## func. to describe one option according to the specified option name.
	def opt_desc(self, name):
		"""
		A func. to display help information. All display format are the same.
		"""
		opt_info = '';
		self.__ver_display__(); ## a internal func. that should be overridden by derived class.
		opts = self.__sopts.keys(); ## get the keys for options, the key is option name.
		for opt in opts:
			opt_info = opt['fmt']+opt;
			if opt['param']: opt_info = opt_info+' <'+opt['param']+'>'; ## if parameter exists, then need to print parameter information.
			opt_info = opt_info+': '+opt['desc']; ## add the semicolon and description.
		return;
	## }

	def __ver_display__(self): ## {
		return;
	## }


## }


class fgen_cfg(prog_cfg): ## {
	"""
	It is a class derived from prog_cfg used by the program run-fgen
	"""

	def __init__(self): ## {
		## initialize the fgen tool information.
		self.__add_opt('eda','-','specify the eda tool, for now, valid only for VCS tool, and interfaces \
		will be retained for other eda tools.','edatool');

		self.__add_opt('help','-','help option to display all valid options for fgen tool.');

		self.__add_opt('rtl','-','specify the rtl type to lead the tool to generate the different combination \
		of compile.lis. Default rtl_type is \'asic\'.','rtl_type');

		self.__add_opt('path','-','specify the path to generate the filelist, this is an optional param, if \
		not specified, the default path: <proj_home>/out/sim/<rtl_type>/tests/ will be used.','dest_path');

		self.__add_opt('proj_home','-','the project home specified by caller.','path');

		self.__add_opt('erf','-','external rtl file, this means the file should be added to rtl.lis, with \
		different rtl mode, the erf can specify corresponding rtl modules.','file_name');

		self.__add_opt('y','-','to specify the library path, by different eda tools, this option will be \
		translated to the corresponding options recognized by the tool. Besides, this option only \
		support the eda tool that can support filelist option insertion.','library');

		self.__add_opt('libext','-','this option work together with -y option, to specify the searching \
		file with specified extension. This option can be input with multiple times for specifying \
		multiple extensions.','extensions');

		self.__add_opt('target','-','the option specify the destined usage for calling this tool. the \
		target name for now are valid within: \
		\n -- sim: for simulation, in this target, the compile.lis, rtl.lis, dpi.lis, fsim.lis and \
		sim_model.lis will be generated nomatter files above exists or not. \
		\n -- wav: for wave vision, in this target, wave.lis, rtl.lis, fsim.lis and sim_model.lis will \
		be generated nomatter files above exists or not.','target_name');

		self.__add_opt('pt','-','the project type option, valid only within IP and SOC.','proj_type');

		return; ## return void.
	## }

## }
