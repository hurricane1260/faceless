from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


@api_view(['POST'])
@csrf_exempt
def create_user(request):
    '''
    create new user
    :param request:
    :return:
    '''
    # TODO:
    return

@api_view(['GET'])
def users(request):
    '''
    get users list
    :param request:
    :return:
    '''
    # TODO:
    return

@api_view(['POST'])
def delete_user(request):
    '''
    delete user,actually,wo don't delete user phyicaly,wo mark the user's status to be frozen
    :param request:
    :return:
    '''
    # TODO:
    return
