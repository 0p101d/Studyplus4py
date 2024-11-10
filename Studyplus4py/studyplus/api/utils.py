import requests

#Headers Functions !!
def get_headers():
    return {
        'accept': '*/*',
        'accept-language': 'ja;q=0.8',
        'client-service': 'Studyplus',
        'content-type': 'application/json; charset=utf-8',
        'origin': 'https://app.studyplus.jp',
        'referer': 'https://app.studyplus.jp/',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Brave";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    }

# Common functions to send POST requests
def post_request(url, json_data):
    headers = get_headers()
    response = requests.post(url, headers=headers, json=json_data)
    response.raise_for_status()
    return response.json()