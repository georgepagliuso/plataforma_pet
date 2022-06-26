from django.conf import settings
from django.contrib import admin
from django.urls import path

from adocao_pet import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('adocao_pet/<int:pet_id>/', views.pet_detail, name='pet_detail')
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)