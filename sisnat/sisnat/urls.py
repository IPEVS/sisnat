from animal import views

from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('', RedirectView.as_view(url='/home_page/')),
    path('sisnat/', admin.site.urls),
    path('home_page/', views.home_page),
    path('pdf/', views.pdf_page),
]
if settings.DEBUG:
    urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)