from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Menu(models.Model):
    """
    菜单
    """
    title = models.CharField(max_length=32, unique=True)
    url = models.CharField(max_length=256, unique=True)
    parent = models.ForeignKey("Menu", null=True, blank=True)

    def __str__(self):
        # 显示层级菜单
        title_list = [self.title]
        p = self.parent
        while p:
            title_list.insert(0, p.title)
            p = p.parent
        return '-'.join(title_list)


class Permission(models.Model):
    """
    权限
    """
    title = models.CharField(max_length=32, unique=True)
    menus = models.ManyToManyField("Menu")

    def __str__(self):
        # 显示带菜单前缀的权限
        return '{menu}---{permission}'.format(menu=self.menu, permission=self.title)


class Role(models.Model):
    """
    角色：绑定权限
    """
    title = models.CharField(max_length=32, unique=True)
    permissions = models.ManyToManyField("Permission")
    # 定义角色和权限的多对多关系

    def __str__(self):
        return self.title


class UserRole(models.Model):
    """
    用户：划分角色
    """
    user = models.ForeignKey(User)
    role = models.ForeignKey("Role")

    def __str__(self):
        return "user:{user_id}-roles:{role_id}".format(user_id=self.user_id,role_id=self.role_id)