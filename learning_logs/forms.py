from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):  #定义一个名为TopicForm的类，继承了forms.ModelForm
    class Meta:
        model = Topic               #根据模型Topic创建表单
        fields = ['text']           #只是包含text字段
        labels = {'text':''}        #不为字段text生成标签


