from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as django_views

app_name='main'

urlpatterns=[
    path('', index),
    path('blog/', blog),
    path('blog/<int:pk>/', posting, name="posting"),
    path('blog/<int:pk>/comment/', comment, name='comment'),
    path('blog/<int:pk>/del_comment/<int:pk2>', del_comment, name='comment'),
    path('blog/new_post/', new_post),
    path('blog/<int:pk>/remove/', remove_post),
    path('blog/register/', register),
    path('blog/login/', django_views.LoginView.as_view(template_name='main/login.html')),
    path('blog/<uidb64>/<token>/', UserActivateView.as_view, name='activate'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)