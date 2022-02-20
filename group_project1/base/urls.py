from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('',views.home, name="home"),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/',views.userProfile,name='profile'),
    path('image_upload/', views.uploading_image_view, name = 'image_upload'),
    path('success/', views.success, name = 'success'),
    path('images', views.display_images, name = 'images'),
]

# For handling photos in DEBUG 
# https://www.geeksforgeeks.org/python-uploading-images-in-django/ 
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)