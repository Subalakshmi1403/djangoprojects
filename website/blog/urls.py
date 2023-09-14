from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.allpost,name='allposts'),
    path('<int:blog_id>/',views.detial,name='detial'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
