## INSTALL.md
  
### Setup
* Clone repository from github: https://github.com/lydiengerbretson/emsi_project.git
* Install Python 2.7.6 (or later version)
* Ensure that you have access to this link: https://raw.githubusercontent.com/economicmodeling/api_developer_technical_project/master/data/cities.json
* In your cloned repository, navigate to the directory where the file "api.py" lives
* Open a command console in that directory and type: ./api.py
* The program will output the link that you are accessing
* The program will prompt the user to enter either two commands: POST /rank or GET /city/:cityid
* When you enter GET /city/:cityid (i.e. GET /city/1) and press Enter, the program will output the information for that city ID. Make sure the command format and spacing is correct.
* When you enter POST /rank and press Enter, the program will prompt the user to enter a dictionary of ranks. The program gives an example of the correct format. Make sure the command spacing and format is correct.
* The program is in a loop, so you can continue to enter these commands
* To end the program, type "exit" and then press Enter
* See program_example.JPG in the repository for more details

### Notes
I tried to set up parameters for the GET call, but from my research, I would need to set up an http server to retrieve and post information. In this program, I requested the URL and then parsed and analyzed all the information. It is faster and more efficient with less overhead to grab all the data at once and parse it rather than getting and posting to and from the website.

This is the code I would've used for GET /city/cityID if I requested this information from the server every GET call.

ID_POS = 10

id_num = raw_input()

PARAMS = {'id': int(id_num[ID_POS])}

response = requests.get(url=URL, params=PARAMS)
