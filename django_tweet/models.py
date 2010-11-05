from django.db import models
from django.utils.translation import ugettext_lazy as _

class TwitterAccount(models.Model):
    username = models.CharField(_("username"), max_length=200, unique=True, null=False, blank=False)
    access_token_key = models.CharField(_("access token key"), max_length=200, null=False, blank=False)
    access_token_secret = models.CharField(_("access token secret"), max_length=200, null=False, blank=False)

    def __unicode__(self):
        return self.username
    
    class Meta:
        verbose_name = _("twitter account")
        verbose_name_plural = _("twitter accounts")
