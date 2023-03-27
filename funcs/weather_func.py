import requests
from datetime import datetime
import time

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
        'page_uid': 'iuv1cdp0Jy0ssPZJ7eVssssssrd-460817',
        'NID_SES': 'AAABwGDNGvZOBnxUxKNUPBZ5ULh6XHztsGZhcBP/pQmCxQsZEzAyRGYuVZPiN91Z1r4rkcCvY+3FeLnJ/nm3V91RdUU9vGxqUN3KNuKgXb/jWSFzW3fsQgaA1s2fabumFjpBAJvZOwaRw9p7Uw4LvUCIf5tdsg5DijcW0jj+1YwSAE3tRwh3A5OPmdahhrfvJ0H7IBJVcIRj9i1Mz5HHt0zh4St+Um0+hTNGt1n2WBQPmISePB4a2CKyik0khoOIGLfYyhb3nACi4bDxTIKfNfItEvHX5p3oBU9mP8Ao1aqdd7Sz4dEuqmHROO1RmY3QRa9S/RluJRLkuaemAelV59UIQP/A9X5AiQUTW9Mr6zCdl0ApPHd+52NDl/4jIwwcxIItCMoZRwSH6LxjTRfaqdgJ1RZ4y4JynP9n6urh7YKLCNU0CPdzYWaDHYhxndJzYtFDr7R6XT+Ey+UAEnqQjVfvZ7OyeVl4LBxSZiegSxkdU1Xa5EIfop2o5NBF1rG/YFZOeVgbMgdwol/t2+m8X+RZjyjDK6MMuDgFqDoGJz2d8Hc2LY8+khBr920YDOlLlY+PaN/Y8xqxiVh0X39hjpbRtbs=',
        'NV_WETR_TRACED_RGN': '"MDYyOTAxMTQ=,MDYxMTAxMDE=,MTYxMTExMjA=,MDkxNDAxMDQ=,MDIxMTMxMjg=,MDQ5NDAzMjA="',
        'NV_WETR_LOCATION_RGN_M': '"MDYyOTAxMTQ="',
        'NV_WETR_LAST_ACCESS_RGN_M': '"MDYyOTAxMTQ="',
        'JSESSIONID': 'F24316C44A42961F078740E430A81EBC',
    }

    headers = {
        'authority': 'weather.naver.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9,ko;q=0.8,de;q=0.7',
        # 'cookie': 'NNB=LL6FACFGUPLGG; m_loc=aff32efa7d4004e355ed513feade17fe8bd339452ab05a81c734984dfc484e12; nx_ssl=2; NFS=2; nid_inf=1261739670; NID_AUT=dIwWHyILwMpPXNBSLP0wLCAywbjTEcRR7NH7wqlrlKPgJOJDAuZPBeZGCYO+WRxs; NID_JKL=wfv+h8I6mobAlR8+tpwWbwDdS9mpQaveNTLlwXHGy28=; page_uid=iuv1cdp0Jy0ssPZJ7eVssssssrd-460817; NID_SES=AAABwGDNGvZOBnxUxKNUPBZ5ULh6XHztsGZhcBP/pQmCxQsZEzAyRGYuVZPiN91Z1r4rkcCvY+3FeLnJ/nm3V91RdUU9vGxqUN3KNuKgXb/jWSFzW3fsQgaA1s2fabumFjpBAJvZOwaRw9p7Uw4LvUCIf5tdsg5DijcW0jj+1YwSAE3tRwh3A5OPmdahhrfvJ0H7IBJVcIRj9i1Mz5HHt0zh4St+Um0+hTNGt1n2WBQPmISePB4a2CKyik0khoOIGLfYyhb3nACi4bDxTIKfNfItEvHX5p3oBU9mP8Ao1aqdd7Sz4dEuqmHROO1RmY3QRa9S/RluJRLkuaemAelV59UIQP/A9X5AiQUTW9Mr6zCdl0ApPHd+52NDl/4jIwwcxIItCMoZRwSH6LxjTRfaqdgJ1RZ4y4JynP9n6urh7YKLCNU0CPdzYWaDHYhxndJzYtFDr7R6XT+Ey+UAEnqQjVfvZ7OyeVl4LBxSZiegSxkdU1Xa5EIfop2o5NBF1rG/YFZOeVgbMgdwol/t2+m8X+RZjyjDK6MMuDgFqDoGJz2d8Hc2LY8+khBr920YDOlLlY+PaN/Y8xqxiVh0X39hjpbRtbs=; NV_WETR_TRACED_RGN="MDYyOTAxMTQ=,MDYxMTAxMDE=,MTYxMTExMjA=,MDkxNDAxMDQ=,MDIxMTMxMjg=,MDQ5NDAzMjA="; NV_WETR_LOCATION_RGN_M="MDYyOTAxMTQ="; NV_WETR_LAST_ACCESS_RGN_M="MDYyOTAxMTQ="; JSESSIONID=F24316C44A42961F078740E430A81EBC',
        'referer': 'https://weather.naver.com/',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'regionCode': f'{region_code}',
        'aplYm': '',
    }

    response = requests.get('https://weather.naver.com/today/api/pastWetr', params=params, cookies=cookies, headers=headers)
    return response.json()