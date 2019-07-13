from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import model_form_upload, index_view


urlpatterns = [
    path('complaint/', model_form_upload),
    path('', index_view, name = 'home')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
