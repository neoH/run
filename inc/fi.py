#! /usr/bin/env python3

"""
---------------------------------------------------------------------------------------------
# File    : fi.py
# Author  : Neo.H
# Date    : Oct 11, 2018
# Version : v1.00
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------

"""

from shell import shell;
import re;

def debug_info(ID,msg):
	## print debug information
	print ("[__DBG__]["+ID+"] "+msg);

## end def }


def inc_reorder(incs):
	"""
	this is a function to reorder the include files, which probably to reorder the define and undefine files.
	"""
	for inc in incs:
		## loop the incs list
		obj = re.search("_def\.h",inc);
		if obj != None:
			## get the define file.
## }

def get_rtls(pf):
	"""
	Program to get all rtl files, and store to a list var.
	"""
	rtls = [];
	sh = shell();
	if pf == None: return rtls; ## if input pf is null, then return an empty list
	## else pf not null.
	if pf.g_debug: debug_info('get_rtls',"current program now in "+pf.g_pt+" mode.");
	if pf.g_pt   == 'IP':
		## to process in IP project type
		## in IP mode, need to select following rtl type: asic/fpga or gate
		if pf.g_rtl_t == 'asic':
			## in asic mode, to do the following with ordering
			## 1. commons rtl, which given by the user, stored in pf.g_erfs
			## 2. asic rtl
			## 3. general rtl
			if len(pf.g_erfs) != 0: rtls.extend(pf.g_erfs); ## if erfs has item, then to add to the rtls list.
			cmd = 'find '+pf.g_proj_home+'/'+pf.g_hierachy['design']['asic']+'/inc -mindepth 1 -name "*.h"'; ## to recognize all the *.h file
			if pf.g_debug: debug_info('get_rtls',"to get define file by the command:\n"+cmd);
			asic_incs = (sh.get_output(cmd)); ## get the inc *.h list
			inc_reorder(asic_incs);

		elif pf.g_rtl_t == 'fpga':
			## in fpga mode, to do the following with ordering
			## 1. commons rtl
			## 2. fpga rtl
			## 3. general rtl
		else:
			## in fpga mode, to do the following with ordering
			## 2. gate rtl
		## }
	## }
	elif pf.g_pt == 'SUBS':
	## }
	else:
	## }
## end def }
