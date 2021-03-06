#! /usr/bin/env python3

"""
---------------------------------------------------------------------------------------------
# File    : exception
# Author  : Neo.H
# Date    : Sep 14, 2018
# Version : v1.00
---------------------------------------------------------------------------------------------
This is an exception processing class that define the exception SIG and all needed exception
processing methods.
---------------------------------------------------------------------------------------------
Supporting exception SIGs, these SIGs used in the different processes of run kit:
	-- 0: normal level verbosity exit SIG.
	-- 1: warning level verbosity exit SIG.
	-- 2: error exit SIG, indicates the error occurred because of illegal input.
	-- 3: error exit SIG, indicates the error caused by the target exiting program, though the
	input is legal, the combination may cause errors.
	-- 4: error exit SIG, indicates an unexcepted error occurred by the target program self.
	-- 5: error exit SIG, this may occur when the condition triggered out of the consideration
	of the developer.
---------------------------------------------------------------------------------------------
Supporting exception Exit, these SIGs will be used to report errors for the user who called
the run command:
	-- 0: normal exit SIG, no error will reported.
	-- 1: warning SIG, indicates user has entered a conflict but not critical combinative options.
	-- 2: error SIG, indicates the user command error.
	-- 3: error SIG, indicates the program error by developer.
	-- 4:
---------------------------------------------------------------------------------------------
"""

import rpt;
import sys;

class exception: ## {

	__prog_exit_d = {
		'NM'  : 0,
		'WN'  : 1, ## warning signal
		'UE'  : 2, ## indicates the error caused by user
		'PE'  : 3, ## indicates the error caused by program
	};



	## this is a function to exit with PE verbosity. In this verbosity, the
	## program will print a certain text for PE exiting.
	##
	def exit_pe(self): ## {
		rpt.fatal("program exit with a critical fatal.");
		sys.exit(self.__prog_exit_d['PE']);
	## }

	## this is a func. to exit with UE verbosity. This func. will be called when an
	## error occurred.
	##
	def exit_ue(self): ## {
		rpt.error("program exit with a user input error.");
		sys.exit(self.__prog_exit_d['UE']);
	## }

	## this is a func. to exit with NM verbosity. This func. will be called when the
	## program exit normally.
	##
	def exit_nm(self): ## {
		sys.exit(self.__prog_exit_d['NM']);
	## }



## }
