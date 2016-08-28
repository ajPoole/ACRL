#!/usr/bin/python
#-*- coding: utf-8 -*-
import random
import math

welcome_msg="""
###################################
####ACRL Weather Preset Creator####
####Made by twizzR with love :)####
###################################
"""

#Database of realistic weather taken from actual racing
trackdetails = [
{"name":"Red Bull Ring","ambient":28,"track_relative":11,"ambient_r":3,"road_r":4,"type":"hot"},
{"name":"Laguna Seca","ambient":24,"track_relative":5,"ambient_r":1,"road_r":2,"type":"cold"},
{"name":"Algarve","ambient":27,"track_relative":11,"ambient_r":2,"road_r":4,"type":"hot"},
{"name":"Road America","ambient":13,"track_relative":-3,"ambient_r":2,"road_r":1,"type":"cold"},
{"name":"Silverstone","ambient":8,"track_relative":2,"ambient_r":1,"road_r":2,"type":"cold"},
{"name":"Paul Ricard","ambient":32,"track_relative":8,"ambient_r":4,"road_r":1,"type":"hot"},
{"name":"Nurburgring","ambient":18,"track_relative":11,"ambient_r":2,"road_r":2,"type":"hot"},
{"name":"Misano cold","ambient":18,"track_relative":1,"ambient_r":2,"road_r":1,"type":"cold"},
{"name":"Misano hot","ambient":23,"track_relative":13,"ambient_r":3,"road_r":3,"type":"hot"}
]

"""
[WEATHER_0]
GRAPHICS=3_clear
BASE_TEMPERATURE_AMBIENT=23
BASE_TEMPERATURE_ROAD=9
VARIATION_AMBIENT=0
VARIATION_ROAD=0
"""


#Takes sun angle from server or time(8-18) and converts it either way.
def sunAngleToTime(angle,timeToAngle):
	convert = {}
	j=8
	for i in range(-80,80,16):
		convert.update({
			i:j
			})
		j+=1
	if(timeToAngle):
		inv_map = {v: k for k, v in convert.items()}
		return inv_map[angle]
	else:
		return convert[angle]


		
#Calculates realistic road temp like the server tool. Thanks Manuel Darin!
def realisticRoadTemp(angle,ambient,coeff):
	e = 2.718281828
	tod = (sunAngleToTime(angle,False)-7.0)*(1.0/24.0)
	d = ((((-10.0*coeff)*tod)+(10.0*coeff))*2.0*((e**(-6.0*tod)*(0.4*math.sin(6.0*tod))+0.1) * (ambient/1.5) * math.sin(0.9*tod)))
	return int(d)
	
###TODO: Take in a server cfg, find time of day, create realisitc road temp and use it for the random presets. Needs weather.ini coeffs and sun angle.
###TODO: Gotta add in fog somewhere too. new for loop cause who needs efficiency?
#Creates x amount of presets to a certain realistic setting.
def createPresets(trackdetails,amount,fog):
	#Weather types for the kind of weather expected.
	hot = ["6_mid_clouds","3_clear","4_mid_clear","5_light_clouds","6_mid_clouds","3_clear"]
	cold = ["5_light_clouds","7_heavy_clouds","6_mid_clouds","6_mid_clouds"]
	fog = ["2_light_fog","1_heavy_fog"]
	presets = []
	track_type = trackdetails['type']
	#Add the actual realisitc weather as one entry first.
	presetString=""
	presetString+="[WEATHER_0]\n"
	if track_type=="hot":
		rand_index=random.randrange(0,len(hot))
		presetString+="GRAPHICS="+hot[rand_index]+"\n"
	else:
		rand_index=random.randrange(0,len(cold))
		presetString+="GRAPHICS="+cold[rand_index]+"\n"
	presetString+="BASE_TEMPERATURE_AMBIENT="+str(trackdetails['ambient'])+"\n"
	presetString+="BASE_TEMPERATURE_ROAD="+str(trackdetails['track_relative'])+"\n"
	presetString+="VARIATION_AMBIENT="+str(trackdetails['ambient_r'])+"\n"
	presetString+="VARIATION_TRACK="+str(trackdetails['road_r'])+"\n"
	presetString+="\n"
	presets.append(presetString)
	
	#Create x amount of random presets with variation of the realisitc weather.
	for i in range(amount):
		presetString =""
		presetString+="[WEATHER_"+str(i+1)+"]\n"
		if track_type=="hot":
			rand_index=random.randrange(0,len(hot))
			presetString+="GRAPHICS="+hot[rand_index]+"\n"
		else:
			rand_index=random.randrange(0,len(cold))
			presetString+="GRAPHICS="+cold[rand_index]+"\n"
		ambient_variation = random.randrange(-3,3)
		presetString+="BASE_TEMPERATURE_AMBIENT="+str(+trackdetails['ambient']+ambient_variation)+"\n"
		track_variation = random.randrange(-3,2)
		#presetString+="BASE_TEMPERATURE_ROAD="+str(realisticRoadTemp(angle,trackdetails['ambient'],coeff))+"\n"
		presetString+="BASE_TEMPERATURE_ROAD="+str(+trackdetails['track_relative']+track_variation)+"\n"
		presetString+="VARIATION_AMBIENT="+str(trackdetails['ambient_r'])+"\n"
		presetString+="VARIATION_TRACK="+str(trackdetails['road_r'])+"\n"
		presetString+="\n"
		presets.append(presetString)
	
	
	
	return presets
	
def main():
	print welcome_msg
	
	for i in range (len(trackdetails)):
		print str(i+1) + ") " + trackdetails[i]['name']+"\n"
	#track_name = raw_input("Please enter a track name:\n")
	track_name = "Red Bull Ring"
	
	for i in range (len(trackdetails)):
		if trackdetails[i]['name']==track_name:
			selected = trackdetails[i]
			break
	
	#amount = int(raw_input("How many extra presets would you like:\n"),10)
	amount = 5
	#fog_q = raw_input("Fog?(Y/N)\n")
	fog_q = 'n'
	fog=True if fog_q.lower()=='y' else False
	if (fog): print "Adding two fog settings.."
	presets = createPresets(selected,amount,fog)
	for preset in presets:
		print preset
#main()
