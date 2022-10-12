from django.urls import path, include
from .views import hello_blog
from .views import post_detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', hello_blog, name="home_blog"),
    path('post/<int:id>/', post_detail, name="post_detail")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
