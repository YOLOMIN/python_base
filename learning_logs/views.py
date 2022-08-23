from django.shortcuts import render

from .models import Topic                               #导入所需数据相关联的模型

# Create your views here.
def index(request):
    # 学习笔记的主页
    return render(request,'learning_logs/index.html')

def topics(request):                                    #Django从服务器哪里收到requst对象
    # 显示所有的主题
    topics = Topic.objects.order_by('date_added')       #查询数据库--请求Topic对象，并根据属性date_added进行排序
    context = {'topics':topics}                         #定义一个将发送给模型的上下文
    return render(request,'learning_logs/topics.html',context)

def topic(request,topic_id):
    # 显示单个主题及其所有的条目
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic.html',context)