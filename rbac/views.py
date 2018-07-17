import json

from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rbac.models import *
from boot.views import auth

@csrf_exempt
@api_view(['POST'])
@auth
def menus(request):
    '''
    get all menus
    #TODO:get all menus by role
    :param request:
    :return:
    '''
    resp={'code':'0','msg':'success'}
    req = json.loads(request.POST)
    user = User.objects.get(id=req['user_id'])
    roles = UserRole.objects.filter(user = user.id)

    userrole = UserRole.objects.get(user=req['user_id'])
    return Response(resp)



@api_view(['POST'])
@csrf_exempt
@auth
def create_user(request):
    '''
    create new user
    :param request:
    :return:
    '''
    # TODO:
    return

@api_view(['GET'])
@auth
def users(request):
    '''
    get users list
    :param request:
    :return:
    '''
    # TODO:
    return

@api_view(['POST'])
@auth
def delete_user(request):
    '''
    delete user,actually,wo don't delete user phyicaly,wo mark the user's status to be frozen
    :param request:
    :return:
    '''
    # TODO:
    return



@api_view(['POST'])
@auth
def create_menu(request):
    '''
    add a menu
    :param request:
    :return:
    '''
    resp = {'code':0,'msg':'success'}
    req = json.load(request.body.decode('utf-8'))


