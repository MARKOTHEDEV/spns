from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from . import models
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
import os


def indexPage(request):



    return render(request,'index.html',{
        "all_service":models.ServiceModel.objects.all(),
        "all_researchInfor":models.ResearchInsightInfo.objects.all()
    })



def solutionsPage(request):return render(request,'soloutions.html',
{
        "all_service":models.ServiceModel.objects.all()
    }
)



def researchInsight(request):return render(request,'researchInsight.html')


def contactUs(request):return render(request,'contact.html')

def researchInsightDetailPage(request,ID=None):
    return render(request,'researchInsightDetailPage.html',{
        'object':models.ResearchInsightInfo.objects.get(id=ID),
        "object_para":models.ResearchInsightInfo.objects.get(id=ID).researchinsight_paragraph_set.all()
        })


def serviceDetail(request,pk=None):
    serviceDetailModel = models.ServiceModel.objects.get(id=pk)
    return render(request,'serviceDetail.html',{'service':serviceDetailModel})


def submitDataAndSendPDF(request,pk=None):

    "we will first get the data then send the data"
    name = ''
    email = ''
    Location = ''
    company = ''
    jobTitle = ''
    message = ''
    send_mail(
        'Subject here',
        'Here is the message.',
        'markothedevmail@gmail.com',
        ['ogechuwkumatthew@gmail.com'],
        fail_silently=False,
            )
    try:
        data = dict(request.POST)  
        print(data)  
        name = request.POST['name']
        email = request.POST['email']
        Location = request.POST['Location']
        company = request.POST['company']
        jobTitle = request.POST['job-title']
        # message= request.POST['message'] if request.POST['message'] else ""
        print(name,email,message)
        data = models.PeopleDataForPdf.objects.create(
            name=name,email=email,
            location=Location,
            company=company,jobTitle=jobTitle,message=message
        )
        data.save()
        # send_mail(
        # 'Subject here',
        # 'Here is the message.',
        # settings.EMAIL_HOST_USER,
        # ['markothedevmail@gmail.com'],
        # fail_silently=False,
        #     )
        messages.success(request, 'Thank you.. check your email for pdf')
        return HttpResponseRedirect(reverse('researchInsightDetail',args=[pk]))

    except:
        messages.error(request, 'Please PRovide required fields.')
        return HttpResponse("ss")
    
    # return redirect('/')