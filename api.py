#!/usr/bin/python

import requests
import json
import ast
import sys

# author: Lydia Engerbretson
# date: December 1, 2017
# project: api_developer_technical_project: https://github.com/economicmodeling/api_developer_technical_project

# This function uses the raw input from the user (which is the city ID number). If it is a valid city ID number, then the function is hardcoded to print out the correct json object for that city ID number to the console.
def get_output(info):
   # if the user input is too long, something must be wrong 
   # ID_POS is position 10 of the raw user input, which is the city ID number. i.e.: GET /city/1
   if len(info) != ID_POS+1:
       print "Error: Format is incorrect."
       return
   # list of city ids, could be filled in all the way up to 300
   city_ids = [ '1', '2', '3', '4', '5', '6', '7', '8']
   for x in range(0, len(city_ids)):
       if info[ID_POS] == city_ids[x]:
	       print data[x]

# This function asks for a dictionary formatted raw input, then using this raw input, iterates through the json object and calculates the overall score of each city in the json object
def post_output(info):
    print "Please enter with dictionary format, listing appropriate weights:"
    print 	"i.e.  { \"walkability\": 1.3 , \"job_growth\": 3.1, \"green_space\": 1.2, \"taxes\": 0.8 }" 
    # raw input for dictionary
    a = raw_input("\"weights\": \n")
	# change input to a dictionary
    try:
        d = ast.literal_eval(a)
    except: 
	    print "Incorrect dictionary formatting."

	# for loop that iterates through the json object, calculating the overall score for each city in json object
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

try:
    # Get the URL and store code in the response 
    response = requests.get(URL)
	# Store JSON objects in the variable data
    data = response.json()
    print(response.url)
    working_url = True
except:
    print "Network or URL error."
    working_url = False

# ID_POS is position 10 of the raw user input, which is the city ID number. i.e.: GET /city/1
ID_POS = 10

while(working_url):
   # Output to the screen for correct formatting
   print "Format: GET /city/:cityid"
   print "Format: POST /rank"
   # RAw user input, which is either GET /city/:cityid or POST /rank
   info = raw_input()
   if "GET" in info:
      # Calls get_output function which outputs the city's information
      get_output(info)
   elif "POST" in info:
	  # Calls post_output function which further prompts the user to input a dictionary of ranks
      post_output(info)
   elif "exit" in info:
      # If user enters "exit", it ends the program
      break;
   else:
      # Any other words besides "POST", "GET", and "exit" will output this message
      print "Incorrect formatting. Try again."