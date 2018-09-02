#!coding:utf-8
import urllib.request
import time, os.path
from html.parser import HTMLParser
import sys, getopt


class MyHTMLParser(HTMLParser):
	wallpaperPath = ''
	def handle_starttag(self, tag, attrs):
		if tag != "img":
			return

		for attr in attrs:
			if attr[0] == 'src' and (attr[1].find('.jpg') != -1):
				self.wallpaperPath = attr[1]

	def getWallpaperPath(self):
		return self.wallpaperPath
	# def handle_endtag(self, tag):
	#     print("End tag  :", tag)

	# def handle_data(self, data):
	#     print("Data     :", data)

	# def handle_comment(self, data):
	#     print("Comment  :", data)

	# def handle_entityref(self, name):
	#     c = chr(name2codepoint[name])
	#     print("Named ent:", c)

	# def handle_charref(self, name):
	#     if name.startswith('x'):
	#         c = chr(int(name[1:], 16))
	#     else:
	#         c = chr(int(name))
	#     print("Num ent  :", c)

	# def handle_decl(self, data):
	#     print("Decl     :", data)

def getBingBackground(path):
	url = 'http://www.bing.com'
	header={
		'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
	}

	request=urllib.request.Request(url,headers=header)
	response=urllib.request.urlopen(request)

	parser = MyHTMLParser()
	parser.feed(response.read().decode('utf-8'))
	if len(parser.getWallpaperPath()) == 0:
		print("getBingBackground addr faild!")
		return

	url = url + parser.getWallpaperPath()
	request = urllib.request.Request(url)
	response = urllib.request.urlopen(request)

	if response.status != 200:
		print(url, 'status = ', response.status)
	else:
		picData = response.read()
		now = time.strftime('%Y-%m-%d',time.localtime(time.time()))
		picPath = os.path.join('%s/bing-%s.jpg' % (path, now))
		try:
			file = open(picPath, 'wb')
			file.write(picData)
			file.close()
			print(picPath, "save!")
		except Exception as e:
			print("open", picPath, "Exception.", e)
		else:
			pass
		finally:
			pass

def usage():
	print("usage: python wallpaper.py -d picSaveDir")

if __name__ == '__main__':
	desDirPath = "E:/picture/wallpaper"
	opts, args = getopt.getopt(sys.argv[1:], "hd:")
	for op, value in opts:
		if op == "-d":
			desDirPath = value
		else :
			usage()
			sys.exit()
	getBingBackground(desDirPath)

	

