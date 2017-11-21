# Google_Maps_Search
User-friendly and sophisticated Google Maps API searching. Query for thousands of location pairs easily and get all relevant data for any combination of modes of travel (driving,transit,walking,biking) or start/end-times.
# Idea
This repository contains an HTML web interface used to interact with a python script that queries the Google Directions API for directions going from Point A to Point B in all 4 modes of travel (Walking, Transit, Driving, and Biking). The exact specifications of this script are in line with those outlined on the [Directions API Developer's Guide] (https://developers.google.com/maps/documentation/directions/intro "Directions API Developer's Guide")

The python script itself can be executed alone, using the parameter options outlined in the comments of the file, but the HTML web interface ensures that no silly errors are done, and also ensures a number of conditions are met. 

# Input and Output Files
All input files sent via the HTML Interface are saved into the `uploads` directory. All output files are saved in the `outputs` directory. The file that was produced as a result of running the python script is then presented for download via the webpage. Should something go wrong, the file can then be accessed in the outputs directory, along with its corresponding upload file, to determine what went wrong. 

## Input File Format
The python script is supplied an input file which is read. Each line contains a point A and Point B lat and long in the following format:
`POINTALat,POINTALong,POINTBLat,POINTBLong`
The above represents one single line of the file. A space is allowed **after the comma** following `POINTALong`. 

## Output Files
The HTML Interface saves all the output files using the current time and date so as not to repeat any filenames, overwriting old data or causing file errors, and to ensure that it is easy to match up corresponding input and output files. The time the input file was uploaded will match the name of the output file. 

The Python script dynamically determines the headers to be created for each output file based on mode selections. For example, if the only mode you would like to query for is Driving then the header of that output file would be as follows:
`Slat,Slong,Dlat,Dlong,time,mode,d1time,d1traffic_time,d1dist,d2time,d2traffic_time,d2dist,d3time,d3traffic_time,d3dist`
Slat = Point A latitude
Slong = Point A longitude
Dlat = Point B latitude
Dlong = Point B longitude
time = Time that the query for this was sent to google's API
mode = current mode (I.e Driving in this example)
d1time = Time that google says this trip will take for Route 1 of potentially 3 (in seconds)
d1traffic_time = Time that google says this trip will take for Route 1 of potentially 3 **including estimated current traffic levels**
d1dist = Distance in meters for route 1 of potentially 3.
Obviously d2* and d3* is the same as above for Routes 2 and 3
### Explanation of Multiple Routes
For any given point A and point B there is potentially 4 routes that google sends back (Can be obtained by using parameter `alternatives="True"` as shown in Developer's Guide. We are returning at most 3 of those routes. However, there does not always have to be 3 routes, there does not always have to be even 1 route (I.e bad input or maybe the two points don't have roads that connect them according to google). In the case that there is less than 3 routes, the python script dynamically fills the remaining space with `NULL` values. 


