from django.contrib import admin

from . import models

admin.site.register(models.ServiceModel)
admin.site.register(models.PeopleDataForPdf)





class researchinsight_ParaGraphConten(admin.TabularInline):
    model = models.researchinsight_ParaGraph
    extra=1

class ResearchInsightInfoAdmin(admin.ModelAdmin):
    fieldsets=[(None,{'fields':['heading','cover_image','intro_content',]})]
    inlines=[researchinsight_ParaGraphConten]


admin.site.register(models.ResearchInsightInfo,ResearchInsightInfoAdmin)

