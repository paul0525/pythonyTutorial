#coding=utf-8

from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import AES, PKCS1_OAEP, PKCS1_v1_5
from Cryptodome.Hash import SHA1
from Cryptodome.Signature import PKCS1_v1_5 as PKCS1_v1_5_sign
import requests
import base64
import json


def encrypt(pub_key_str, msg, length=245):
    recipient_key = RSA.import_key(pub_key_str)
    cipher_rsa = PKCS1_v1_5.new(recipient_key)
    res = []
    for i in range(0, len(msg), length):
        res.append(cipher_rsa.encrypt(msg[i:i+length]))
    encrypt_str ="".join(res)
    return base64.encodestring( encrypt_str ).replace("\n","")
    
def signData(priKey,data):
    recipient_key = RSA.import_key(priKey)
    signObj = PKCS1_v1_5_sign.new(recipient_key)
    print signObj.can_sign()
    h = SHA1.new(data)
    signStr = signObj.sign(h)
    return base64.encodestring( signStr )

def verifySign(priKey,data,signature):
    recipient_key = RSA.import_key(priKey)
    signObj = PKCS1_v1_5_sign.new(recipient_key)
    return signObj.verify(SHA1.new(data), base64.decodestring(signature))
    
    
def decrypt(priv_key_str, msg, length=256):
    private_key = RSA.import_key( priv_key_str )
    cipher_rsa = PKCS1_v1_5.new(private_key)
    msg1 = base64.decodestring(msg)
    res=[]
    for i in range(0, len(msg1), length):
        res.append(cipher_rsa.decrypt(msg1[i:i+length],""))
    return "".join(res)


private_key="-----BEGIN RSA PUBLIC KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDiza6lqV92iEmx\nGEyFjJXiHoKlxfCl+/yyi4MD22r6mJvDscIA5FufYicASO96GB28dBDvcpigxyPs\nvBQVpwZHv0PXi896S1clnwKFxVVyl2JlzI44p3ZPE+PgZcCLsfxoclKJw7ppfVPO\ntnmRybct39L0STQJO4MjqGfGoVSP7i2hi/H7ZBrjTmAcEldJ8IHYaS8ashPy8f3C\nmWlGaqyikQ05V6VpUi4NW1BidKjSvXPXwMFwUaIGywkuh8xW3Oi12GS2R7dwIb5w\n25PKGcjtE47M7afgpFaM4xVllbAGtjfenCwpFHfFa7yx9so8jA/iRpDf6UYPSkbZ\n+TWE+lJhAgMBAAECggEAFEh6tvwHuo0Dsh/PMB5bhSZfXr3uAJohhkItzFmCHrkp\nLP4nsHa7ruxTOpZLPGsNtb3XieKAvdgxYUmMrkcKq73yLkOloXU9bPLkgdwdASuC\ntEHv8icf0ICh336aEqQvQ5P9x65GbIq1xQXSp3QXurWKoygszCqTVswHw97HtjtW\nkmtoZsIT6cLsF/A9ZF9Ao2qFQ3DANmr25JPZTvcds2wj36Uaa4e5o6CXNrOqLu1G\n7BLANE9nUGCn0x0wd0x9u2Zw/yl+3o4uBc9EuW4qp5mF5BTNFS49ZTvavW9Jlncb\nAIVLqOI5xfXyrrUhZGKGGlPdEI0dnNp3mSIYpUOzcQKBgQD/w0PRy18qsAyPqACo\nqC9Gy5d+8vmEg/f7AEDAscesfkyHKaxSMue9p1JowqY2WdG/KiYxMyhEa8WBouDM\nCF4o3zdmo1TwuuhuunvYajcgccMroHTgmsWNzuyecSzRiGfps+gdVOJ6YRuqIJiQ\nNLHWBxwv1iepp0NH7HjPMZw2BQKBgQDjA4pZqUswELbsPTG6T5xowJfT+SiywxgB\nHpAioGlQ1gvcEtvZXYugmrN5+nHaiFGzqIH11SLq6kysSgvqwHRPEKuLnB8FbZbC\nG2PFTYBgrzJFfVWQ+zWiuJRR8kSomtdkVAKgtRnk7HiUAKAiHbIFOt3heobEz3Rk\nD6C7Q8JdrQKBgH2QsQgbr2I2wkP4+DHVODiqlXr28PdVDvcEvcWcwmn2K74kAHzu\njwV2UygpgA6o9CfFGrEG65sDyhiGDZU9+nRYekuCnp39NUW/ejPamavtDiOqCBeJ\nBLpFP7fd2mIYdOOwtqFH3lS0vi89B4msxS5NmVIG8rwA6TAzcXBPa+C9AoGAJC4z\nRZj6t71iOgKCw2vexL81M355Yww+7ia92Bby0gRbPYbv7RPApichxaYJsUeapeSM\nWe7PMtuGvsrKXW6w2s0QWh7Wvtm5dlRBMXfppv8lJvgTxBiVcsqyMOFI2gpbm8zb\n4lsatmaNzSDQZL+Q2M6KAF6zzfg2V6A6AL6K4r0CgYEA7EPu0Y1BMDLoFIN+Y44G\nPJqS5ti3xSd66ukupaKp2NHjjCbfZTq2nkCzx0965jEA51bbxaAOy3CK12mtIueN\nNCYV3XSFIvAWMB8whUva4JoixXUFPnc8HWj1FO5LEb5F6P6J1E57MdaH54C5bAID\nlDm7JpsIEgsiJrfNfFQ0t9E\=\n-----END RSA PUBLIC KEY-----"
public_key="-----BEGIN RSA PRIVATE KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA4s2upalfdohJsRhMhYyV\n4h6CpcXwpfv8souDA9tq+pibw7HCAORbn2InAEjvehgdvHQQ73KYoMcj7LwUFacG\nR79D14vPektXJZ8ChcVVcpdiZcyOOKd2TxPj4GXAi7H8aHJSicO6aX1TzrZ5kcm3\nLd/S9Ek0CTuDI6hnxqFUj+4toYvx+2Qa405gHBJXSfCB2GkvGrIT8vH9wplpRmqs\nopENOVelaVIuDVtQYnSo0r1z18DBcFGiBssJLofMVtzotdhktke3cCG+cNuTyhnI\n7ROOzO2n4KRWjOMVZZWwBrY33pwsKRR3xWu8sfbKPIwP4kaQ3+lGD0pG2fk1hPpS\nYQIDAQAB\n-----END RSA PRIVATE KEY-----"

insId = "INS150915000001"
operId = "123@163.com"
url = "http://127.0.0.1:8080/xlzxop/certificate/auth/relCard/standard.do"
data = '{"cardNo":"6225768780721476","name":"李小明","cidNo":"410821199107144518","mobile":"15920000592","cooperSerialNo":"20170915001001001"}'

encryptData = encrypt( public_key, data)
sign = signData(private_key, data)

print "encryptData：", encryptData
print "signResult:", sign

r = requests.post(url, data={'insId': insId, 'operId': operId, 'sign': sign, 'encrypt': encryptData})

print(r.status_code, r.reason)
print r.text

result = json.loads( r.text)
signResponse =  result.get("sign")
dataResponse = result.get("encrypt")

dataDecrypt = decrypt(private_key, dataResponse)
signResult = verifySign(public_key,dataDecrypt,signResponse)
print '验签结果:',signResult

if signResult:
    print '响应结果:',dataDecrypt
else:
    print '验签不通过'





