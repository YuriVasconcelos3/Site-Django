from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import PostList, PostList2, DetailView, enviar_email

urlpatterns = [
    url(r'^(?:index/|home/)?$', views.home, name='home'),
    url(r'^blog/$', PostList.as_view(), name='blog'),
    url(r'^enviar_email/$', enviar_email, name='enviar_email'),
    url(r'^membros/$', PostList2.as_view(), name='membros'),
    url(r'^(?P<slug>[\w-]+)/$', DetailView.as_view(), name='post_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
