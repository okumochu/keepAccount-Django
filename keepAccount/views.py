from django.shortcuts import render,redirect
from keepAccount.models import account,assets
from django.contrib.auth.models import User
from .forms import editForm,assetForm
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
import csv

def index(request):
    costList=account.objects.filter(user=request.user).order_by('-date','-cost')
    if request.method == 'POST':
        form=editForm(request.POST)
        if form.is_valid():
            #update asset
            if assets.objects.filter(user=request.user).exists():
                items=assets.objects.get(user=request.user)
                if form.cleaned_data['type']=='收入':
                    items.asset+=form.cleaned_data['cost']
                else:
                    items.asset-=form.cleaned_data['cost']
                items.save()

            add=form.save(commit=False)
            add.user=request.user
            add.save()
            return HttpResponseRedirect(reverse('index'))
    if assets.objects.filter(user=request.user).exists():
        items=assets.objects.get(user=request.user)
        return render(request,'keepAccount/index.html',{
            'editForm':editForm,
            'costList':costList,
            'items':items.asset
        })
    return render(request,'keepAccount/index.html',{
            'editForm':editForm,
            'costList':costList,
        })

def update(request,id):
    item=account.objects.get(pk=id)
    form=editForm(request.POST or None, instance=item)
    temp=item.cost
    if form.is_valid():
            #update asset
            if assets.objects.filter(user=request.user).exists():
                items=assets.objects.get(user=request.user)
                if form.cleaned_data['type']=='收入':
                    if temp>form.cleaned_data['cost']:
                        items.asset-=abs(temp-form.cleaned_data['cost'])
                    else:
                        items.asset+=abs(temp-form.cleaned_data['cost'])
                else:
                    if temp>form.cleaned_data['cost']:
                        items.asset+=abs(temp-form.cleaned_data['cost'])
                    else:
                        items.asset-=abs(temp-form.cleaned_data['cost'])
                items.save()
            add=form.save(commit=False)
            add.user=request.user
            add.save()
            return HttpResponseRedirect(reverse('index'))   
    if assets.objects.filter(user=request.user).exists():
        items=assets.objects.get(user=request.user)
        return render(request,'keepAccount/update.html',{
            'editForm':editForm,
            'item':item,
            'form':form,
            'items':items.asset
            })
    return render(request,'keepAccount/update.html',{
            'editForm':editForm,
            'item':item,
            'form':form,

            })


def search(request):
    if request.method == 'POST':
        searched=request.POST['searched']
        result=account.objects.filter(description__contains=searched,user=request.user).order_by('-date','-cost')
        return render(request,'keepAccount/search.html',{
            'editForm':editForm,
            'searched':searched,
            'result':result
        })
    else:
        return render(request,'keepAccount/search.html',{
            'editForm':editForm,
        })

def delete(request,id):
    accounts=account.objects.get(pk=id)

    if assets.objects.filter(user=request.user).exists():
        item=assets.objects.get(user=request.user)
        if accounts.type=='收入':
            item.asset-=accounts.cost
        else:
            item.asset+=accounts.cost
        item.save()
    accounts.delete()
    return HttpResponseRedirect(reverse('index'))


def graph(request):
    typeSum=[]
    for types in ['食','衣','住','行','育','樂','收入','其他']:
        sum=0
        for add in account.objects.filter(type=types):
            if add.user==request.user:
                 sum+=add.cost
        typeSum.append(sum)
    if assets.objects.filter(user=request.user).exists():
        items=assets.objects.get(user=request.user)
        return render(request,'keepAccount/graph.html',{
            'editForm':editForm,
            'typeSum':typeSum,
            'items':items.asset
        })
    return render(request,'keepAccount/graph.html',{
        'editForm':editForm,
        'typeSum':typeSum,
    })

def generateCSV(request):
    response=HttpResponse(content_type='text/csv')
    response.charset = 'utf-8-sig'
    response['Content-Disposition']='attachment; filename=account.csv'

    # create csv writer
    writer=csv.writer(response)
    costList=account.objects.filter(user=request.user)
    writer.writerow(['date','type','description','cost'])

    for item in costList:
        writer.writerow([item.date,item.type,item.description,item.cost])

    return response

def overview(request):
    if request.method=='POST':
        searched=request.POST['searched']
        result=account.objects.filter(date__contains=searched).order_by('-date','-cost')
        typeSum=[0,0,0,0,0,0,0,0]
        for add in result:
            index=0
            for types in ['食','衣','住','行','育','樂','收入','其他']:
                if add.user==request.user and str(add.type)==types:
                    typeSum[index]+=add.cost
                index+=1     

        totalCost=typeSum[0]+typeSum[1]+typeSum[2]+typeSum[3]+typeSum[4]+ typeSum[5]+typeSum[7]
        balance=typeSum[6]-totalCost  
        if assets.objects.filter(user=request.user).exists():
            item=assets.objects.get(user=request.user)
            quotas=int(item.expectedCost)-int(totalCost)
            items=assets.objects.get(user=request.user)
            return render(request,'keepAccount/overview.html',{
                'searched':searched,
                'typeSum':typeSum,
                'result':result,
                'editForm':editForm,
                'user':request.user,
                'totalCost':totalCost,
                'balance':balance,
                'quotas':quotas,
                'items':items.asset
             })
        else:
            return render(request,'keepAccount/overview.html',{
                'searched':searched,
                'typeSum':typeSum,
                'result':result,
                'editForm':editForm,
                'user':request.user,
                'totalCost':totalCost,
                'balance':balance,
             })
    else:
        if assets.objects.filter(user=request.user).exists():
            items=assets.objects.get(user=request.user)
            return render(request,'keepAccount/overview.html',{
                'editForm':editForm,
                'items':items.asset
            })
        else: return render(request,'keepAccount/overview.html',{
                'editForm':editForm,
            })
        

def asset(request):

    if request.method=="POST":
        if assets.objects.filter(user=request.user).exists():
            item=assets.objects.get(user=request.user)
            form=assetForm(request.POST or None, instance=item)
            if form.is_valid():
                    add=form.save(commit=False)
                    add.user=request.user
                    add.save()
                    return HttpResponseRedirect(reverse('index'))          
        else:
            form=assetForm(request.POST)
            if form.is_valid():
                    add=form.save(commit=False)
                    add.user=request.user
                    add.save()
                    return HttpResponseRedirect(reverse('index'))
    else: 
        if assets.objects.filter(user=request.user).exists():     
            item=assets.objects.get(user=request.user)
            form=assetForm(request.POST or None, instance=item) 
            return render(request,'keepAccount/asset.html',{
                'editForm':editForm,
                'item':item,
                'form':form,
                'items':item.asset
            })   
        else:
            return render(request,'keepAccount/asset.html',{
            'editForm':editForm,
            'form':assetForm,
            })
           
    