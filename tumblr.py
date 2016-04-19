#-*-coding:utf8 -*-
import requests
import sys
from lxml import etree
no = 0
page = 39
#url_bloger	= 'http://onlyecholy.lofter.com/'
url_bloger	= 'http://wanimal1983.tumblr.com/'

#payload = {'page':''}
def download_on_page(page):
	no = 1
#	payload['page'] = str(page)
	html=requests.get(url_bloger+'page/'+str(page)).content
	selector=etree.HTML(html)
	set_urls = selector.xpath("//div[@class='media']/a/img")
	if len(set_urls) ==0:
		sys.exit(0)
	for url in set_urls:
		r = requests.get(url.attrib['src'])
		with open('/home/likex/picture_0/'+str(page)+'_'+str(no),'wb') as f:
				f.write(r.content)
				no=no+1

while 1:
	download_on_page(page)
	page =page+1
