#!python3

import requests
import bs4
import re
import pprint
import json

res = requests.get('https://dining.umich.edu/menus-locations/dining-halls/mosher-jordan/')
try:
    res.raise_for_status()
except Exception as exc:
    print("There was a problem: %s" %(exc))

menuDict = {}
itemsList = []
caloriesList = []
proteinList=[]
nutritionalList = []
mosherMenu = bs4.BeautifulSoup(res.text, features = "lxml")

menuFile = open('menuFile.json', 'w')
for item in mosherMenu.find_all('li', class_=re.compile('^trait-')):
    if "item-name" in str(item):

         itemName = item.find(class_='item-name').text
       
         if item.find('tr',class_='portion-calories'):
            itemsList.append(itemName)
            numCalories = item.find('tr',class_='portion-calories').text
            caloriesList.append(numCalories)
            proteinString = item.find('strong' ,string="Protein")
            numProtein = proteinString.next_sibling
            proteinList.append(numProtein)
        

#menuFile.write(str(pprint.pformat(itemsList)))
#menuFile.write(str(pprint.pformat(caloriesList)))




for i in range(len(caloriesList)):
    temp = re.findall(r'\d+', caloriesList[i]) 
    nutritionalList.append(temp)
    temp2 = re.findall(r'\d+', proteinList[i])
    nutritionalList[i].append(temp2[0])

itemsDict = dict(zip(itemsList,nutritionalList))






menu_json = json.dumps(pprint.pformat(itemsDict))
menuFile.write(menu_json)
menuFile.close()