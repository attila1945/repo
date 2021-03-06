﻿# -*- coding: utf-8 -*-
# 12.08.2018 - ©realvito

import sys
import os
import xbmc
import xbmcgui
import xbmcaddon
import xbmcvfs
import shutil


PY2 = sys.version_info[0] == 2
__addon__ = xbmcaddon.Addon('service.L0RE.cron')
addonPath = xbmc.translatePath(__addon__.getAddonInfo('path')).encode('utf-8').decode('utf-8')
profile    = xbmc.translatePath(__addon__.getAddonInfo('profile')).encode('utf-8').decode('utf-8')
temp       = xbmc.translatePath(os.path.join( profile, 'temp', '')).encode('utf-8').decode('utf-8')
database = os.path.join(temp, 'cron.db')
icon = os.path.join(addonPath ,'icon.png')


class Unload:
	def __init__(self, *args, **kwargs):
		if sys.argv[1] == "loeschen":
			if os.path.isdir(temp) and xbmcvfs.exists(database):
				if xbmcgui.Dialog().yesno(heading=__addon__.getAddonInfo('id'), line1=translation(30502), line2=translation(30503), nolabel=translation(30504), yeslabel=translation(30505)):
					shutil.rmtree(temp, ignore_errors=True)
					xbmc.sleep(1000)
					xbmcgui.Dialog().notification(translation(30521), translation(30522), icon, 8000)
					xbmc.log("["+__addon__.getAddonInfo('id')+"](unload.py) ########## DELETING complete DATABASE ... "+database+" ... success ##########", xbmc.LOGNOTICE)
				else:
					return# they clicked no, we just have to exit the gui here
			else:
				xbmcgui.Dialog().ok(__addon__.getAddonInfo('id'), translation(30506))

def py2_enc(s, encoding='utf-8'):
	if PY2 and isinstance(s, unicode):
		s = s.encode(encoding)
	return s

def translation(id):
	LANGUAGE = __addon__.getLocalizedString(id)
	LANGUAGE = py2_enc(LANGUAGE)
	return LANGUAGE

def Main():
	Unload()

if (__name__ == "__main__"):
	Main()
