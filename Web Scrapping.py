import csv
from bs4 import BeautifulSoup
import requests

url = "https://zeplin.io/pricing/"
h = requests.get(url)

s = BeautifulSoup(h.content, 'html5lib')
plan_amt = []
features =[]
is_present=[]
elements = s.find('body', attrs={'class':'id-7b3807bf-ce9d-4633-a915-cb05c5a79651 zp-antialiased zp-text-18 zp-leading-21'})
for element in elements.find_all_next('div', attrs = {'class':'zp-h-167 zp-pt-24 zp-border-b zp-border-gray-karl zp--mb-1'}):
    price={}
    price['plan_amt']= element.div.text
    plan_amt.append(price)
for element in elements.find_all_next('li', attrs = {'class':'zp-h-35 zp-flex zp-items-center zp-pr-12 zp-pl-24 zp-relative zp-text-gray-clooney'}):
    feature={}
    feature['features']= element.span.text
    features.append(feature)
for element in elements.find_all_next('div', attrs = {'class':'zp-pt-57'}):
    yes_no={}
    if (element.span == None):
        yes_no['is_present'] = "not present"
    else:
        yes_no['is_present']= element.span.text

    
    is_present.append(yes_no)

filename = "data.csv"
with open(filename, 'w+', encoding="utf-8") as f:
    w = csv.DictWriter(f,['features', 'plan_amt', 'is_present'])
    w.writeheader()
    for feature in features:
#        w.writerow(yes_no)
        for price in plan_amt:
           
                w.writerow(feature)            
                w.writerow(price)            
                #w.writerow(yes_no)             
    for yes_no in is_present:
        w.writerow(yes_no)    