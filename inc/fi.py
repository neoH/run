#! /usr/bin/env python3

"""
---------------------------------------------------------------------------------------------
# File    : fi.py (fgen include file)
# Author  : Neo.H
# Date    : Oct 11, 2018
# Version : v1.00
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------

"""

from shell import shell;
import foper;
import re;

__rtl_lis__ = 'rtl.lis';

def debug_info(ID,msg):
	## print debug information
	print ("[__DBG__]["+ID+"] "+msg);

## end def }


def inc_reorder(incs): ## {
	"""
	this is a function to reorder the include files, which probably to reorder the define and undefine files.
	"""
	index = 0;
	num   = len(incs);
	while index < num: ## {
		## loop the incs list
		def_obj = re.search("_def\.h",inc);
		udef_obj = re.search("_udef\.h",inc);

		## get the define file.
		if def_obj != None: incs.insert(0,incs.pop(index)); ## change the item of current index into 0 pos.

		## get the undefine file.
		if udef_obj != None: incs.insert(num-1,incs.pop(index));

		index += 1; ## add index
	## }
	if pf.g_debug: debug_info('inc_reorder',"the inc list after reordering:\n"+incs);
	return;
## }


def get_incdir(srcs): ## {
	"""
	get the dirs in input lis at the front of the lis. According to the files list in the lis.
	"""
	incdirs = [];
	for src in srcs: ## {
		obj = re.search('\/[\w|_]+\.\w',src);
		if obj != None: ## {
			## if the file and path matched, then need to get the path first, and then check if already in incdirs.
			path = src[0:obj.start()];
			if not path in incdirs: incdirs.append(path); ## if path not in incdirs, then need to add this path
		## }
	## }
	## after looping all, then to push all incdirs into the srcs.
	for incdir in incdirs: ## {
		srcs.insert(0,incdir); ## insert to the first index
	## }

	return; ## return now without anything.
## }

def get_rtl_incs(proj_home,hierachy,rtl_t,debug): ## {
	"""
	this is a func. to get include files for rtl.
	only valid within asic mode or fpga mode
	"""
	sh = shell();
	cmd = 'find '+proj_home+'/'+hierachy['design'][rtl_t]+'/inc -mindepth 1 -name "*.h"'; ## to recognize all the *.h file
	if debug: debug_info('get_rtl_incs',"to get "+rtl_t+" include file of rtl by the command:\n"+cmd);
	incs = sh.get_output(cmd); ## get the inc *.h list

	## after getting the asic include file, then need to get include file in general
	cmd = 'find '+proj_home+'/'+hierachy['design']['general']+'/inc -mindepth 1 -name "*.h"'; ## to recognize all the *.h file
	if debug: debug_info('get_rtl_incs',"to get general include file of rtl by the command:\n"+cmd);
	incs.extend(sh.get_output(cmd));

	##inc_reorder(incs); ## reorder the include file

	return incs;
## end def }

def get_rtl_srcs(proj_home,hierachy,rtl_t,debug): ## {
	"""
	this is a function to get source files for rtl, only valid in asic or fpga mode.
	"""
	sh = shell();
	cmd = 'find '+proj_home+'/'+hierachy['design'][rtl_t]+'/src/v -mindepth 1 -name "*.v"'; ## to recognize all the *.v files
	if debug: debug_info('get_rtl_srcs',"to get "+rtl_t+" src files of rtl by the command:\n"+cmd);
	srcs = sh.get_output(cmd);

	## after getting the asic src files, then need to get src files in general
	cmd = 'find '+proj_home+'/'+hierachy['design']['general']+'/src/v -mindepth 1 -name "*.v"'; ## to recognize all the *.v files
	if debug: debug_info('get_rtl_srcs',"to get general src files of rtl by the command:\n"+cmd);
	srcs = sh.get_output(cmd);

	return srcs;
## }

def get_rtls(pf): ## {
	"""
	Program to get all rtl files, and store to a list var.
	"""
	rtls = [];
	if pf == None: return rtls; ## if input pf is null, then return an empty list
	## else pf not null.
	if pf.g_debug: debug_info('get_rtls',"current program now in "+pf.g_pt+" mode.");
	if pf.g_pt   == 'IP': ## {
		## to process in IP project type
		## in IP mode, need to select following rtl type: asic/fpga or gate
		if pf.g_rtl_t == 'asic': ## {
			## in asic mode, to do the following with ordering
			## 1. commons rtl, which given by the user, stored in pf.g_erfs
			## 2. asic rtl
			## 3. general rtl
			if len(pf.g_erfs) != 0: rtls.extend(pf.g_erfs); ## if erfs has item, then to add to the rtls list.
			asic_incs = get_rtl_incs(pf.g_proj_home,pf.g_hierachy,pf.g_rtl_t,pf.g_debug);

			## after getting include file for asic mode, then need to get source file of asic.
			asic_srcs = get_rtl_srcs(pf.g_proj_home,pf.g_hierachy,pf.g_rtl_t,pf.g_debug);

			rtls.extend(asic_incs);rtls.extend(asic_srcs); ## merge the two temple list into rtls
			inc_reorder(rtls); ## reorder, to set *_def.h file to the front of the list and *_udef.h file to the bottom of the list
			get_incdir(rtls);  ## add incdir to the top of list.
			return rtls; ## now return the rtl list.
		## }
		elif pf.g_rtl_t == 'fpga': ## {
			## in fpga mode, to do the following with ordering
			## 1. commons rtl
			## 2. fpga rtl
			## 3. general rtl
			if len(pf.g_erfs) != 0: rtls.extend(pf.g_erfs); ## if erfs has item here, then to add to the rtls list.
			fpga_incs = get_rtl_incs(pf.g_proj_home,pf.g_hierachy,pf.g_rtl_t,pf.g_debug);

			## after getting cinlude file for fpga mode, then need to get source file of fpga.
			fpga_srcs = get_rtl_srcs(pf.g_proj_home,pf.g_hierachy,pf.g_rtl_t,pf.g_debug);

			rtls.extend(fpga_incs);rtls.extend(fpga_srcs); ## merge the two temple list into rtls
			inc_reorder(rtls); ## reorder all inc files in the rtls list.
			get_incdir(rtls); ## add incdir for all incs and srcs
			return rtls;
		## }
		else: ## {
			## in gate mode, to do the following with ordering
			## 2. gate rtl
			## for gate mode, only files in gate/v/ will be collected.
			if len(pf.g_erfs) != 0: rtls.extend(pf.g_erfs); ## if erfs has item here, then to add to the rtls list.
			gate_srcs = get_rtl_srcs(pf.g_proj_home,pf.g_hierachy,pf.g_rtl_t,pf.debug);
			rtls.extend(gate_srcs); ## merge all gate_srcs into rtls.
			get_incdir(rtls);
			return rtls;
		## }
	## end of IP branch }
	elif pf.g_pt == 'SUBS':
	## }
	else:
		## SOC level
	## }
## end def }

def gen_rtl_lis(contents, opath = ""):
	"""
	this func. to generate rtl list according to input contents, current function will call foper.write_cnts
	directly.
	"""
	foper.write_cnts(opath+'/'+__rtl_lis__,contents);
## end def }


def get_sim_models ():


## end def %
