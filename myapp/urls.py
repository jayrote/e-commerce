from django.contrib import admin
from django.urls import path
from .views import products_list,userLogin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',products_list,name='products_list'),
    path('login/',userLogin, name='login'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)