import requests
import json
#口碑楼盘接口
base_url="http://api.zhuge.com//home/v1/Appindex/showHighOpinion"
# #发送get请求
# r=requests.get(base_url+'get')
# print(r.status_code)
# #发送post请求
# r=requests.post(base_url+'post')
# print(r.status_code)
#get请求传递参数
param_data={'cityid':'1','paltformType':'3'}
r=requests.get(base_url+'/post',params=param_data)
# r.content=json.dumps(r)
print (r.url)
print (r.status_code)
#post请求传递参数


