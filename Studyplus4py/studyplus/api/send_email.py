from .utils import post_request

def send_email(email, consumer_key=None, consumer_secret=None):
    consumer_key = consumer_key
    consumer_secret = consumer_secret

    url = 'https://api.studyplus.jp/2/start_signup'
    json_data = {
        'consumer_key': consumer_key,
        'consumer_secret': consumer_secret,
        'email': email,
    }
    response_data = post_request(url, json_data)
    session_id = response_data.get('session_id')
    print(f"セッションID: {session_id}")
    return session_id
