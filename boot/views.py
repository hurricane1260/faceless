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
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username,password=password)

    resp_content = {'errcode':0,'errmsg':''}

    if not user:
        resp_content['errcode'] = 1
        resp_content['errmsg'] = "user not invalid"
    else:
        resp_content['user'] = {
            'userid':user.id,
            'username':user.username
        }
    return Response(json.dumps(resp_content))
