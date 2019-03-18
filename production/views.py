from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Merchandise,Detail
from .forms import MerchandiseForm
from django.views import generic
from django.urls import reverse


def merchandise_list(request):
    merchandises = Merchandise.objects.all()
    context = {
        'merchandises':merchandises
    }
    return render(request,'production/index.html',context)

def merchandise_add(request):
    if(request.method == 'POST'):
        form = MerchandiseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('merchandise:index'))
    else:
        form = MerchandiseForm()
        return render(request,'production/myform.html',{'form':form})

def merchandise_remove(request,p_id):
    merchandise = get_object_or_404(Merchandise,p_id)
    return HttpResponse(merchandise.mer_name)

def merchandise_update(request,p_id):
    return HttpResponse('update')
