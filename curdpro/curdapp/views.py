from django.shortcuts import render,redirect
from .models import  curdData

def homeview(request):
    data=curdData.objects.all()
    return render(request,'main.html',{'abc':data})
def formview(request):
    if request.method=='GET':
        return render(request,'formDate.html')
    else:
        curdData(
        name=request.POST['name'],
        date=request.POST['date'],
        relation=request.POST['relation'],
        mobile=request.POST['mobile'],
        professional=request.POST['professional'],
        comment=request.POST['comment']
        ).save()
        return redirect(homeview)
def dateview(request):
    data=curdData.objects.all()
    return render(request,'datatable.html',{'abc':data})
def dateentryview(request,id):
    data=curdData.objects.get(id=id)
    return render(request,'dateentry.html',{'abc':data})
def updateview(request,id):
    data= curdData.objects.get(id=id)
    return render(request,'update.html',{'data':data})
def updating_data(request,id):
    data=curdData.objects.get(id=id)
    data.name=request.POST['name']
    data.date=request.POST['date']
    data.relation=request.POST['relation']
    data.mobile=request.POST['mobile']
    data.professional=request.POST['professional']
    data.comment=request.POST['comment']
    data.save()
    return redirect(homeview)
def deleteview(request,id):
    data=curdData.objects.get(id=id)
    data.delete()
    return redirect(homeview)

def updateviews(request,id):
    data=curdData.objects.get(id=id)
    return render(request,'dateentry.html',{'abc':data})
def updatingview(request,id):
        data=curdData.objects.get(id=id)
        data.name=request.POST['name']
        data.date=request.POST['date']
        data.relation=request.POST['relation']
        data.mobile=request.POST['mobile']
        data.professional=request.POST['professional']
        data.comment=request.POST['comment']
        data.save()
        return redirect(homeview)
