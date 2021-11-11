# Downloads all current CSB podcasts

import requests, bs4, lxml, time, re, wget

homepage = "https://superbestfriendcast.libsyn.com/"
request = requests.get(homepage)
page_html = bs4.BeautifulSoup(request.content, 'lxml')
page_links = page_html.find_all('a', {'href': re.compile(r'superbestfriendcast\.libsyn\.com\/csb-')})
latest_episode_str = (re.findall(r'[0-9]{3}', page_links[0]['href']))[0]
latest_episode = int(latest_episode_str.lstrip("0"))

def create_links(latest_episode):
    for i in range(1, latest_episode):
        prefix = "CSB0"
        suffix = str(i) + ".mp3"
        url = "https://traffic.libsyn.com/secure/force-cdn/highwinds/superbestfriendcast/" + prefix
        if i > 0 and i < 10:
            wget.download(url+ "0" + suffix,"./" + prefix + "0" + suffix)
        elif i > 9:
            wget.download(url + suffix,"./" + prefix + suffix)
        else:
            print("No negative numbers!")
            break
    return episodes

create_links(latest_episode)
