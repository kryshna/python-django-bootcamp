"""bootcamp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from blog.views import home,contact,about,detail,createblog,signup
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login,logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', signup, name='signup'), 
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, {'next_page':'home'}, name='logout'),
    url(r'^$',home, name='home'),
    url(r'^blog/create$',createblog, name='create-blog'),
    url(r'^contact/$',contact, name='contact'),
    url(r'^about/$',about, name='about'),
    url(r'^blog/detail/(?P<pk>\d+)/$',detail, name='detail'),#\d = digit ,+ = one or more

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)