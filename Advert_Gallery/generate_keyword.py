import json
import os
import re
import pandas as pd
if not os.path.exists("keyword.json"):
    open("keyword.json",'w').close()
    
with open("keyword.json",'r') as f:
    if os.path.getsize("keyword.json") > 0:
        keywords = json.load(f)
    else:
        keywords = {}
    
# Was done to get name of the brands-----------------------------------

# with open("brand.txt",'r') as f:
#     brand = f.readlines()
# brand = [x.strip() for x in brand]
# brands_name = []
# for b in brand:
#     if '(' in b:
#         temp = b.split('(')        
#         if temp[0].strip() not in keywords:
#             keywords[temp[0].strip()] = [temp[1][:temp[1].rfind(')')]]
#         brands_name.append(temp[0].strip())
            
# print(keywords)
# with open('keyword.json','w') as f:
#     json.dump(keywords,f,indent=4)

    
# -----------------------------------------------------------------
# Done to get final csv file
with open('brands_link.txt','r') as f:
    links = f.readlines()
links = [x.strip() for x in links]

Keywords = pd.DataFrame({'brand_name':keywords.keys(),'brand_link':links,'#_of_images':[x[0] for x in keywords.values()]})
        
with open('keyword.csv','w') as f:
    pd.DataFrame.to_csv(Keywords,'keyword.csv')