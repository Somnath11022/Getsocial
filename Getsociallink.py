import requests
from bs4 import BeautifulSoup

url = input("Enter website : ")
r = requests.get(url)
social_sites = ['facebook.com','linkedin.com']
social_sites_present = []
soup = BeautifulSoup(r.content, 'html5lib')
all_links = soup.find_all('a', href = True)
for sm_site in social_sites:
    for link in all_links:
        if sm_site in link.attrs['href']:
            social_sites_present.append(link.attrs['href'])

print('Social links   :  ','\n',social_sites_present[0],'\n', social_sites_present[1])