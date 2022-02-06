from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('steps/', include('steps.urls')),
    path('admin/', admin.site.urls),
]
