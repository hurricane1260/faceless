from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import operator

@api_view(['POST'])
@csrf_exempt
def boot_login(request):
    """
    Login
    :param request:
    :return:
    """
    resp_content = {'code':'0','msg':'Success'}
    req = json.loads(request.body)

    if 'type' not in req:
        resp_content['code'] = '3'
        resp_content['msg'] = "missing login type"
        return Response(resp_content)
    type = req['type']

    if 'userName' not in req:
        resp_content['code'] = '3'
        resp_content['msg'] = "missing login userName"
        return Response(resp_content)
    username = req['userName']

    if operator.eq(type, 'account') :
        if 'password' not in req:
            resp_content['code'] = '3'
            resp_content['msg'] = "missing login password"
            return Response(resp_content)
        password = req['password']
        user = authenticate(username=username, password=password)
    elif operator.eq(type, 'mobile') :
        if 'captcha' not in req:
            resp_content['code'] = '3'
            resp_content['msg'] = "missing captcha"
            return Response(resp_content)
        captcha = req['captcha']
        # 获取关联账户
        user = User.objects.get(username__exact='guest')
    else:
        resp_content['code'] = '10002'
        resp_content['msg'] = "invalid login type"
        return Response(resp_content)

    if not user:
        resp_content['code'] = '10001'
        resp_content['msg'] = "user not invalid"
    else:
        resp_content['type'] = type
        resp_content['user'] = {
            'userId':user.id,
            'userName':user.username
        }
    return Response(resp_content)
