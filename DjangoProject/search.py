from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
# 表单
def search_form(request):
    return render_to_response('search.html')


# 接受请求的数据
def search_get(request):
    # request.encoding = 'utf-8'
    if 'wenben' in request.GET:
        print(request.GET)
        wenben = request.GET['wenben']
        if wenben is '':
            message = '内容无效!'
        elif wenben == '陈丹妮':
            message = "龙哥牛逼！！！"
        else:
            message = "你要搜索的内容为：" + request.GET['wenben']
    else:
        message = '内容无效!'
    return HttpResponse(message)

@csrf_protect
def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)

