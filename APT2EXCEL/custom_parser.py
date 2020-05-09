import urllib.request
from bs4 import BeautifulSoup
import json


# get website content
def parse_group_details(target,starts_with_letter):
	req = urllib.request.Request(url=target)
	f = urllib.request.urlopen(req)
	xhtml = f.read().decode('utf-8')
	soup = BeautifulSoup(xhtml,features="lxml")
	table = soup.find_all("table")
	table = table[1] #Pick the 2nd table from the page
	result_dict={}
	if table:
		for table_row in table.findAll('tr'):
			columns = table_row.findAll('td')
			output_row = []
			temp_list=[]
			for column in columns:
				temp_list.append((column.text).strip())
			if len(temp_list) >= 2 and temp_list[1].startswith(starts_with_letter) :
				result_dict[temp_list[1]]=temp_list[3]
	return result_dict

def get_group_tech_procedure(tech_id):
	url = 'https://attack.mitre.org/groups/G0050/'
	tech_procedure=parse_group_details(url,'T')
	tech_procedure=tech_procedure[tech_id]
	return tech_procedure


# get website content
def get_details(target,starts_with_letter):
	req = urllib.request.Request(url=target)
	f = urllib.request.urlopen(req)
	xhtml = f.read().decode('utf-8')
	soup = BeautifulSoup(xhtml,features="lxml")
	table = soup.find("table")
	result_dict={}
	if table:
		for table_row in table.findAll('tr'):
			columns = table_row.findAll('td')
			output_row = []
			temp_list=[]
			for column in columns:
				temp_list.append((column.text).strip())
			if len(temp_list) >= 2 and temp_list[0].startswith(starts_with_letter) :
				result_dict[temp_list[0]]=temp_list[1]
	return result_dict

#get all the techniques
def get_techniques():
	url = 'https://attack.mitre.org/techniques/enterprise/'
	techniques_dict=get_details(url,'T')
	for k,v in techniques_dict.items():
		print(k,v)
	return len(techniques_dict),techniques_dict

#get all the tactics
def get_tactics():
	url = 'https://attack.mitre.org/tactics/enterprise/'
	tactics_dict=get_details(url,'T')
	for k,v in tactics_dict.items():
		print(k,v)
	return len(tactics_dict),tactics_dict

#Get all the techniques mapped to respective tactics
def get_tactic_techniques_mapping():
	tactic_technique_dict={}
	for k,v in tactics_dict.items():
		url = 'https://attack.mitre.org/tactics/'+k+'/'
		temp_dict=get_details(url,'T')
		tactic_technique_dict[k]=[*temp_dict] #Convert the key values in to list and store it in dictonary as value
	for k,v in tactic_technique_dict.items():
		print(k,v)
	return tactic_technique_dict

#Get all the techniques
def get_tech_name(techID):
	url = 'https://attack.mitre.org/techniques/enterprise/'
	techniques_dict=get_details(url,'T')
	return techniques_dict[techID]

#Get all the techniques
def get_tatic_id(tactic_name):
	url = 'https://attack.mitre.org/tactics/enterprise/'
	tactic_dict=get_details(url,'T')
	for k,v in tactic_dict.items():
		if tactic_name.lower() in v.lower():
			return k




#Parse the downloaded GROUP File and return result as dict
def parse_group_json(data):
	result_dict={}
	group_name=data['name']
	for techniques in  data['techniques']:
		tactic=techniques['tactic']
		techniqueID=techniques['techniqueID']
		if tactic in result_dict:
			value_list=result_dict[tactic]
		else:
			value_list=[]
		value_list.append(techniqueID)
		result_dict[tactic]=value_list
	return group_name,result_dict


#Read the file and store the result in variable
def json_file_load(file_name):
	#Read the file and store the value in variable
	with open(file_name) as datafile:    
		data = json.load(datafile)
	group_name,result_dict=parse_group_json(data)
	return group_name,result_dict 
