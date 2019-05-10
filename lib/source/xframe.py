from lib.ui.Ui import *
import requests
import sys

def Test(url):
	if "http://" not in url:
		urls = "http://"+url
		print Sec.info+"Testing X-Frame clickjacking..."
		try:
			r = requests.get(urls)
			with open("web.html","w") as f:
				f.write(r.content)
				f.close()
			print Sec.info+"checking from foles.html is there <embed> or <iftame>..."
			i = open("web.html","r")
			if "<embed>" or "<iframe>" in i:
				print Sec.info+"Website Is Vuln Of \033[1;33m X-Frame Clickjacking"
				with open("vuln.txt","wb") as f:
					f.write("VULN\n1. X-Frame Clickjacking")
					f.close()
			else:
				print Sec.info+"X Frame Is Safe!"
		except:
			print Sec.fail+"Error To Getting the url"
			sys.exit()
	print Sec.info+"Testing X-Frame clickjacking..."
	try:
		r = requests.get(url)
		with open("foles.html","wb") as f:
			f.write(r.content)
			f.close()
		print Sec.info+"checking from foles.html is there <embed> or <iftame>..."
		i = open("foles.html","r")
		if "<embed>" and "<iframe>" in i:
			print Sec.info+"Website Is Vuln Of \033[1;33m X-Frame Clickjacking"
			with open("vuln.txt","wb") as f:
				f.write("VULN\n1. X-Frame Clickjacking")
				f.close()
		else:
			print Sec.info+"X Frame Is Safe!"
	except:
		print Sec.fail+"Error To Getting the url"
		sys.exit()