# -*-coding:utf-8-*-
# you should change password string
from lxml import etree
import os

import requests
class LOGIN_IN:
    def __init__(self):
        self.url = 'http://210.28.186.100/moodle/login/index.php'
        self.course_url = 'http://210.28.186.100/moodle/course/view.php'
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36' }
        '''private information'''
        self.form_data = {'username': 'nj_kexin',
                            'password': 'xxxxxx',
                          }

    def login(self):
        no = 1
        s = requests.session()
        response = s.post(self.url, data=self.form_data, headers=self.header)
        # print response.status_code
        response = s.get(self.course_url,params = {'id':'15'})
        print '---------------------'
        # print response.status_code
        # print response.content
        html = etree.HTML(response.content.lower().decode('utf-8'))
        parts = html.xpath('//*[@class="section main clearfix"]//*[@class="activity resource modtype_resource "]//a/@href')
        for part in parts:
            response = s.get(part)
            print response.status_code
            html = etree.HTML(response.content.decode('utf-8'))
            text = html.xpath('//*[@class="region-content"]/h2')[0].text
            print text
            contents = html.xpath('//*[@class="resourceworkaround"]//a/@href')
        # print content[0]
            for content in contents:
                print content
                response = s.get(content)
                with open( "./4/no."+str(no)+"_"+text+".swf","wb") as save:
                    save.write(response.content)
            no =no+1
def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        print path+ " create successfully"
        os.makedirs( path )
        return True
    else:
        print path + " existed!!!"

a = LOGIN_IN()
a.login()

