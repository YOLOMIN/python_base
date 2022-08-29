# python_base
建立虚拟环境
$ python3 -m venv 11_env

激活虚拟环境
[lss@lss-pc ~]$ source 11_env/bin/activate

关闭虚拟环境
(11_env) [lss@lss-pc ~]$ deactivate 

安装Django
(11_env) [lss@lss-pc ~]$ pip install django
如果提示网络不可达，则可以指定源安装
(11_env) [lss@lss-pc Django]$ pip install django -i https://pypi.mirrors.ustc.edu.cn/simple/

在Django中创建项目：
(11_env) [lss@lss-pc ~]$ django-admin startproject learning_log .

创建数据库:
(11_env) [lss@lss-pc ~]$ python3 manage.py migrate


查看项目：---运行项目
(11_env) [lss@lss-pc ~]$ python3 manage.py runserver


创建应用程序
(11_env) [lss@lss-pc ~]$ python3 manage.py startapp learning_logs


定义模型
(11_env) [lss@lss-pc ~]$ vim ./learning_logs/models.py


(11_env) [lss@lss-pc ~]$ cat ./learning_logs/models.py
from django.db import models

# Create your models here.
class Topic(models.Model):
#用户学习的主题
text = models.CharField(max_length=200)
date_added = models.DateTimeField(auto_now_add=True)

def __str__(self):
#返回模型的字符串表示
return self.text

激活模型

修改数据库
(11_env) [lss@lss-pc Django]$ python3 manage.py makemigrations learning_logs
(11_env) [lss@lss-pc Django]$ python3 manage.py migrate

Django管理网站
创建超级用户
(11_env) [lss@lss-pc Django]$ python3 manage.py  createsuperuser

迁移模型Entry

(11_env) [lss@lss-pc Django]$ python3 manage.py makemigrations learning_logs
(11_env) [lss@lss-pc Django]$ python3 manage.py migrate

步骤：修改models.py，执行python3 manage.py makemigrations learning_logs然后 python3 manage.py migrate
