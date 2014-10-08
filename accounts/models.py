from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser,UserManager, PermissionsMixin,AbstractUser)
from django.core import validators
from django.utils import timezone
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.shortcuts import get_object_or_404


# Create your models here.
#class UserProfile(AbstractBaseUser, PermissionsMixin):
#    email = models.EmailField(verbose_name= 'email address', max_length=255, unique=True)
#    username = models.CharField(_('username'), max_length=30, unique=True,
#        help_text=_('Required. 30 characters or fewer. Letters, digits and '
#                    '@/./+/-/_ only.'),
#        validators=[
#            validators.RegexValidator(r'^[\w.@+-]+$', _('Enter a valid username.'), 'invalid')
#        ])
#    company = models.CharField(_('company'), max_length= 255, blank=False)
#    is_active = models.BooleanField(default=True)
#    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
#
#    objects = UserManager()
#    USERNAME_FIELD = 'username'
#    REQUIRED_FIELDS = ['company','email']
#
#    # On Python 3: def __str__(self):
#    def __unicode__(self):
#        return self.username
#
#    def get_full_name(self):
#        return self.company
#
#    def get_short_name(self):
#        "Returns the short name for the user."
#        return self.username
#
#    def has_perm(self, perm, obj=None):
#        return True
#
#    def has_module_perms(self, app_label):
#        return True


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    company = models.CharField(verbose_name=_('Company'), max_length=255, blank=False)
    location = models.CharField(verbose_name=_("location"), max_length=256, blank=True, null=True)
    contact = models.CharField(verbose_name=_('contact'), max_length=32, blank=True, null=True)
    phone = models.CharField(verbose_name=_('phone'), max_length=32, blank=True, null=True)

    def __unicode__(self):
        return self.company


@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs):
    if kwargs['created']:
        #create UserProfile on User created event
        user = User.objects.get(username=instance.username)
        p = UserProfile(user=user, company=instance.username)
        p.save()

@receiver(pre_delete, sender=User)
def delete_profile(sender, instance, **kwargs):
    user = User.objects.get(username=instance.username)
    p = get_object_or_404(UserProfile, user_id=user.pk)
    p.delete()



