from django.urls import path
from . import views


urlpatterns = [
    path('', views.indexPage),
    path('our-solution/',views.solutionsPage,name='our-solutions'),
    path('research-insight/',views.researchInsight,name='researchInsight'),
    path('contact/',views.contactUs,name='contact-us')

]