from django.contrib import admin
from models import TwitterAccount
from forms import TwitterForm

class TweetAdmin(admin.ModelAdmin):
    form = TwitterForm
    list_display = ('username', 'access_token_key', 'access_token_secret')
    
admin.site.register(TwitterAccount, TweetAdmin)
