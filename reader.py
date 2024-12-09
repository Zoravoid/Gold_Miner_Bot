from bs4 import BeautifulSoup

with open('directory', 'r') as f:
    data = f.read()

Bs_data = BeautifulSoup(data, "xml")

b_unpaid = Bs_data.find_all('unpaid')

#do smth with unpaid variable and also get the right tag for the uppaid variable

#get the names of the unpaid members here 
b_member = Bs_data.find()