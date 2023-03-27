import requests
from geopy.geocoders import Nominatim

def geocoding(address):
    geolocoder = Nominatim(user_agent = 'South Korea', timeout=None)
    geo = geolocoder.geocode(address)
    location = {"lat": str(geo.latitude), "lng": str(geo.longitude)}
    return location['lat'], location['lng']

def food_list(address):

    lat, lng = geocoding(address)

    cookies = {
        'optimizelyEndUserId': 'oeu1676798887770r0.9667135447884909',
        '_gcl_au': '1.1.1642016665.1676798888',
        '_fbp': 'fb.2.1676798912123.1470443580',
        '_gid': 'GA1.3.2034530224.1679933336',
        'sessionid': '6b2166e9ad42cad811e32d3712bf186f',
        'RestaurantListCookieTrigger': 'true',
        '_ga': 'GA1.3.2019210241.1676798888',
        '_gat': '1',
        '_gat_UA-42635603-4': '1',
        '__cf_bm': 'VYbtGY8OjdwJlQBIUdrIFE13890NRj0M.txI0I5H00I-1679934826-0-AT2322hTWB8ovzx+v8MNQWGzaBJ/s74StJleJaeq41bxO5t4x015idxF50mHrreL14J2WMqqnnR5M/RfMQXFnh0=',
        '_ga_6KMY7BWK8X': 'GS1.1.1679933336.4.1.1679934837.60.0.0',
        'wcs_bt': 's_51119d387dfa:1679934837',
    }

    headers = {
        'authority': 'www.yogiyo.co.kr',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,ko;q=0.8,de;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'optimizelyEndUserId=oeu1676798887770r0.9667135447884909; _gcl_au=1.1.1642016665.1676798888; _fbp=fb.2.1676798912123.1470443580; _gid=GA1.3.2034530224.1679933336; sessionid=6b2166e9ad42cad811e32d3712bf186f; RestaurantListCookieTrigger=true; _ga=GA1.3.2019210241.1676798888; _gat=1; _gat_UA-42635603-4=1; __cf_bm=VYbtGY8OjdwJlQBIUdrIFE13890NRj0M.txI0I5H00I-1679934826-0-AT2322hTWB8ovzx+v8MNQWGzaBJ/s74StJleJaeq41bxO5t4x015idxF50mHrreL14J2WMqqnnR5M/RfMQXFnh0=; _ga_6KMY7BWK8X=GS1.1.1679933336.4.1.1679934837.60.0.0; wcs_bt=s_51119d387dfa:1679934837',
        'referer': 'https://www.yogiyo.co.kr/mobile/',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'x-apikey': 'iphoneap',
        'x-apisecret': 'fe5183cc3dea12bd0ce299cf110a75a2',
    }

    params = {
        'items': '10',
        'lat': f'{lat}',
        'lng': f'{lng}',
        'order': 'rank',
        'page': '0',
        'search': '',
    }

    response = requests.get('https://www.yogiyo.co.kr/api/v1/restaurants-geo/', params=params, cookies=cookies, headers=headers)
    return response.json()