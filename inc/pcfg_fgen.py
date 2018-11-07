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

class pcfg_fgen: ##

	__owner__ = 'Neo.H';

	## the project home, if not entered by user, then use './' as default.
	g_proj_home = '';

	## the output path indicates where to generate the target list file, if not entered by
	## user, then use './' instead.
	g_o_path = '';

	## the eda tool as the target, indicates which tool will use the generated list
	## if not entered by user, then will use 'vcs' as default.
	g_eda = '';


	g_lpaths = []; ## this is a list to store the lib path for verilog or other src files, default is empty.

	## this is the libext that combined with lib path, only when lib path is not empty, can this value applyed to the file list
	## else if this option not entered by user, the default value '.v', only when the list is empty, the default value will be used.
	##
	g_libext = [];
	g_libext_df = '.v'; ## the default libext

	## switch for help mode, if this switch is True, then entered the help display procedure.
	g_help = False;


	## the debug switch, if enabled, all debug information in this program will be displayed.
	g_debug = False;

	## the rtl type specified by user, if not specified, then use the default value: 'asic'
	## this var valid only within 'asic','fpga' and 'gate'.
	g_rtl_t = 'asic';

	## the target usage for generating this list, for now, only verdi need a special list without dpi.lis
	## so the target only valid when eda is 'vcs'.
	## if user not specified this option, then use the default value: 'sim'
	g_target = '';


	## the project type var, if not specified by user, then use 'IP'
	g_pt = '';

	## the list to storing external rtl files, default is empty.
	g_erfs = [];

	## the list ot storing external sim_model files, default is empty.
	g_esfs = [];

	## the list storing all valid uvcs from user entering.
	g_uvcs = [];

	## the directory structure of current methodology.
	##
	g_hierachy = {
		'design': {
			'general': 'design/tops',
			'asic'   : 'design/asic',
			'fpga'   : 'design/fpga',
			'gate'   : 'design/gate',
		},
		'sim_model': {
			'general': 'verif/sim_model/general',
			'asic'   : 'verif/sim_model/asic',
			'fpga'   : 'verif/sim_model/fpga',
		},
		'fsim': {
			'btest': 'verif/fsim/base_test',
			'tests': 'verif/fsim/tests',
			'tb'   : 'verif/fsim/tb',
			'tenv' : 'verif/fsim/top_env',
			'dpi'  : 'verif/fsim/dpi',
			'rfm'  : 'verif/fsim/rfm',
			'scb'  : 'verif/fsim/scoreboard',
		},
		'formal': {
		},
	};



	def __init__(self,argvs,rpt): ## {
		g_opt = options();

		g_opt.set_support('eda','\n\tspecify the eda tool, for now, valid only for vcs tool, \n\tand interfaces will be retained for other eda tools.','edatool');

		g_opt.set_support('help','\n\thelp option to display all valid options for fgen tool.');

		g_opt.set_support('rtl','\n\tspecify the rtl type to lead the tool to generate the different \n\tcombination of compile.lis. Default rtl_type is \'asic\'.','rtl_type');

		g_opt.set_support('path','\n\tspecify the path to generate the filelist, this is an optional param, \n\tif not specified, the default path: <proj_home>/out/sim/<rtl_type>/tests/ will be used.','dest_path');

		g_opt.set_support('proj_home','\n\tthe project home specified by caller.','path');

		g_opt.set_support('erf','\n\texternal rtl file, this means the file should be added to rtl.lis, this option used to load common rtls, \n\twith different rtl mode, the erf can specify corresponding rtl modules.','file_name');

		g_opt.set_support('esf','\n\texternal sim_model file, this means the file should be added to sim_model.lis, this option used to load common sim_models, \n\twith different rtl mode, the esf can specify corresponding sim_model modules.','file_name');

		g_opt.set_support('uvc','\n\tspecify the uvc package with path.','uvc_pkg');

		g_opt.set_support('y','\n\tto specify the library path, by different eda tools, this option will be \n\ttranslated to the corresponding options recognized by the tool. Besides, \n\tthis option only support the eda tool that can support filelist option insertion.','library');

		g_opt.set_support('libext','\n\tthis option work together with -y option, to specify the \n\tsearching file with specified extension. This option can be input \n\twith multiple times for specifying multiple extensions.','extensions');

		g_opt.set_support('target','\n\tthe option specify the destined usage for calling this tool. \n\tthe target name for now are valid within: \n <sim>: for simulation, in this target, the compile.lis, rtl.lis, \n\tdpi.lis, fsim.lis and sim_model.lis will be generated nomatter files above exists or not. \n <wav>: for wave vision, in this target, wave.lis, rtl.lis, fsim.lis \n\tand sim_model.lis will be generated nomatter files above exists or not.','target_name');

		g_opt.set_support('pt','\n\tthe project type option, valid only within IP, SUBS and SOC.','proj_type');

		g_opt.set_support('debug','\n\tthe debug enable switch, use this option to display debug information.');


		## -- option process -------------------------------------------------------------------------
		if g_opt.load(argvs) == False: ## {
			rpt.fatal("program fatal occurred when check option.");
			exit(1);
		## }

		self.g_proj_home = g_opt.get_param('proj_home');
		if self.g_proj_home == False: self.g_proj_home = './'; ## if the proj_home is not specified by user, then use default value: './'


		## the var that indicates the eda tool user want to use, then we will generate corresponding file list.
		## value valid in range of: 'vcs' and 'xcelium'.
		self.g_eda = g_opt.get_param('eda');
		if self.g_eda == False: self.g_eda = 'vcs'; ## default use vcs tool if no user entered -eda

		while g_opt.exists('y'): ## {
			## while the 'y' param exists, then to pop the param until all user entered -y are poped from the argv pool
			self.g_lpaths.append(g_opt.get_param('y'));
		## }

		while g_opt.exists('libext'): ## {
			## and this option can be specified by user with multiple times
			self.g_libext.append(g_opt.get_param('libext'));
		## }

		self.g_help = g_opt.exists('help');

		self.g_debug = g_opt.exists('debug');

		self.g_rtl_t = g_opt.get_param('rtl');
		if self.g_rtl_t == False: self.g_rtl_t = 'asic'; ## if get the False type, then use the default value: 'asic'

		self.g_target = g_opt.get_param('target');
		if self.g_target == False: self.g_target = 'sim'; ## if get the False param, then use default: 'sim'.

		self.g_pt = g_opt.get_param('pt');
		if self.g_pt == False: self.g_pt = 'IP'; ## if get the False param, then use default: 'IP'

		self.g_o_path = g_opt.get_param('path');
		if self.g_o_path == False: self.g_o_path = self.g_proj_home+'/out/sim/'+self.g_rtl_t+'/tests'; ## if the path not specified by user, then use default output path .


		while g_opt.exists('erf'); ## {
			## this option can be called multiple times.
			self.g_erfs.append(g_opt.get_param('erf'));
		## }

		while g_opt.exists('esf'): ## {
			## this option can be called multiple times for sim_model.
			self.g_esfs.append(g_opt.get_param('esf'));
		## }

		while g_opt.exists('uvc'): ## {
			## this option can be called multiple times for uvc packages.
			self.g_uvcs.append(g_opt.get_param('uvc'));
		## }

		return;

	## }



	def help(self): ## {
		"""
		It is a help mode process function, because the fgen is a sub program, so just to print a simple help information.
		"""
		g_opt.descript();
	## }



## }
