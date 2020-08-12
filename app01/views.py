from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
from app01 import models



def publisher_list(request):

    all_publisher = models.Publisher.objects.all()


    return render(request,'publisher_list.html',{"all_publisher":all_publisher})



def publisher_add(request):
    if request.method == 'POST':
        # post请求
        # 获取用户提交的数据
        pub_name = request.POST.get('pub_name')
        if not pub_name:
            # 输入为空
            return render(request, 'publisher_add.html', {'error': '出版社名称不能为空'})

        if models.Publisher.objects.filter(name=pub_name):
            # 数据库中有重复的名字
            return render(request, 'publisher_add.html', {'error': '出版社名称已存在'})

        # 将数据新增到数据库中
        ret = models.Publisher.objects.create(name=pub_name)
        print(ret, type(ret))
        # 返回一个重定向到展示出版社的页面
        return redirect('/publisher_list/')

        # get请求返回一个页面，页面中包含form表单
    return render(request, 'publisher_add.html')

def publisher_delete(request):

    pk = request.GET.get('pk')

    models.Publisher.objects.filter(id = pk).delete()
    print("1111")
    return redirect('/publisher_list/')

#编辑出版社
def publisher_edit(request):
    pk = request.GET.get('pk')

    pub_obj = models.Publisher.objects.get(id=pk)
    if request.method == 'GET':
        # get  返回一个页面 页面包含form表单  input有原始的数据
        return render(request, 'publisher_edit.html', {'pub_obj': pub_obj})
    else:
        # post
        # 获取用户提交的出版社的名称
        pub_name = request.POST.get('pub_name')

        # 修改数据库中对应的数据
        pub_obj.name = pub_name  # 只是在内存中修改了
        pub_obj.save()  # 将修改操作提交的数据库
        # 返回重定向到展示出版社的页面
        return redirect('/publisher_list/')

