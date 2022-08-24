from pyexpat import model
from django import forms
from .models import Topic,Entry

class TopicForm(forms.ModelForm):  #定义一个名为TopicForm的类，继承了forms.ModelForm
    class Meta:
        model = Topic               #根据模型Topic创建表单
        fields = ['text']           #只是包含text字段
        labels = {'text':''}        #不为字段text生成标签


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widgets = {'text':forms.Textarea(attrs={'cols':80})}        #定义属性widgets，给足够的编辑文本空间