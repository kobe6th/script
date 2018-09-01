import os.path
import time
import shutil
import sys, getopt

def getWin10Wallpaper(srcDirPath, desDirPath):
	if not os.path.isdir(srcDirPath):
		print(srcDirPath, "path not found!")
		return

	if not os.path.isdir(desDirPath):
		os.mkdir(desDirPath)
		print("mkdir", desDirPath)

	srcPics = os.listdir(srcDirPath)
	desPics = os.listdir(desDirPath)
	now = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	for pic in srcPics:
		picSrcPath = os.path.join('%s/%s' % (srcDirPath, pic))
		picDesPath = os.path.join('%s/%s.jpg' % (desDirPath, pic))
		if os.path.isfile(picSrcPath) \
			and (not isRepeateWallpaper(pic, desPics)):
				saveWallpaper(picSrcPath, picDesPath)

def isWallPaper(file):
	fileSize = os.path.getsize(file)
	return fileSize >= 200 * 1024

def isRepeateWallpaper(pic, desPics):
	for des in desPics:
		pos = des.find(pic)
		if pos == -1:
			return True
	return False

def saveWallpaper(srcPath, desPath):
	if isWallPaper(srcPath):
		shutil.copyfile(srcPath, desPath)
		print(desPath, "save!")

def usage():
	print("usage: python wallpaper.py -u WindowsUser -d picSaveDir")

if __name__ == '__main__':
	user = "51950"
	desDirPath = "E:/picture/wallpaper"
	opts, args = getopt.getopt(sys.argv[1:], "hu:d:")
	for op, value in opts:
		if op == "-u":
			user = value
		elif op == "-d":
			desDirPath = value
		else :
			usage()
			sys.exit()

	srcDirPath = 'C:/Users/%s/AppData/Local/Packages/' % (user) +\
				"Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets"
	getWin10Wallpaper(srcDirPath, desDirPath)