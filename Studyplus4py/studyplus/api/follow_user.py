from .utils import post_request

def follow_user(access_token, username):
    json_data = {
        'username': username,
    }
    headers = {
        'Authorization': f'OAuth {access_token}',
    }
    response = post_request('https://api.studyplus.jp/2/follows', json_data)
    return response
