"""pbbdesablimbing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

from guestpage import views as guestpageView

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_page'),
    path('', guestpageView.index, name='guest_index'),
    path('wp/', guestpageView.wpindex, name='wp_index'),
    path('wp/insert/', guestpageView.wpInsertPage, name='wp_insert'),
    path('wp/create/', guestpageView.wpCreate, name='wp_create'),
    path('wp/edit/<int:pk>/', guestpageView.wpEditPage, name='wp_edit'),
    path('wp/edit/<int:pk>/update/', guestpageView.wpUpdate, name='wp_update'),
    path('wp/delete/<int:pk>', guestpageView.wpDelete, name='wp_delete'),

    path('sppt/', guestpageView.spptindex, name='sppt_index'),
    path('sppt/insert/', guestpageView.spptInsertPage, name='sppt_insert'),
    path('sppt/create/', guestpageView.spptCreate, name='sppt_create'),
    path('sppt/edit/<int:pk>/', guestpageView.spptEditPage, name='sppt_edit'),
    path('sppt/edit/<int:pk>/update/',
         guestpageView.spptUpdate, name='sppt_update'),
    path('sppt/delete/<int:pk>', guestpageView.spptDelete, name='sppt_delete'),

    path('trx/', guestpageView.trxindex, name='trx_index'),
    path('trx/insert/', guestpageView.trxInsert, name='trx_insert'),
    path('trx/create/', guestpageView.trxCreate, name='trx_create'),
]
