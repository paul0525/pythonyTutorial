#coding=utf-8

import requests
import base64
import json
from Crypto.Cipher import AES
from Crypto.Hash import SHA256



BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 

#加sign
def sign(context):
    signhelper = SHA256.new()
    signhelper.update(context.encode('utf-8'))
    return signhelper.hexdigest()

def aesEncrypt(context):
    cipher = AES.new(key, AES.MODE_ECB)
    return base64.encodestring(cipher.encrypt(pad(context)))


#注意下key，此key用于拼sign
key1="pFNPY8Z3nvVAvOOQ5ImqBu46h1Y3WuNg"
#转换后的key,用转换后的key加密
key=base64.b64decode("gESSC2jAeBwtcHH2Rm3Qhg==")

insId = u""
operId = u""
url = ""

sendData={}
sendData['insId']=insId
sendData['operId']=operId
sendData['version']=u'2.0'
sendData['reqTime']=u'20171207101010'
sendData['reqSerialNo']=u'201611178910002'
sendData['cardNo']=aesEncrypt("6225750009602935")
sendData['resv']=u''
sendData['resv2']=u''


#生成请求的sign串,按字典key排序并加上key1
signStr=u""
for item in sorted(sendData.keys()):
    signStr += sendData[item]
signStr+=key1
print '请求sign串:', signStr

sendData['signature']=sign(signStr)
print '请求数据:',sendData

#发送请求
r = requests.post(url, data=sendData)
print(r.status_code, r.reason)
print '响应内容：',r.text

rspDict = json.loads(r.text, encoding='utf-8')
rspSign = rspDict['signature']


#组装响应的sign串
rspDict.pop('signature')
signStr2=u""
for item in sorted(rspDict.keys()):
    signStr2 += rspDict[item]
signStr2+=key1

mySign=sign(signStr2)


if mySign == rspSign:
    print '验签通过'
    print '响应结果:',rspDict
else:
    print '验签不通过'