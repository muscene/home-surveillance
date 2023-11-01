from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .recognition_logic import recognize_faces  # Import the recognize_faces function
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('Attendance/', views.members, name='Attendance'),
    path('members/details/<int:id>', views.details, name='details'),
    path('members/display-image/', views.image_view, name='image_view'),
    path('members/read-csv/', views.read_csv, name='read_csv'),
    path('members/member-images/', views.member_images, name='member_images'),
    # path('images/<str:image_name>', views.serve_image, name='serve_image'),
    path('members/camera-feed/', views.camera_feed, name='camera_feed'),
    # path('image-list/', views.image_list, name='image_list'),
    # path('image_list/', views.image_list, name='image_list'),
    # path('members//', views.camera_feed.as_view(), name='camera_feed'),
    # path('member_list/', views.member_list, name='member_list'),
    # path('member_list/<int:id>/', views.member_details, name='member_details'),
    # path('upload_image/', views.upload_image, name='upload_image'),
    # path('view_unrecognized_faces/', views.view_unrecognized_faces,name='view_unrecognized_faces'),
    # path('view_unrecognized_faces/', views.view_unrecognized_faces, name='view_unrecognized_faces'),

    path('upload/', views.upload_image, name='upload_image'),

    # Add more URL patterns as needed
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)