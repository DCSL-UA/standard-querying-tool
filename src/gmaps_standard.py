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
x=1
gmaps = ""
global directions11
directions11 = ""
def client(API_KEY_INPUT):
  global x
  global gmaps
  try:
    gmaps = googlemaps.Client(key = str(API_KEY_INPUT))
  except:
    print "API Key " + str(x-1) + " Was Full or invalid.<br>"
    x += 1
    if (got_more_keys(KEYS,x) != False):      
      client(got_more_keys(KEYS,x))
    else:
      print "No More keys to run on. None of the keys provided worked."
      exit()
def finish_line(array_size,array_index,array,output):
  while(array_index != array_size):
    if(modes_to_run[array_index] == 'driving'):
      output.write(",driving,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL")
    else:
      output.write(',' + modes_to_run[array_index] + ",NULL,NULL,NULL,NULL,NULL,NULL")
    array_index += 1

def try_except(gmaps12,address,destination,mode,modes_to_run,output,KEYS,a):
  global gmaps
  global x
  try:
    global directions11
    directions11 = gmaps.directions(address,destination,mode=mode,units="metric",departure_time="now",alternatives="true")
  except googlemaps.exceptions.ApiError as e:
    x += 1
    print "Key " + str(x-2) + " Has filled up or another error has occured.<br>\n"
    if(got_more_keys(KEYS,x) != False):
      client(got_more_keys(KEYS,x))
      try_except(gmaps,address,destination,mode,modes_to_run,output,KEYS,a)
    else:
      print "Key Has filled up or another error has occured. Any partial data from google can be downloaded below.<br>\n"
      finish_line(len(modes_to_run),modes_to_run.index(mode),modes_to_run,output)
      exit()
  except Exception as e:
    x += 1
    print "Key " + str(x-2) + " Has filled up or another error has occured.<br>\n"
    if(got_more_keys(KEYS,x) != False):
      client(got_more_keys(KEYS,x))
      try_except(gmaps,address,destination,mode,modes_to_run,output,KEYS,a)
    else:
      print "Key " + str(x-1) + " Has filled up or another error has occured. Any partial data from google can be downloaded below.<br>\n"
      finish_line(len(modes_to_run),modes_to_run.index(mode),modes_to_run,output)
      exit()
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
def get_seconds(t1,t2,Entry_count,mode_count):
  h1, m1, s1 = t1.hour, t1.minute, t1.second
  h2, m2, s2 = t2.hour, t2.minute, t2.second
  t1_secs = s1 + 60 * (m1 + 60*h1)
  t2_secs = s2 + 60 * (m2 + 60*h2)
  return((t2_secs/Entry_count)/mode_count)

def got_more_keys(KEYS,count):
  global x
  if(KEYS[count-1] == str("0") or x > len(KEYS)-1):
    return False
  return KEYS[count-1]

def check_dest_space(line):
  if(line.strip().split(',')[2][0] == ' '):
    return line.strip().split(",")[2][1:] + "," +line.strip().split(",")[3]
  else:
    return line.strip().split(",")[2] + "," +line.strip().split(",")[3]

if (sys.argv[1]=="-help"):
   print "To Run, execute as  such: \"python gmaps.py <input_file_name> <output_file_name>\""
   print "\n"
   print "Output File defaults to stdout if not specified.\n"
   print "Input File Format = <lat,long,lat,long NEWLINE>No spaces until end of second pair"
   exit(-1)
output = open(sys.argv[2],"w+")
#print sys.argv[1]

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

key_count = 0

KEYS=[API_KEY_INPUT,KEY2,KEY3,KEY4,KEY5]
for key in KEYS:
  if(key != "0"):
    key_count += 1
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
counter=0
y=0
time_stretch = sys.argv[15]
client(API_KEY_INPUT)
if (str(time_stretch) == "1"):
    start_time = "0:00:00"
    end_time = sys.argv[14]
    time_stretch = sys.argv[15]
    time_over_entries = get_seconds(datetime.datetime.strptime(start_time,'%H:%M:%S').time(),datetime.datetime.strptime(end_time,'%H:%M:%S').time(),file_len(str(sys.argv[1])),mode_count)
    print "Time between Runs: " + str(time_over_entries)
else:
    time_stretch = 0
for line in inputfile:
  
  address = line.strip().split(",")[0]+ ","+line.strip().split(",")[1]
  destination = check_dest_space(line)
  output.write(address+","+destination+",")
  output.write(str(datetime.datetime.now().strftime("%H:%M:%S")))
  iterate_counter=0
  for mode in modes_to_run:
    counter+=1
    if(time_stretch == 1):
      time.sleep(time_over_entries)
    try_except(gmaps,address,destination,mode,modes_to_run,output,KEYS,x)
    i=0
    #print directions
    output.write(",%s" % mode)
    iterate_counter+=1
    for route in directions11:
      if(i<3):
        output.write(",")
        output.write(str(directions11[i]['legs'][0]['duration']['value']))
        output.write(",")
        if(mode=='driving'):
          if "duration_in_traffic" in directions11[i]['legs'][0].keys():
            output.write(str(directions11[i]['legs'][0]['duration_in_traffic']['value']))
            output.write(',')
          else:
            output.write(str(directions11[i]['legs'][0]['duration']['value']))
            output.write(",")
        output.write(str(directions11[i]['legs'][0]['distance']['value']))
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
  output.write("\n")
output.close()
inputfile.close()
print "Total runs spread over " + str(key_count) + " key(s) was " + str(counter) + ".\n"