"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from kulichtv import views
from users import views as uviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^stream/$', views.stream_feed, name='stream'),
    url(r'^index/$', views.IndexView.as_view(), name='index'),
    url(r'^games/new/$', views.GameAddView.as_view(), name='add_game'),
#    url(r'^register/$', uviews.UserRegistrationView.as_view(), name='registration'),
    url(r'^login/$', uviews.UserLoginView.as_view(), name='login_user'),
    url(r'^logout/$', uviews.dismissed, name='logout'),
    url(r'^communities/add/$', views.CommunityAddView.as_view(), name='add_community'),
    url(r'^communities/$', views.CommunityView.as_view(), name='communities'),
    url(r'^communities/(?P<pk>[0-9]+)/$', views.CommunityDetailView.as_view(), name='details_community'),
    url(r'^communities/(?P<pk>[0-9]+)/edit/$', views.CommunityUpdateView.as_view(), name='update_community'),
    url(r'^auth/$', uviews.twitter_login, name='auth'),
    url(r'^auth/twitter/callback/$', uviews.twitter_authenticated),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
