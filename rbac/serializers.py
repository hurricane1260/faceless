from django.contrib.auth.models import User,Group
from rbac.models import *

from rest_framework import serializers

class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = ('menu_id','title','parent')

class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission
        fields = ('title','menu')

class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role

class UserRoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserRole