from .utils import post_request

def verify_token(token, session_id):
    url = 'https://api.studyplus.jp/2/verify_token'
    json_data = {
        'session_id': session_id,
        'token': token,
    }
    response_data = post_request(url, json_data)
    return response_data
