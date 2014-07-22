from django.utils.translation import ugettext as _
from django import template
register = template.Library()

@register.filter(name='approve_state')
def approve_state(value):
    if value:
        return _('Approved')
    else:
        return _('Deny')
