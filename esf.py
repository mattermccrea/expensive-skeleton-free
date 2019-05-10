#!/usr/bin/env python

from subprocess import call
import argparse
import sys
import platform
import os

from lib.source.xframe import *
from lib.ui.Ui import *

if platform.python_version().split('.')[0] != '2':
	print "\033[1;31m[!] \033[1;30m kamu menggunakan Python versi %s.. silahkan ganti ke versi 2 "%v().split(' ')[0]
	sys.exit()

if os.name == "nt":
	try:
		from colorama import init,AnsiToWin32
		init()
	except ImportError:
		print """

INFORMATION:
	kamu menggunakan Windows atau sebagian dari versi
	NT.
	dan kamu belum memiliki Liblary colorama untuk men-
	jalankan ESF agar lebih maksimal.
	untuk menjalankan ESF dengan secara sah... kamu harus
	menginstall colorama terlebih dahulu
	
		"""
		while True:
			x = raw_input("install colorama [y/n]\t\t")
			if x == "y" or x == "Y":
				call('pip install colorama',shell=True)
			elif x == 'N' or x == 'n':
				sys.exit()
			else:
				print "invalid commands"
else:
	pass

p = argparse.ArgumentParser()
p.add_argument("-v", help = "melihat versi dari E.S.F", action = "store_true", dest="V")
p.add_argument("-c", "--company", help = "Credits", action = "store_true",dest="C")
p.add_argument("-T", "--test", help = "tes Kerentanan Web", dest="Web")
a = p.parse_args()

if a.V:
	print "1.4.5 "
elif a.C:
	print "Copyright (C) 8 Ball, Muhammad Quwais Safutra 2017 - 2019"
elif a.Web:
	Banner()
	Test(a.Web)