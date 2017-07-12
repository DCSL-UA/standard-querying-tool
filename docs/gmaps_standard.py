# -*- coding: utf-8 -*-
# @Author: Miclain Keffeler
# @Date:   2017-03-30 08:45:47
# @Last Modified by:   user
# @Last Modified time: 2017-05-17 19:14:44
#Script outputs all routes between 2 locations via driving, walking, biking, and transit
# Execute as such: 

import json, urllib
import googlemaps
import time
from datetime import datetime
import sys
import datetime

def get_mode(count):
  if(count == 0):
    return "driving"
  if(count == 1):
    return "walking"
  if(count == 2):
    return "bicycling"
  if(count == 3):
    return "transit"

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
def get_seconds(t1,t2,Entry_count):
  h1, m1, s1 = t1.hour, t1.minute, t1.second
  h2, m2, s2 = t2.hour, t2.minute, t2.second
  t1_secs = s1 + 60 * (m1 + 60*h1)
  t2_secs = s2 + 60 * (m2 + 60*h2)
  return((t2_secs - t1_secs)/Entry_count)


if (sys.argv[1]=="-help"):
   print "To Run, execute as  such: \"python gmaps.py <input_file_name> <output_file_name>\""
   print "\n"
   print "Output File defaults to stdout if not specified.\n"
   print "Input File Format = <lat,long,lat,long NEWLINE>No spaces until end of second pair"
   exit(-1)
output = open(sys.argv[2],"w")
#print sys.argv[1]
outputjson = open("google_output.json","w")
inputfile = open(sys.argv[1],"r")
#Path to output file created
API_KEY_INPUT = sys.argv[4]
modes_to_run = []
#-off and -on
Toggle_traffic_models = sys.argv[3]
#API KEY STORAGE
KEY2 = sys.argv[5]
KEY3 = sys.argv[6]
KEY4 = sys.argv[7]
KEY5 = sys.argv[8]
KEYS=[API_KEY_INPUT,KEY2,KEY3,KEY4,KEY5]

#Compile all modes to see which are to be run (ORDER: Driving,Walking,Biking,Transit)
all_modes = [sys.argv[9],sys.argv[10],sys.argv[11],sys.argv[12]]
mode_count = 0
#Get Count of how many modes we are running
for entry in all_modes:
  if(entry == "on"):
    mode = get_mode(mode_count)
    modes_to_run.append(mode)
  mode_count += 1

modes_printed = 0
header = ""
for entry in modes_to_run:
  if(modes_printed == len(modes_to_run)-1) or (len(modes_to_run)==1):
    if('driving' == entry):
        header += (entry[0] + "1time," + entry[0] +  "1traffic_time," + entry[0] + "1dist," + entry[0] + "2time," + entry[0] +  "2traffic_time," + entry[0] + "2dist," + entry[0] + "3time," + entry[0] +  "3traffic_time," + entry[0] + "3dist")
    else:
        header += (entry[0] + "1time," + entry[0] + "1dist," + entry[0] + "2time," + entry[0] + "2dist," + entry[0] + "3time," + entry[0] + "3dist")

  else:
    if('driving' == entry):
        header += (entry[0] + "1time," + entry[0] +  "1traffic_time," + entry[0] + "1dist," + entry[0] + "2time," + entry[0] +  "2traffic_time," + entry[0] + "2dist," + entry[0] + "3time," + entry[0] +  "3traffic_time," + entry[0] + "3dist,mode,")
    else:
        header += (entry[0] + "1time," + entry[0] + "1dist," + entry[0] + "2time," + entry[0] + "2dist," + entry[0] + "3time," + entry[0] + "3dist,mode,")
    modes_printed += 1

output.write("Slat,Slong,Dlat,Dlong,time,mode," + header)
address = ""
traffic_models_list = []
destination = ""
#print "<br>LINE COUNT: " + str(file_len(str(sys.argv[1])))

output.write("\n")
x=1
counter=0
y=0
time_stretch = sys.argv[15]
#print time_stretch
if (str(time_stretch) == "1"):
    start_time = sys.argv[13]
    end_time = sys.argv[14]
    time_stretch = sys.argv[15]
    time_over_entries = get_seconds(datetime.datetime.strptime(start_time,'%H:%M:%S').time(),datetime.datetime.strptime(end_time,'%H:%M:%S').time(),file_len(str(sys.argv[1])))
else:
    time_stretch = 0
for line in inputfile:
  if(counter>2450):
      API_KEY_INPUT = KEYS[y:x]
      x+=1
      y+=1
  address = line.strip().split(",")[0]+ ","+line.strip().split(",")[1]
  if(line.strip().split(',')[2][0] == ' '):
    destination = line.strip().split(",")[2][1:] + "," +line.strip().split(",")[3]
  else:
    destination = line.strip().split(",")[2] + "," +line.strip().split(",")[3]
  output.write(address+","+destination+",")
  output.write(str(datetime.datetime.now().strftime("%H:%M:%S")))
  traffic_models_list = []
  gmaps = googlemaps.Client(key = str(API_KEY_INPUT))
  iterate_counter=0
  for mode in modes_to_run:
    counter+=1
    for traffic_type in traffic_models_list:
      counter+=1
     # print counter
      output.write(",IF%s" % traffic_type)
      if(time_stretch == 1):
        time.sleep(time_over_entries)
      directions = gmaps.directions(address,destination,mode=mode,units="metric",departure_time=datetime.now(),alternatives="true")
      i=0
      #print directions
      output.write(",%s" % mode)
      iterate_counter+=1
      for route in directions:
        if(i<3):
          output.write(",")
          output.write(str(directions['routes'][i]['legs'][0]['duration']['value']))
          output.write(",")
          if(mode=='driving'):
            output.write(str(directions['routes'][i]['legs'][0]['duration_in_traffic']['value']))
            output.write(',')
          output.write(str(directions['routes'][i]['legs'][0]['distance']['value']))
          i+=1
      if(i<3 and mode == 'driving'):
        output.write(",NULL,NULL,NULL")
        i+=1
        while(i<3):
          output.write(","+"NULL"+",NULL,NULL")
          i+=1
      if(i<3):
        output.write(",NULL,NULL")
        i+=1
        while(i<3):
          output.write(","+"NULL"+",NULL")
          i+=1
    else:
      if(str(time_stretch) == "1"):
        time.sleep(time_over_entries)
      directions = gmaps.directions(address,destination,mode=mode,units="metric",departure_time=datetime.datetime.now(),alternatives="true",optimize_waypoints="true")
    i=0
    outputjson.write(json.dumps(directions,sort_keys=True,indent=4)) 
    output.write(",%s" % mode)
    for route in directions:
      output.write(",")
      output.write(str(route['legs'][0]['duration']['value']))
      output.write(",")
      if(mode == 'driving'):
        output.write(str(route['legs'][0]['duration_in_traffic']['value']))
        output.write(',')
      output.write(str(route['legs'][0]['distance']['value']))
      i+=1
      if(i==3):
        break
    if(i<3 and mode == 'driving'):
      output.write(",NULL,NULL,NULL")
      i+=1
      while(i<3):
        output.write(","+"NULL"+",NULL,NULL")
        i+=1
    if(i<3):
      output.write(",NULL,NULL")
      i+=1
      while(i<3):
        output.write(","+"NULL"+",NULL")
        i+=1
    if( i == 0 and mode=='driving'):
      output.write(',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL')
      i=3
    if(i==0):
      output.write(',NULL,NULL,NULL,NULL,NULL,NULL')
      i=3
  #print counter
  output.write("\n")
