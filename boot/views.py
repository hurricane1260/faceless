from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
import json
import operator
from rest_framework_jwt.settings import api_settings
from django.core.cache import cache
from .decorators import auth,request_arg_validate


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER



@api_view(['POST'])
@csrf_exempt
@request_arg_validate("type","userName","password","captcha")
def boot_login(request):
    """
    Login
    :param request:
    :return:
    """
    resp_content = {'code':'0','msg':'Success'}
    req = json.loads(request.body.decode('utf-8'))

    if 'type' not in req:
        resp_content['code'] = '8001'
        resp_content['msg'] = "missing login type"
        return Response(resp_content)
    type = req['type']

    if 'userName' not in req:
        resp_content['code'] = '8001'
        resp_content['msg'] = "missing login userName"
        return Response(resp_content)
    username = req['userName']

    if operator.eq(type, 'account') :
        if 'password' not in req:
            resp_content['code'] = '8001'
            resp_content['msg'] = "missing login password"
            return Response(resp_content)
        password = req['password']
        user = authenticate(username=username, password=password)
    elif operator.eq(type, 'mobile') :
        if 'captcha' not in req:
            resp_content['code'] = '8001'
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
        #token = Token.objects.get(user=user)
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        cache.set(token,payload,timeout=60*5)
        group = user.groups.first()
        resp_content['type'] = type
        resp_content['user'] = {
            'userId':user.id,
            'userName':user.username,
            'userGroup':group.name
        }
        resp_content['token'] = token
    return Response(resp_content)

@csrf_exempt
@api_view(['POST'])
@auth
def boot_test(request):
    resp_content = {'code': '0', 'msg': 'Success'}
    return Response(resp_content)

@csrf_exempt
@api_view(['POST'])
@auth
def boot_logout(request):
    resp_content = {'code': '0', 'msg': 'Success'}
    cache.delete(request.jwt_token)
    return Response(resp_content)

@csrf_exempt
@api_view(['POST'])
@auth
@request_arg_validate("username","password","type")
def boot_signup(request):
    resp_content = {'code': '0', 'msg': 'Success'}
    req = json.load(request.POST)
    # TODO:
    new_user = User(username=req['username'])
    new_user.password = make_password(req['password'])
    if not req['email']:
        new_user.email = req['email']
    new_user.save()
    payload = jwt_payload_handler(new_user)
    token = jwt_encode_handler(payload)
    cache.set(token, payload, timeout=60 * 5)
    group = new_user.groups.first()
    resp_content['type'] = type
    resp_content['user'] = {
        'userId': new_user.id,
        'userName': new_user.username,
        'userGroup': group.name
    }
    resp_content['token'] = token





