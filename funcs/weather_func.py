import requests
from datetime import datetime
import time
from bs4 import BeautifulSoup as bs

def get_all_region_weather():
    today = datetime.today().strftime('%Y%m%d')
    url = f'https://weather.naver.com/today/api/nation/{today}/now'
    response = requests.get(url)
    result = response.json()
    return result

def get_region_code(address):
    url = f'https://ac.weather.naver.com/ac?q_enc=utf-8&r_format=json&r_enc=utf-8&r_lt=1&st=1&q={address}'
    location = requests.get(url)
    return location.json()['items'][0][0][1][0]

def get_region_weather(address):

    region_code = get_region_code(address)

    cookies = {
        'NNB': 'LL6FACFGUPLGG',
        'm_loc': 'aff32efa7d4004e355ed513feade17fe8bd339452ab05a81c734984dfc484e12',
        'nx_ssl': '2',
        'NFS': '2',
        'nid_inf': '1261739670',
        'NID_AUT': 'dIwWHyILwMpPXNBSLP0wLCAywbjTEcRR7NH7wqlrlKPgJOJDAuZPBeZGCYO+WRxs',
        'NID_JKL': 'wfv+h8I6mobAlR8+tpwWbwDdS9mpQaveNTLlwXHGy28=',
        'page_uid': 'iuclqlprvh8ssfHfeVVssssssHl-231783',
        'NID_SES': 'AAABvfrgbcXgOY2+0rUsJJSBbvohTDaeamgg21Dfb77E5ZaXq4evSMp5Te4kTn22KW9WCT8KceBqRfFIKLmU+L6zicXfUyfRnipBDT4hwl//J8sp25/UzvMxSjkHrIdt1tpbObCu8mzFEJ3olauufoD8fsL8Ta07aphbx4X/uJyDla1GcGw/aRNa9d//umHDrR4uFkU7mILoUE1ssmSkl7bbr8Vw0wm69+3wc+iLwyp22iAF5tkw0XRrnWXKkYk0zlLKEfIKaEAoV3iHuwGXSQITleLD/aBJochH6I+Jz24E0iMXXikJe3C2YI8IHsG9Xh6Izw4kK8pyHs4Nf3ht3/iB51lxao8PAR3JUnxJtfZcSKneEOo8cqr2dKPHC4fblys/yfAWNPgevpwupuTLDWjtxHD5uN5DBFJnr5fddxEVRinEE2gPIi5/L+Cf8zzWDgxkfYvuFeL1cunDcIxsORXJGOEED3eAglVojM4XTu/Ky6Sn5w8/xBpM9OtYKpnBTQheFIP5++ARUCGkTdZEjw7Z/6ZYexluR8omefhphfN+JyaNVgxwSxN0O4u7yk8d6xnnq0gNF3zyEm2aWj2Si0snfGA=',
        'NV_WETR_TRACED_RGN': '"MTAxNDAxMDU=,MDYyOTAxMTQ=,MDQxOTAxMTg=,MDYxMTAxMDE=,MTYxMTExMjA=,MDkxNDAxMDQ=,MDIxMTMxMjg=,MDQ5NDAzMjA="',
        'NV_WETR_LAST_ACCESS_RGN_M': '"MTAxNDAxMDU="',
        'NV_WETR_LOCATION_RGN_M': '"MTAxNDAxMDU="',
        'JSESSIONID': '02AFA7D36086D7D2C1411CB90951938D',
    }

    headers = {
        'authority': 'weather.naver.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,ko;q=0.8,de;q=0.7',
        'cache-control': 'max-age=0',
        # 'cookie': 'NNB=LL6FACFGUPLGG; m_loc=aff32efa7d4004e355ed513feade17fe8bd339452ab05a81c734984dfc484e12; nx_ssl=2; NFS=2; nid_inf=1261739670; NID_AUT=dIwWHyILwMpPXNBSLP0wLCAywbjTEcRR7NH7wqlrlKPgJOJDAuZPBeZGCYO+WRxs; NID_JKL=wfv+h8I6mobAlR8+tpwWbwDdS9mpQaveNTLlwXHGy28=; page_uid=iuclqlprvh8ssfHfeVVssssssHl-231783; NID_SES=AAABvfrgbcXgOY2+0rUsJJSBbvohTDaeamgg21Dfb77E5ZaXq4evSMp5Te4kTn22KW9WCT8KceBqRfFIKLmU+L6zicXfUyfRnipBDT4hwl//J8sp25/UzvMxSjkHrIdt1tpbObCu8mzFEJ3olauufoD8fsL8Ta07aphbx4X/uJyDla1GcGw/aRNa9d//umHDrR4uFkU7mILoUE1ssmSkl7bbr8Vw0wm69+3wc+iLwyp22iAF5tkw0XRrnWXKkYk0zlLKEfIKaEAoV3iHuwGXSQITleLD/aBJochH6I+Jz24E0iMXXikJe3C2YI8IHsG9Xh6Izw4kK8pyHs4Nf3ht3/iB51lxao8PAR3JUnxJtfZcSKneEOo8cqr2dKPHC4fblys/yfAWNPgevpwupuTLDWjtxHD5uN5DBFJnr5fddxEVRinEE2gPIi5/L+Cf8zzWDgxkfYvuFeL1cunDcIxsORXJGOEED3eAglVojM4XTu/Ky6Sn5w8/xBpM9OtYKpnBTQheFIP5++ARUCGkTdZEjw7Z/6ZYexluR8omefhphfN+JyaNVgxwSxN0O4u7yk8d6xnnq0gNF3zyEm2aWj2Si0snfGA=; NV_WETR_TRACED_RGN="MTAxNDAxMDU=,MDYyOTAxMTQ=,MDQxOTAxMTg=,MDYxMTAxMDE=,MTYxMTExMjA=,MDkxNDAxMDQ=,MDIxMTMxMjg=,MDQ5NDAzMjA="; NV_WETR_LAST_ACCESS_RGN_M="MTAxNDAxMDU="; NV_WETR_LOCATION_RGN_M="MTAxNDAxMDU="; JSESSIONID=02AFA7D36086D7D2C1411CB90951938D',
        'referer': 'https://weather.naver.com/',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    }

    response = requests.get(f'https://weather.naver.com/today/{region_code}', cookies=cookies, headers=headers)

    html = bs(response.text, 'html.parser')
    today_table = html.find('div', {'class' : 'weather_table_wrap'})
    today_tables = today_table.find_all('th', {'class' : 'data top _cnItemTime'})
    location = html.find('strong', {'class' : 'location_name'})
    weathers = f'지역 : {location.text} \n'
    for today_table in today_tables[:24]:
        data_tmpr = today_table['data-tmpr']
        data_wetr_text = today_table['data-wetr-txt']
        data_ymdt = today_table['data-ymdt']
        year = data_ymdt[:4]
        month = data_ymdt[4:6]
        date = data_ymdt[6:8]
        hour = data_ymdt[8:10]
        weathers += f'[{year}년 {month}월 {date}일 {hour}시] 온도 : {data_tmpr} | 날씨 : {data_wetr_text}\n'

        if hour == '23':
            tomorrow_weather = html.find('th', {'class' : 'data top tomorrow _cnItemTime'})
            data_tmpr = tomorrow_weather['data-tmpr']
            data_wetr_text = tomorrow_weather['data-wetr-txt']
            data_ymdt = tomorrow_weather['data-ymdt']
            year = data_ymdt[:4]
            month = data_ymdt[4:6]
            date = data_ymdt[6:8]
            hour = data_ymdt[8:10]
            weathers += f'[{year}년 {month}월 {date}일 {hour}시] 온도 : {data_tmpr} | 날씨 : {data_wetr_text}\n'
        
    return weathers