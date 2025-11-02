from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]

# Serve static and media files always
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
