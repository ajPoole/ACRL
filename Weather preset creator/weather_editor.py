#!/usr/bin/python
#-*- coding:utf-8 -*-
import ast
#Populate track list
trackdetails = []
with open('copy_of_weather.py','r') as tracks:
    for track in tracks.readlines():
        if track.strip():
            trackdetails.append(ast.literal_eval(track.strip()))




#Add or change a weather profile
def addRealisticWeather(track,layout,name,ambient,track_rela,ambient_r,track_r,w_type):
#    if(not checkDuplicate(name)):
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
        return 'Track added.'
 #   else:
  #      return 'Duplicate track!'

#Edits a current preset. Can also delete if checkbox was checked from the webpage.
def editRealisticWeather(track,layout,name,ambient,track_rela,ambient_r,track_r,w_type,delete):
    f = open('copy_of_weather.py','r')
    lines = f.readlines()
    f.close()
    with open('copy_of_weather.py','w') as newsets:
        for line in lines:
            line2 = ast.literal_eval(line)
            if name!=line2['name']:
                newsets.write(line)
    newsets.close()
    if not delete:
        print addRealisticWeather(track,layout,name,ambient,track_rela,ambient_r,track_r,w_type)
        return 'Track edited.'
    else:
        return 'Track deleted.'


def checkDuplicate(name):
    name=name.strip()
    for i in range(len(trackdetails)):
        if trackdetails[i]['name'].lower()==name.lower():
            return True
    return False

#Don't quite remember what this was for. Best not remove it.
def getWeatherDictKeys():
    keys = []
    for key in trackdetails[0]:
        keys.append(key)
    return keys

#status = editRealisticWeather("ks_test","gp","Test 2","23","10","3","4","hot",False)
#print status


