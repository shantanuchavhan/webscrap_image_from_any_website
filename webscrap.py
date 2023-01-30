import requests
from bs4 import BeautifulSoup
import urllib.request
import os

directory =input('directory name please: ')
parent_dir = "C:/Users/shant/projects/project"
path = os.path.join(parent_dir, directory)  
os.makedirs(path) 


def getdata(url):
	r = requests.get(url)
	return r.text
def download_image(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)
	
def scrap_images(link):

    htmldata = getdata(link)
    soup = BeautifulSoup(htmldata, 'html.parser')
    for item in soup.find_all('img'):
        
        imglink=item['src']
        image_name=imglink.rsplit('/', 1)[1]
        url = imglink
        file_name = f"{image_name}"
        download_image(url, f'{directory}/', file_name)
        
        #links.append(f'{imglink}')
url=input(f'{https://www.swiggy.com/}')
scrap_images(url)



        


    







