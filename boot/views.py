from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

@api_view(['POST'])
@csrf_exempt
def boot_login(request):
    """
    Login
    :param request:
    :return:
    """
    username = request.POST.get('username', 'admin')
    password = request.POST.get('password', '123123')
    user = authenticate(username=username,password=password)

    resp_content = {'code':0,'msg':'Success'}

    if not user:
        resp_content['code'] = 1
        resp_content['msg'] = "user not invalid"
    else:
        resp_content['user'] = {
            'userid':user.id,
            'username':user.username
        }
    return Response(resp_content)
