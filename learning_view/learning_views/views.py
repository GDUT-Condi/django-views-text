# coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect

def index(request):
    return HttpResponse(request.path)

def detail(request, a1, a2, a3):
    return HttpResponse('%s,%s,%s' % (a1, a2, a3))

# 展示链接页面
def getText1(request):
    return render(request, 'learning_views/getText1.html')

# 接受一键一值
def getText2(request):
    # 接受键值对
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    # 构建上下文
    context = {'text1': a, 'text2': b, 'text3': c}
    return render(request, 'learning_views/getText2.html', context)

# 接受一键多值
def getText3(request):
    a_s = request.GET.getlist('a')
    context = {'texts': a_s}
    return render(request, 'learning_views/getText3.html', context)

# 创建form表单
def postText1(request):
    return render(request, 'learning_views/postText1.html')

# 展现post的内容
def postText2(request):
    uname = request.POST['uname']
    upassword = request.POST['upassword']
    ugender = request.POST['ugender']
    uhobby = request.POST.getlist('uhobby')
    context = {'uname': uname, 'upassword': upassword, 'ugender': ugender, 'uhobby': uhobby}
    return render(request, 'learning_views/postText2.html', context)

# cookie练习
def cookieText(request):
    response = HttpResponse()
    cookie = request.COOKIES
    if cookie.has_key('t1'):
        response.write(cookie['t1'])
    #response.set_cookie('t1', 'abc')
    return response

#转向视图
def redText1(request):
    #return HttpResponseRedirect('/booktest/redText2/')
    return redirect('/booktest/redText2/')

def redText2(request):
    return HttpResponse('这是转向来的练习')

#用户登录练习
def session1(request):
    uname =request.session.get('myname','未登录')
    context = {'uname':uname}
    return render(request,'learning_views/session1.html',context)

def session2(request):
    return render(request,'learning_views/session2.html')

def session2_handle(request):
    uname = request.POST['uname']
    request.session['myname']=uname
    #退出浏览器就过期
    request.session.set_expiry(0)
    return redirect('/booktest/session1/')

def session3(request):
    #删除session
    del request.session['myname']
    return redirect('/booktest/session1/')