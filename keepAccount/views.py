from django.shortcuts import render
from keepAccount.models import account
from django.contrib.auth.models import User
from .forms import editForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    costList=account.objects.filter(user=request.user).order_by('-date','-cost')
    if request.method == 'POST':
        form=editForm(request.POST)
        if form.is_valid():
            add=form.save(commit=False)
            add.user=request.user
            add.save()
            return HttpResponseRedirect(reverse('index'))
    return render(request,'keepAccount/index.html',{
        'editForm':editForm,
        'costList':costList,
    })

def update(request,id):
    item=account.objects.get(pk=id)
    form=editForm(request.POST or None, instance=item)
    if form.is_valid():
            add=form.save(commit=False)
            add.user=request.user
            add.save()
            return HttpResponseRedirect(reverse('index'))
    return render(request,'keepAccount/update.html',{
        'item':item,
        'form':form
    })


def search(request):
    if request.method == 'POST':
        searched=request.POST['searched']
        result=account.objects.filter(description__contains=searched)
        return render(request,'keepAccount/search.html',{
            'searched':searched,
            'result':result
        })
    else:
        return render(request,'keepAccount/search.html',{})

def delete(request,id):
    item=account.objects.get(pk=id)
    item.delete()
    return HttpResponseRedirect(reverse('index'))


def graph(request):
    typeSum=[]
    for types in ['食','衣','住','行','育','樂','其他']:
        sum=0
        for add in account.objects.filter(type=types):
            if add.user==request.user:
                 sum+=add.cost
        typeSum.append(sum)

        
    return render(request,'keepAccount/graph.html',{
        'typeSum':typeSum
    })