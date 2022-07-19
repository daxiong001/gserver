from django.shortcuts import render, redirect
from ipsserver.models import Department, UserInfo
from ipsserver.forms import userforms


# Create your views here.
def depart_list(request):
    """部门列表"""
    departList = Department.objects.all()
    return render(request, 'depart_list.html', {"depart_list": departList})


def depart_add(request):
    """部门添加"""
    if request.method == "GET":
        return render(request, "depart_add.html")
    title = request.POST.get("title")
    Department.objects.create(title=title)
    return redirect("/depart/list/")


def depart_delete(request):
    """删除部门"""
    nid = request.GET.get('nid')
    Department.objects.filter(id=nid).delete()
    return redirect('/depart/list/')


def depart_update(request, nid):
    """编辑部门"""
    if request.method == "GET":
        rowObject = Department.objects.filter(id=nid).first()
        return render(request, "depart_update.html", {"title": rowObject})
    title = request.POST.get("title")
    Department.objects.filter(id=nid).update(title=title)
    return redirect("/depart/list/")


def userList(request):
    """用户列表"""
    userAll = UserInfo.objects.all()
    return render(request, 'user_list.html', {"userAll": userAll})


def addUser(request):
    """原始添加用户"""
    if request.method == "GET":
        context = {
            "gender_choices": UserInfo.gender_choices,
            "departList": Department.objects.all()
        }
        return render(request, "user_add.html", context)
    name = request.POST.get("name")
    age = request.POST.get("age")
    account = request.POST.get("account")
    time = request.POST.get("time")
    sex = request.POST.get("sex")
    depart = request.POST.get("depart")
    UserInfo.objects.create(name=name, age=age, account=account, create_time=time, gender=sex, depart_id=depart)
    return redirect("/user/list/")


def addUserModelForm(request):
    if request.method == "GET":
        form = userforms.UserModelForm()
        return render(request, 'user_model_form_add.html', {'form': form})

    form = userforms.UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/user/list/")
    return render(request, 'user_model_form_add.html', {'form': form})


def userEdit(request, nid):
    rowObject = UserInfo.objects.filter(id=nid).first()
    if request.method == "GET":
        form = userforms.UserModelForm(instance=rowObject)
        return render(request, "user_edit.html", {"form": form})
    form = userforms.UserModelForm(data=request.POST, instance=rowObject)
    if form.is_valid():
        form.save()
        return redirect("/user/list/")
    return render(request, 'user_edit.html', {"form": form})


def userDelete(request):
    nid = request.GET.get("nid")
    UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list/")
