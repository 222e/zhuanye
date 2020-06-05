# -*- coding:utf-8 -*-
import urllib.request

doc = open('out.txt', 'w')
url = "http://cebxol.apabiedu.com/api/getservice?orgid=gxjc&ObjId=m.20190902-BJDX-RXJC-0208.ft.cebx.1&UserName=carsi%3Ae6e4c1e14d51dfc4bf94a344960cf40189c97d26&MetaId=m.20190902-BJDX-RXJC-0208&cult=CN&dbsource=dlib&Time=2020/6/5%207:35:12&Sign=A0BB7602E6638C47D27849CE6F7ED4CE&Rights=1-0_00&width=2500&height=4000&page="
i = 3
while i < 637:
    url_a = url
    url_a = url_a + str(i) + "&ServiceType=imagepage"
    print(url_a,file = doc)
    i = i + 1
print("Good bye!")
