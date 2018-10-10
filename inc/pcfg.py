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

from options import options;

class proj_cfg: ## {
	"""
	The project configure process class, storing and processing the project configures.
	"""

	__owner__ = 'Neo.H';

	__dbg__ = False; ## switch for debug print



	def __init__(self,dbg = False): ## {
	## }

## }


class prog_cfg: ## {
	"""
	The program configure class. it is a base class used to store program configurations.
	And this class will provide several APIs for all extending classes.
	"""

	__owner__ = 'Neo.H'; ## owner of this file

	__opt__ = None;

	def __init__(self,dbg = False): ## {
		self.__opt__ = options(dbg);
	## }

	def __ver_display__(self): ## {
		"""
		This func. should be overridden by extended classes.
		"""
		return;
	## }


## }


class fgen_cfg(prog_cfg): ## {
	"""
	It is a class derived from prog_cfg used by the program run-fgen
	"""

	def __init__(self,dbg = False): ## {
		## initialize the fgen tool information.
		self.__init__(dbg); ## call super.__init__

		self.__opt__.set_support('eda','specify the eda tool, for now, valid only for VCS tool, and interfaces \
		will be retained for other eda tools.','edatool');

		self.__opt__.set_support('help','help option to display all valid options for fgen tool.');

		self.__opt__.set_support.('rtl','specify the rtl type to lead the tool to generate the different combination \
		of compile.lis. Default rtl_type is \'asic\'.','rtl_type');

		self.__opt__.set_support('path','specify the path to generate the filelist, this is an optional param, if \
		not specified, the default path: <proj_home>/out/sim/<rtl_type>/tests/ will be used.','dest_path');

		self.__opt__.set_support('proj_home','the project home specified by caller.','path');

		self.__opt__.set_support('erf','external rtl file, this means the file should be added to rtl.lis, with \
		different rtl mode, the erf can specify corresponding rtl modules.','file_name');

		self.__opt__.set_support('y','to specify the library path, by different eda tools, this option will be \
		translated to the corresponding options recognized by the tool. Besides, this option only \
		support the eda tool that can support filelist option insertion.','library');

		self.__opt__.set_support('libext','this option work together with -y option, to specify the searching \
		file with specified extension. This option can be input with multiple times for specifying \
		multiple extensions.','extensions');

		self.__opt__.set_support('target','the option specify the destined usage for calling this tool. the \
		target name for now are valid within: \
		\n -- sim: for simulation, in this target, the compile.lis, rtl.lis, dpi.lis, fsim.lis and \
		sim_model.lis will be generated nomatter files above exists or not. \
		\n -- wav: for wave vision, in this target, wave.lis, rtl.lis, fsim.lis and sim_model.lis will \
		be generated nomatter files above exists or not.','target_name');

		self.__opt__.set_support('pt','the project type option, valid only within IP and SOC.','proj_type');

		self.__opt__.set_support('debug','the debug enable switch, use this option to display debug information.');

		return; ## return void.
	## }

## }
