

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path('', include('shop.urls')),
    path('post', include('post.urls')),
    path('visit', include('visit.urls')),
    path('api/' , include('visit_api.urls' , namespace='visit_api')),
    path('api/' , include('pictures_api.urls' , namespace='pictures_api')),
    path('api/' , include('shop_api.urls' , namespace='shop_api')),
    path('api/' , include('blog_api.urls' , namespace='blog_api')),
    path('api/' , include('feedback_api.urls' , namespace='feedback_api')),
    path('api/' , include('subscriber_api.urls' , namespace='subscriber_api')),
    path('admin/', admin.site.urls),  
    path('Account/', include('Account.urls')),
    path('Account/', include('Account.urls')),
    path('Account/', include('Account.urls')),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
