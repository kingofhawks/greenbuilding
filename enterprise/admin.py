from django.contrib import admin
from models import Submission,Project,ApplicationReview,SelfEvaluation,Selection, PM10, ProgressMonitor
from django.utils.translation import ugettext as _


class SubmissionAdmin(admin.ModelAdmin):
    fieldsets = [('Project Info',{'fields':['project','grade']}),(None,{'fields':['date']})]
    list_display = ('project', 'grade','date')
    actions = ['change_grade']

    def change_grade(self, request, queryset):
        rows_updated = queryset.update(grade=1)
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)
    change_grade.short_description = _("Change Grade")

admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Project)
admin.site.register(ApplicationReview)
admin.site.register(SelfEvaluation)
admin.site.register(Selection)
admin.site.register(PM10)
admin.site.register(ProgressMonitor)

