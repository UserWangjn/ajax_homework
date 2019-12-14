'''
https://www.cnblogs.com/maple-shaw/articles/9524153.html
'''
from django.shortcuts import render,HttpResponse
from app01.models import Grade

def index(request):
    num1,num2 ='',''
    if request.method == 'POST':
        num1 = request.POST.get('i1')
        num2 = request.POST.get('i2')
        print(num1,num2)
        return HttpResponse('OK11')
    return render(request,'index.html',{
        'i1':num1,
        'i2':num2
    })


def calc(request):
    num1 = int(request.POST.get('i1'))
    num2 = int(request.POST.get('i2'))
    num3 = num1 + num2
    return HttpResponse(num3)


def upload(request):
    if request.is_ajax():
        print('request.FILES:',request.FILES)
        file = request.FILES.get('f1')
        print('file:',file)
        with open(file.name,'wb') as f:
            for i in file.chunks():
                f.write(i)

        return HttpResponse('上传成功')

    return render(request, 'upload.html')


def regist(request):
    '''
    注册功能，主要练习在注册表单中，当用户填写了用户名后，把光标移开后，
    会自动向服务器发送异步请求。服务器返回这个用户名是否已经被注册过。
    :param request:
    :return:
    '''
    if request.is_ajax():
        user_name = request.POST.get('username')
        if user_name == 'ww':
            return HttpResponse(True)
        else:
            return HttpResponse(False)
    return render(request,'regist.html')


def sweetalert(request):
    '''
    练习ajax的sweetAlert
    :param request:
    :return:
    '''
    grade_obj = Grade.objects.all()
    # print(grade_obj)
    return render(request,'sweetalert.html',{'grade_obj':grade_obj})


def sweetalert_delete(request):
    delete_id = request.POST.get('delete_id')
    # print('delete_id:',delete_id)
    delete_id = delete_id[2:]
    # print('delete_id:',delete_id)

    delete_flag = None
    try:
        Grade.objects.get(id=delete_id).delete()
        delete_flag = True
    except Exception as e:
        delete_flag = False
        print(e)
    return HttpResponse(delete_flag)