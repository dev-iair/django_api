"""
URL configuration for django_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

schema_view_first = get_schema_view(
    openapi.Info(
        title="Django First API",
        default_version='v1',
        description="Heidi First API description",
        terms_of_service="",
        contact=openapi.Contact(email="jhlee@aistudio.co.kr"),
        license=openapi.License(name=""),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    urlconf='first.urls',
    patterns=[re_path(r'^first/', include('first.urls'))]
)

schema_view_second= get_schema_view(
    openapi.Info(
        title="Django Second API",
        default_version='v1',
        description="Heidi Second API description",
        terms_of_service="",
        contact=openapi.Contact(email="jhlee@aistudio.co.kr"),
        license=openapi.License(name=""),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    urlconf='second.urls',
    patterns=[re_path(r'^second/', include('second.urls'))]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/swagger/', schema_view_first.with_ui('swagger', cache_timeout=0), name='schema-swagger-first'),
    path('first/redoc/', schema_view_first.with_ui('redoc', cache_timeout=0), name='schema-redoc-first'),
    path('second/swagger/', schema_view_second.with_ui('swagger', cache_timeout=0), name='schema-swagger-second'),
    path('second/redoc/', schema_view_second.with_ui('redoc', cache_timeout=0), name='schema-redoc-second'),
    path('first/', include('first.urls')),
    path('second/', include('second.urls')),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
]