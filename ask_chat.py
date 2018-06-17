import requests
import json
from tasks import add, add_cache_1, add_cache_2, add_cache_3, add_cache_4, add_cache_5


fp = open('chat_question.txt', 'r', encoding="utf-8")
line = fp.read()
question_list = []
question_list = line.split(',')
fp.close()


url = "http://10.161.4.82:30394/v1/ai/chatbot/addchatcache/mibo_id"

headers = {"content-type": "application/json", "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwOi8vdWF0LWFwaS5udXdhcm9ib3RpY3MuY29tIiwic3ViIjoiYXV0aC51YXQubnV3YXJvYm90aWNzfDE3MjU2NjQ4OTc1MSIsImF1ZCI6IkZEN0M3NzIxLTNFMDQtNDY2RC1BRDY1LUE2QjZEQTdDNjVFNiIsImlhdCI6MTUyMzU5MDA0NCwiZXhwIjoxNTMxMzY2MDQ0LCJqdGkiOiIzNjA3MzQ0Yy05ZDcwLTQ0YmMtOTc0Ny1jMmM1NWU2NDhiYzgiLCJjb250ZXh0Ijp7InR5cGUiOiJhY2Nlc3MiLCJwcm92aWRlciI6Im51d2F8Y2hlbi5qb2huQG51d2Fyb2JvdGljcy5jb20ifSwic2NvcGUiOiJwcm9maWxlIGF1dGggYXV0aF9yZWZyZXNoLmdldCBvdGEgb3RhLmdldCJ9.dNk89PCOmBGi5XVGwt6HAbZoBPh5CfPRVqtyLm3l7zgpl34rBqURullnP5FPkRKLkorBIEg89CvJpkfJUbk9f5avPRIO3lS6KZqi9WUWZNIfYEZHE1sVaY0Jfh2mUXhs26I1XLkHVI8M0X1bwbuy1LsZfbqyl2LtV2-9hv11b9Wh9x7aRXSjyRJ_efvDfwfnOvi1_3Hvi8fkACycOFMGXi20FtXsctG1ONoLR-NaMT2W2viM-baUIT4ytcUphTsV0YkbnAQF9icBTHzESQWWFnjBXXuOBphOcEx1kr8VjiIMIs3oe8SBdUcwQYFXgHkNpZ4vnqfVEAw0qXSmxQQK5g"}


for i in range(len(question_list)-1):

   #add_cache_1.apply_async((question_list, url, headers), queue='ask1')
   #add_cache_2.apply_async((question_list, url, headers), queue='ask2')
   #add_cache_3.apply_async((question_list, url, headers), queue='ask3')
   #add_cache_4.apply_async((question_list, url, headers), queue='ask4')
   add_cache_5.apply_async((question_list, url, headers), queue='ask5')
