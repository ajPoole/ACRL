#!/usr/bin/python
#-*- coding:utf-8 -*-
import ast

trackdetails = []
with open('copy_of_weather.py','r') as tracks:
    for track in tracks.readlines():
        if track.strip():
            trackdetails.append(ast.literal_eval(track.strip()))





def addRealisticWeather(track,layout,name,ambient,track_rela,ambient_r,track_r,w_type):
    if(not checkDuplicate(name)):
        with open('copy_of_weather.py','a') as presets:
            presets.write(
            '{"track":\"'+track.strip()+
            '\","layout":"'+layout.strip()+
            '\","name":"'+name.strip()+
            '\","ambient":'+ambient.strip()+
            ',"track_relative":'+track_rela.strip()+
            ',"ambient_r":'+ambient_r.strip()+
            ',"track_r":'+track_r.strip()+
            ',"type":"'+w_type.strip()+
            '\"}\n')
        return 'Track added'
    else:
        return 'Duplicate track!'


def checkDuplicate(name):
    name=name.strip()
    for i in range(len(trackdetails)):
        if trackdetails[i]['name'].lower()==name.lower():
            return True
    return False


def getWeatherDictKeys():
    keys = []
    for key in trackdetails[0]:
        keys.append(key)
    return keys

#status = addRealisticWeather("ks_test","gp","Test 2","23","10","3","4","hot")
#print status
