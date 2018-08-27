import requests

url = 'http://app.avgfytzba.com//mov/browse?movId=103223&version=v2 '

headers = {
    'host': "app.avgfytzba.com",
    'accept-encoding': "gzip, deflate",
    'cookie': "JSESSIONID=393C00C35D078D1F24FD1E12E3DF789A; __cfduid=d9def8ed8fb74e69c07e35f3d0e8f7a771532102629",
    'connection': "keep-alive",
    'accept': "*/*",
    'version': "106002101",
    'user-agent': "huang gua shi pin/1.0.6 (iPhone; iOS 11.3.1; Scale/2.00)",
    'accept-language': "zh-Hans-CN;q=1, en-US;q=0.9",
    'seq': "052798cbed3g1ef274ff41C30mC30qDZKtDpa",
    'cache-control': "no-cache",
    }

a= requests.get(url,headers = headers).text
print(a)



