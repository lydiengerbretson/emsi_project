#!/usr/bin/python

import requests
import json
import ast

# This function uses the raw input from the user (which is the city ID number). If it is a valid city ID number, then the function is hardcoded to print out the correct json object for that city ID number to the console.
def get_output(info):
   # if the user input is too long, something must be wrong 
   # ID_POS is position 10 of the raw user input, which is the city ID number. i.e.: GET /city/1
   if len(info) != ID_POS+1:
       print "Error: city ID is between 1 and 8."
       return
   #TODO: Design this portion of the program as if there were 300 cities!
   if "1" == info[ID_POS]:
      print(data[0])
   elif "2" == info[ID_POS]:
      print(data[1])
   elif "3" == info[ID_POS]:
      print(data[2])
   elif "4" == info[ID_POS]:
      print(data[3])
   elif "5" == info[ID_POS]:
      print(data[4])
   elif "6" == info[ID_POS]:
      print(data[5])
   elif "7" == info[ID_POS]:
      print(data[6])
   elif "8" == info[ID_POS]:
      print(data[7])
   else:
      print "Error: city ID is between 1 and 8."

# This function asks for a dictionary formatted raw input, then using this raw input, iterates through the json object and calculates the overall score of each city in the json object
def post_output(info):
    print "Please enter with dictionary format, listing appropriate weights:"
    print 	"i.e.  { \"walkability\": 1.3 , \"job_growth\": 3.1, \"green_space\": 1.2, \"taxes\": 0.8 }" 
    # raw input for dictionary
    a = raw_input("\"weights\": \n")
	# change input to a dict
    try:
        d = ast.literal_eval(a)
    except: 
	    print "Incorrect dictionary formatting."

	# for loop that iterates through the json object, calculating the overall score for each item in json object
    for x in range(0, len(data)):
        try:
            overall_score = (d['walkability']*data[x]["scores"]["walkability"]) + (d['job_growth'] * data[x]["scores"]["job_growth"]) + (d['green_space'] * data[x]["scores"]["green_space"]) + (d['taxes'] * data[x]["scores"]["taxes"])
            print(data[x])
            print "overall_score = " + str(overall_score)
        except:
            print "Program could not retrieve overall score."
            break
	

# This is the URL that accesses the raw JSON content on github
URL = "https://raw.githubusercontent.com/economicmodeling/api_developer_technical_project/master/data/cities.json"

# I tried to set up parameters for the GET call, but I believe https will not allow this to happen. From my research, I would need to set up an http server to retrieve information, and I did not want to do that for this project. 
# Setting up a server would require EMSI interviewers to also set up a server, meaning extra work. Instead, I requested for the URL in this program and then parsed and analyzed the information.

# This is the code I would've used if the server was working and if I could access individual parts of the json object from the server
#ID_POS = 10
#id_num = raw_input()
#PARAMS = {'id': int(id_num[ID_POS])}
#response = requests.get(url=URL, params=PARAMS)

response = requests.get(URL)

data = response.json()
print(response.url)
ID_POS = 10

while(1):
   print "Format: GET /city/:cityid"
   print "Format: POST /rank"
   info = raw_input()
   if "GET" in info:
      get_output(info)
   elif "POST" in info:
      print "POST"
      post_output(info)
   elif "exit" in info:
      break;
   else:
      print "Incorrect formatting. Try again."