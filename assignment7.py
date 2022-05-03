import math
from pyparsing import Regex
import requests
import re

def main():

    url = "https://valorant-api.com/v1/agents/dade69b4-4f5a-8528-247b-219e5a1facd6"
    response = requests.get(url).json()
    
    char_name = ((response['data'])['displayName'])

    #Dive into specific parts of website
    data = ((response['data'])['abilities'])
    
    f = open("valorantFade.txt", "w")

    print("Character name: "+ char_name + '\n')

    thisdict = {}

    #First Traverse through data
    data1 = (data[0])
    ability_name = (data1['slot']) #Finding Ability
    print("Ability: " + ability_name, end=' | ')
    data2 = (data1['displayName']) #Finding Ability Name
    print("Ability Name: " + data2, end=' | ')
    data3 = (data1['description']) #Finding Description of Ability
    print("Description: " + data3 + '\n')

    #Traverse through found data and pinpoint exact info
    regex = re.compile('^EQUIP[^.]+') #Finding All sentences with Equip in it
    match_object = regex.findall(data3)
    if len(match_object) != 0:
        for word in match_object: 
            thisdict["Equip Sentence"] = word #Writing information found to the dictionary

    f.write("Category : Data" + '\n') #Header
    f.write(str(thisdict)) #Adding Dictionary to File
        
    f = open("valorantFade.txt", "r")
    print(f.read())

main()

