from django.db import models

# Create your models here.

class Menu(models.Model):
    """
    菜单
    """
    menu_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=32, unique=True)
    parent_id = models.IntegerField(unique=True,null=True,blank=True)

    def __str__(self):
        # 显示层级菜单
        title_list = [self.title]
        p = self.parent_id
        while p:
            title_list.insert(0, p.title)
            p = p.parent_id
        return '-'.join(title_list)

class Role(models.Model):
    """
    角色
    """
    role_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.role_name

class Permission(models.Model):
    """
    权限
    """
    role_id = models.IntegerField()
    menu_id = models.IntegerField()
