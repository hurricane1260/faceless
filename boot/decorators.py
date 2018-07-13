from functools import wraps

from rest_framework.response import Response
from django.core.cache import cache

def auth(func):
    '''判断是否登录'''
    @wraps(func)
    def inner(request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')
        resp_content = {'code': '0', 'msg': 'Success'}
        #ck = request.session.get("user_id")
        if not token:
            resp_content['code'] = '10003'
            resp_content['msg'] = "user need login"
            return Response(resp_content)
        payload = cache.get(token)
        if not payload:
            resp_content['code'] = '10004'
            resp_content['msg'] = "invalid token"
            return Response(resp_content)
        cache.expire(token,timeout=300)
        request.user_info = payload
        request.jwt_token = token
        return func(request, *args, **kwargs)
    return inner


def request_arg_validate(*check_args):
    def decorate(fn):
        @wraps(fn)
        def wrapped(request,*args,**kwargs):
            resp_content = {'code': '0', 'msg': 'Success'}
            for arg_name in check_args:
                if not request.POST.get(arg_name):
                    resp_content['code'] = 10005
                    resp_content['msg'] = "{arg_name} should't be null".format(arg_name=arg_name)
                    return Response(resp_content)
            return fn(request,*args,**kwargs)
        return wrapped
    return decorate