from django.shortcuts import render




def indexPage(request):

    return render(request,'index.html',{})



def solutionsPage(request):return render(request,'soloutions.html',{})



def researchInsight(request):return render(request,'researchInsight.html')


def contactUs(request):return render(request,'contact.html')