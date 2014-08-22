from django.utils.translation import ugettext as _
from django import template
from enterprise.models import Selection, NOTIFICATION_TYPE_CHOICES
register = template.Library()

@register.filter(name='approve_state')
def approve_state(value):
    if value:
        return _('Approved')
    else:
        return _('Deny')


@register.filter(name='vote_state')
def vote_state(value, arg):
    print arg
    if value:
        return _('Thumbs Up')
    elif arg is None:
        return _('Not yet voted')
    else:
        return _('Thumbs Down')

@register.filter(name='vote_result')
def vote_result(value):
    status = _('Not yet voted')
    total = Selection.objects.filter(project_id=value).count()
    passed_count = Selection.objects.filter(project_id=value, passed=True).count()

    if total == 0:
        up_ratio = 0
        return status
    else:
        up_ratio = passed_count*1.0/total

    print '{}:{}:{}'.format(passed_count, total, up_ratio)

    if up_ratio >= 2*1.0/3:
        status = _('Thumbs Up')
    elif up_ratio > 0:
        status = _('Thumbs Down')

    return status


@register.filter(name='notification_type')
def notification_type(value):
    for choice in NOTIFICATION_TYPE_CHOICES:
        if choice[0] == value:
            return choice[1];
    return ''
