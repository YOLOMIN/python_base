from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from .models import Topic                               #导入所需数据相关联的模型
from .forms import TopicForm
from .forms import TopicForm,Entry
from .forms import TopicForm,EntryForm
from django.http import Http404
# Create your views here.
def index(request):
    # 学习笔记的主页
    return render(request,'learning_logs/index.html')

@login_required         #限制访问显示所有主题的页面-----检查用户是否已登录，仅当用户已登录时，Django才运行topics的代码
def topics(request):                                    #Django从服务器哪里收到requst对象
    # 显示所有的主题
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')       #查询数据库--请求Topic对象，并根据属性date_added进行排序
    context = {'topics':topics}                         #定义一个将发送给模型learning_logs/topics.htm的上下文
    return render(request,'learning_logs/topics.html',context)

@login_required
def topic(request,topic_id):
    # 显示单个主题及其所有的条目
    topic = Topic.objects.get(id=topic_id)

    #确认请求的主题属于当前用户
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic.html',context)

@login_required
def new_topic(request):
    #添加新主题
    if request.method != 'POST':            #如果请求不是POST，请求就是GET需要返回一个空表单
        #未提交数据，创建一个新表单
        form = TopicForm()
    else:
        #POST 提交的数据：对数据进行处理
        form = TopicForm(data=request.POST)
        if form.is_valid():         
            # form.save()
            #将新主题关联到当前用户
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')         #重定向页面

    #显示空表单或指出表单数据无效
    context = {'form':form}
    return render(request,'learning_logs/new_topic.html',context)

@login_required
def new_entry(request,topic_id):
    # 在特定主题中添加新条目
    topic = Topic.objects.get(id=topic_id)
    
    if request.method != 'POST':
        #未提交数据：创建一个空表单
        form = EntryForm()
    else:
        #POST提交的数据：对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic',topic_id=topic_id)

    #显示空表单或指出表单数据无效
    context = {'topic':topic,'form':form}
    return render(request,'learning_logs/new_entry.html',context)

def edit_entry(request,entry_id):
    """编辑既有条目"""
    entry = Entry.objects.get(id=entry_id)     #获取用户要修改的条目对象以及相关联的主题
    topic = entry.topic

    #保护页面edit_entry
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #初次请求：使用当前条目填充表单
        form = EntryForm(instance=entry)        #使用实参instance=entry创建一个EntryForm实例
    else:
        #POST 提交的数据：对数据进行处理
        form = EntryForm(instance=entry,data=request.POST)          #传递实参instance=entry和data=request.POST,让Django根据既有条目对象创建一个表单实例，并根据request.POST中的相关数据对其进行修改
        if form.is_valid():                     #检查表单是否有效，
            form.save()
            return redirect('learning_logs:topic',topic_id=topic.id)    #重定向到显示条目所属主题的页面，用户将在其中看到其编辑的条目 的新版本
    context = {'entry':entry,'topic':topic,'form':form}
    return render(request,'learning_logs/edit_entry.html',context)
