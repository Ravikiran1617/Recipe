from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('receipes/', views.receipes, name='receipes'), 
    path('delete_receipe/<int:id>',views.delete_receipe, name='delete_receipe'),
    path('update_receipe/<int:id>',views.update_receipe, name='update_receipe'),

]

# Add this block to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
