#-*-coding:utf8 -*-

import requests
import sys
from lxml import etree
no = 0
page = 1
#url_bloger	= 'http://onlyecholy.lofter.com/'
#url_bloger	= 'http://wawalrz.lofter.com/'
url_bloger	= 'http://1067328721.lofter.com/'
payload = {'page':''}
def download_on_page(page):
	no = 1
	payload['page'] = str(page)
	html=requests.get(url_bloger,params=payload).content
	selector=etree.HTML(html)
	set_urls = selector.xpath("//div[@class='content']/div[@class='img']/a")
	if len(set_urls) ==0:
		sys.exit(0)
	for url in set_urls:
		html = requests.get(url.attrib['href']).content
		selector = etree.HTML(html)
		img_urls = selector.xpath("//div[@class='img']/a[@class='imgclasstag']/img")
		for img_url in img_urls:
			r = requests.get(img_url.attrib['src'])
			with open('/home/likex/picture_3/'+str(page)+'-'+str(no),'wb') as f:
				f.write(r.content)
				no = no+1

while 1:
	download_on_page(page)
	page =page+1
