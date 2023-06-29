from django.conf import settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/', include('catalog.urls')),
    path('api/v1/', include('catalog.urls')),
    path('api/v1/users/', include('user.urls')),
    path('api/v1/google/', include('social_auth.urls')),
    path('api/v1/csv/', include('importcsv.url')),
    path('chat/', include('chat.urls'))
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path(r"debug/", include(debug_toolbar.urls))]
