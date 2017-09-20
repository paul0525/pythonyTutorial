#coding="utf-8"

import urllib2
import re
import threading
import time

'''
http://www.cnproxy.com/proxy1.html
http://www.66ip.cn/2.html
'''

proxylistg = []

def get_proxy_from_cnproxy():
    
    p=re.compile('''<tr><td>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>(.+?)</td></tr>''')
    
    for i in range(1,6):
        target = r"http://www.66ip.cn/%d.html" % i 
        print target
        req = urllib2.urlopen( target )
        #print req.headers
        result =  req.read().decode("gbk")
        matchs =  p.findall(result)
        print matchs
        for row in matchs:
            ip = row[0].encode("utf-8")
            if ip=='ip':
                continue
            port = row[1].encode("utf-8")
            address = row[2].encode("utf-8")
            l = [ip,port,address]
            print l
            proxylistg.append(l)


class ProxyCheck(threading.Thread):
    def __init__(self, proxylist,fileName):
        threading.Thread.__init__(self)
        self.proxylist = proxylist
        self.timeout = 8
        self.test_url="http://www.baidu.com"
        self.test_str="030173"
        self.checkedProxyList = []
        self.fileName = fileName
        
    def checkProxy(self):
        cookies = urllib2.HTTPCookieProcessor()
        for proxy in self.proxylist:
            proxy_handler = urllib2.ProxyHandler({"http":r'http://%s:%s'%(proxy[0],proxy[1])})
            opener = urllib2.build_opener(cookies, proxy_handler)
            opener.addheaders=[('User-agent', 'Mozilla/5.0')]
            urllib2.install_opener(opener)
            t1 = time.time()
            try:
                req = urllib2.urlopen(self.test_url, timeout=self.timeout)
                result = req.read()
                timeused = time.time() - t1
                pos = result.find(self.test_str)
                if pos > 1:
                    print 'it can be used'
                    self.checkedProxyList.append((proxy[0],proxy[1],proxy[2],timeused))
                else:
                    continue
            except Exception,e:
                print e.message
                continue
            
            
    def sort(self):
        sorted(self.checkedProxyList, cmp=lambda x,y:cmp(x[3],y[3]))
    
    def save(self):
        f = open( self.fileName,'w+')
        for proxy in self.checkedProxyList:
            f.write("%s:%s\t%s\t%s\n"%(proxy[0],proxy[1],proxy[2],str(proxy[3])))
        f.flush()
        f.close()
    
    def run(self):
        self.checkProxy()
        self.sort()
        self.save()
        
        
if __name__ == '__main__':
    get_proxy_from_cnproxy()
    t1 = ProxyCheck(proxylistg, "t1.txt")
    t1.start()