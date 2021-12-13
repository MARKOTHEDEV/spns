from django.db import models

# Create your models here.



class ServiceModel(models.Model):
    title = models.CharField(max_length=300)
    main_content = models.TextField()
    intro_content=models.TextField(max_length=300)
    icon_class = models.CharField(max_length=200,default="..")


    def __str__(self):return f'{self.title}'


class PeopleDataForPdf(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    location = models.CharField(max_length=300)
    company = models.CharField(max_length=300)
    jobTitle = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):return f'{self.name}'



class ResearchInsightInfo(models.Model):
    cover_image = models.ImageField(upload_to='spns_cover_image/')
    heading= models.CharField(max_length=350)
    intro_content = models.TextField(default='..')

    def __str__(self):return f'{self.heading}'


class researchinsight_ParaGraph(models.Model):
    researchinsightinfo = models.ForeignKey(ResearchInsightInfo,on_delete=models.CASCADE)
    paragraph = models.TextField()

    # defs

