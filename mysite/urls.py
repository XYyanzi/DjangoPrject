"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from learn import views as learn_views
from polls import views as polls_views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', learn_views.add3, name='add3'),    # 添加index配置
    url(r'^add$', learn_views.add, name='add'),
    url(r'^new_add/(\d+)/(\d+)$', learn_views.add2, name='add2'),
    url(r'^showstring$', learn_views.show_string),
    url(r'^showlist$', learn_views.show_list),
    url(r'^showdict$', learn_views.show_dict),
    url(r'^showfor$', learn_views.show_for),
    url(r'^showif$', learn_views.show_if, name='showif'),
    url(r'^index$', polls_views.index)



]
