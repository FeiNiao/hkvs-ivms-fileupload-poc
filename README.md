# hkvs-ivms-fileupload-poc

海康威视文件上传检测脚本


# 免责声明
使用本程序请自觉遵守当地法律法规，出现一切后果均与作者无关。

本工具旨在帮助企业快速定位漏洞修复漏洞,仅限授权安全测试使用!

严格遵守《中华人民共和国网络安全法》,禁止未授权非法攻击站点!

由于用户滥用造成的一切后果与作者无关。

切勿用于非法用途，非法使用造成的一切后果由自己承担，与作者无关。

### 食用方法

```
python .\hkvs-ivms-fileupload-poc.py -u http://xx.xx.xx.xx
```

效果图
图放错啦，该图片是实验之前的图片文件名字忘记改了，所以测试脚本还是hkvs-ivms-fileupload-poc.py

![image](https://github.com/FeiNiao/hkvs-ivms-fileupload-poc/assets/66779835/5a563d28-2ad2-4d8d-a44c-1041c1142246)

提示上传附件失败，上传文件不能为空，说明存在漏洞并且可以上传文件

失败提示

![image](https://github.com/FeiNiao/hkvs-ivms-fileupload-poc/assets/66779835/3137c82d-ddf7-4a27-8a56-16bdadb80616)

## 文件上传
验证完成后可以使用getshell脚本测试文件上传
### 食用方法
```
 python .\hkvs-ivms-fileupload-getshell.py -u http://xx.xxx.xx.xx
```
效果图

![image](https://github.com/FeiNiao/hkvs-ivms-fileupload-poc/assets/66779835/9daf337f-c507-4385-a369-6814723541dd)

根据脚本提示访问地址进行查看

![image](https://github.com/FeiNiao/hkvs-ivms-fileupload-poc/assets/66779835/d703fc4d-e2cf-4f9f-aef1-dc1232880d5e)

原创脚本并没有上传webshell，而是使用了`hkvs`字符进行替代，如有需要请自行修改为webshell。
由于用户滥用造成的一切后果与作者无关，切勿用于非法用途，非法使用造成的一切后果由自己承担，与作者无关。
