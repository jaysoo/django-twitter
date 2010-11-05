from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

import twitter

class TwitterAccount(models.Model):
    username = models.CharField(_("username"), max_length=200, unique=True, null=False, blank=False)
    access_token_key = models.CharField(_("access token key"), max_length=200, null=False, blank=False)
    access_token_secret = models.CharField(_("access token secret"), max_length=200, null=False, blank=False)

    def __unicode__(self):
        return self.username
    
    def post_status_update(self):
        try:
            api = twitter.Api(consumer_key=settings.TWITTER_CONSUMER_KEY,
                    consumer_secret=settings.TWITTER_CONSUMER_SECRET,
                    access_token_key=self.access_token_key,
                    access_token_secret=self.access_token_secret)
            return api.PostUpdate(mesg)
        except:
           return False

    class Meta:
        verbose_name = _("twitter account")
        verbose_name_plural = _("twitter accounts")
