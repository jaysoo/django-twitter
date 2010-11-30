django-twitter
============

Simple application that provides a way to easily add Twitter accounts through Django admin.

Dependencies
------------

This Django app uses the [python-twitter](http://code.google.com/p/python-twitter/) library. Make sure you install at least version 0.8.

Not use easy_install for python-twitter module because isn't at 0.8 version, but you must clone main repository by http://code.google.com/p/python-twitter/source/checkout.

Clone main repository:

hg clone https://python-twitter.googlecode.com/hg/ python-twitter

You will also need oauth2 and django (obviously). Both can be installed using  easy_install or pip.


Register Twitter app
--------------------

If you don't have an app registered with Twitter yet, you'll need to do so before getting started.

See: [http://dev.twitter.com/apps](http://dev.twitter.com/apps)

Note during registration Twitter-app:

Select "Browser" into "Application Type" and put correct url into "Callback URL" (es. http://someip/authorize/)

Select correct main url/ip or location into "Sites" of Django Administration dashboard

Project Settings
----------------

django-twitter required two settings in the project.

    TWITTER_CONSUMER_KEY = "put your app's key here"
    TWITTER_CONSUMER_SECRET = "put your app's secret here"

The consumer key and secret are provided by Twitter. You can get them by viewing your app's details.

You also need to add django_twitter to project.

    INSTALLED_APPS = (
        ...
        'django_twitter',
    )

And don't forget to syncdb! ;)


Add to urls.py
--------------

Add an entry for django-twitter to your project's `urls.py`.

    urlpatterns = patterns('',
        ...
        (r'^django_twitter/', include('django_twitter.urls')),
        ...
    )


That's it!
----------

You should now see the django_twitter application in your Django admin. 

When adding an account, simply press the ``Retrieve credentials from Twitter`` button, and it'll pull in everything you need.

You can now use your consumer key, consumer secret, access key, access secret to post messages to Twitter on behalf of your Twitter account.

For more details on how to use the Twitter API using Python see [python-twitter](http://code.google.com/p/python-twitter/)
