from .utils import post_request

def confirm_signup(session_id, password, nickname, job, grades, job_visibility,
                   family_name, family_name_kana, given_name, given_name_kana, runtimeType):
    url = 'https://api.studyplus.jp/2/confirm_signup'
    json_data = {
        'session_id': session_id,
        'password': password,
        'nickname': nickname,
        'job': job,
        'grades': grades,
        'job_visibility': job_visibility,
        'family_name': family_name,
        'family_name_kana': family_name_kana,
        'given_name': given_name,
        'given_name_kana': given_name_kana,
        'runtimeType': runtimeType,
    }
    response_data = post_request(url, json_data)
    access_token = response_data.get('access_token')
    username = response_data.get('username')
    print(f"アクセストークン: {access_token}\nユーザーネーム: {username}\nで登録しました")
    return access_token, username
