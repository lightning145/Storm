import requests
import json

url = "https://epassport.diditaxi.com.cn/passport/login/v5/codeMT"

headers = {'Host': 'epassport.diditaxi.com.cn', 'Connection': 'keep-alive', 'Mpxlogin-Ver': '5.5.1', 'content-type': 'application/x-www-form-urlencoded', 'secdd-authentication': '49afb436f1b4de01ccd95876718546a2ee095f5762fd80e5b45c6017a80b6d73e09ebd0ba9c3ef1cd29888d9ca528e19bf0e73cf9401000001000000', 'secdd-challenge': '3|2.0.11||||||', 'Accept-Encoding': 'gzip,compress,br,deflate', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.56(0x1800382d) NetType/WIFI Language/zh_CN', 'Referer': 'https://servicewechat.com/wx9e9b87595c41dbb7/491/page-frame.html'}

phonenumber = input("输入电话号码：")

data = {
    "api_version": "1.0.1",
    "appid": 35011,
    "role": 1,
    "device_name": "iPhone XS Max China-exclusive<iPhone11,6>",
    "sec_session_id": "BxdYpEmKtRAjVQKCUbzheJtWBkjiT5ZYQ1S4k8ZpEQEbICRRc7Iom6gG3EFtcOYj",
    "policy_id_list": [50008256],
    "policy_name_list": [],
    "ddfp": "",
    "lang": "zh-CN",
    "wsgenv": "",
    "cell": phonenumber,
    "country_calling_code": "+86",
    "code_type": 1,
    "scene": 1
}

payload = {
    "q": json.dumps(data, ensure_ascii=False)
}

response = requests.post(url, headers=headers, data = payload)

print(response.status_code)
print(response.text)
