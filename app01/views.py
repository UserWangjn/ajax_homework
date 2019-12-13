from django.shortcuts import render,HttpResponse

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


def upload_file(request):
    if request.method == 'POST':
        print(request.POST)
        file = request.POST.get('formData')
        print(file)
        return HttpResponse(str(file))

    return render(request,'upload_file.html')