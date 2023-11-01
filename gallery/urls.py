from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



app_name = 'gallery'
urlpatterns = [
    path('', views.image_list, name='image_list'),
    path('upload/', views.image_upload, name='image_upload'),
    path('images/delete/<int:image_id>/', views.image_delete, name='image_delete'),
    # path('images/<int:image_id>/', views.image_detail, name='detail'),
    # path('images/delete/<int:image_id>/', views.image_delete, name='delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)