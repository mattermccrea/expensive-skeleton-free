from datetime import datetime

t = datetime.now().strftime("\033[1;33m[\033[1;37m%H:%M\033[1;33m][")
class Sec:
	info = t+"\033[1;32mINFO\033[1;33m]\033[1;37m "
	fail = t+"\033[1;31mFAIL\033[1;33m]\033[1;31m "
	warn = t+"\033[1;31mWARN\033[1;33m]\033[1;30m "
	
def Banner():
	print r"""
                                 
 _____ _       _     _           
|   __| |_ ___| |___| |_ ___ ___ 
|__   | '_| -_| | -_|  _| . |   |
|_____|_,_|___|_|___|_| |___|_|_|
"""
	print """
\033[1;31m+\033[1;33m--=[ \033[1;31me\033[1;30mxpensive \033[1;31ms\033[1;30mkeleton\033[1;32m free
\033[1;31m+\033[1;33m--=[ \033[1;30mBy    : 8 Ball, Muhammad Quwais Safutra\n\n
     """