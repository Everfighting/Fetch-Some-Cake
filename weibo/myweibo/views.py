import json

import requests
from django.http import HttpResponse
from django.shortcuts import render





def get_user_info(request):
    weibo_access_url = 'https://api.weibo.com/oauth2/access_token'
    params = {
        'client_id': '2217088527',
        'client_secret': '471878a0a07ccc5f8585c41217c58d1d',
        'grant_type': 'authorization_code',
        'code': request.GET.get('code'),  # 获得code
        'redirect_uri': 'http://127.0.0.1:8000/home/weibologin'
    }
    resp = requests.post(weibo_access_url, data=params)
    json_data = resp.json()
    print(json_data)
    access_token = json_data.get('access_token')
    # #
    get_userid_url = 'https://api.weibo.com/2/account/get_uid.json?access_token=' + access_token
    uid = requests.get(get_userid_url).json().get('uid')
    #
    user_url = "https://api.weibo.com/2/users/show.json"
    get_url = user_url + "?access_token={at}&uid={uid}".format(at=access_token, uid=uid)
    response = requests.get(get_url)
    response_dict=response.text
    response_dict=json.loads(response_dict)
    screen_name=response_dict['screen_name']
    profile_image_url=response_dict['profile_image_url']
    location=response_dict["location"]
    description=response_dict['description']
    print(screen_name,profile_image_url,location,description)


    data={

    }

    return render(request,'weibologin.html',locals())






