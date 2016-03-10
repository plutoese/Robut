# coding=UTF-8

import random
import json
from libs.file.class_Excel import Excel
from applications.collegeAdmission.class_ceespider import CEESpider

# 0. Initial configuration
proxy_checked_list = ['58.20.234.243:8000','58.20.242.85:8000',
                      '110.52.232.56:8000','110.52.232.56:80',
                      '58.20.232.239:8000','58.246.242.154:8080',
                      '58.20.232.239:8000','110.52.232.75:8000',
                      '60.13.74.184:81','110.52.232.60:8000',
                      '58.247.30.222:8080','58.22.86.44:8000']

proxy_checked_list = ['58.252.2.5:8000', '61.179.110.8:8081', '58.252.8.25:8000', '1.197.14.102:8000', '111.12.107.19:80', '1.193.162.123:8000']

regions = ['安徽','北京','重庆','福建','广东','广西','甘肃','贵州','河北','河南',
           '湖南','湖北','海南','黑龙江','吉林','江苏','江西','辽宁','内蒙古',
           '宁夏','青海','上海','四川','山西','山东','陕西','天津','新疆','西藏','云南','浙江']
subject = ['文科','理科']

college_rate_file = r'E:\gitrobot\files\college\rating\college_rating.xlsx'
mexcel = Excel(college_rate_file)
mdata = mexcel.read()
universities = [item[1] for item in mdata[2:]]

result = []

# 1. 开始抓取

college = universities[1]
spider = CEESpider(proxy=proxy_checked_list[random.randint(0,len(proxy_checked_list)-1)])
for region in regions[2:]:
    print(region)
    result = []
    for sub in subject:
        print(sub)
        spider.select_region(region)
        spider.select_subject(sub)
        spider.set_college(college)
        spider.do_search()
        spider.get_result_and_more()
        result.extend(spider.colleges)

    file_name = ''.join(['E:/gitrobot/files/college/exam/',college,'_',region,'.txt'])
    json.dump(result, fp=open(file_name,'w'))

spider.close()

'''
file = ''.join(['E:/gitrobot/files/college/exam/','北京大学','.txt'])
F = json.load(fp=open(file,'r'))
for item in F:
    print(item)
print(len(F))'''