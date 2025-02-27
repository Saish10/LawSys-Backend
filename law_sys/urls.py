"""
URL configuration for law_sys project.

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
from django.urls import path
from django.urls.conf import include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

SchemaView = get_schema_view(
    openapi.Info(
        title="LawSys",
        default_version="v1",
        description="LawSys Operations",
        terms_of_service="",
        contact=openapi.Contact(email=""),
        license=openapi.License(name=""),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "swagger/",
        SchemaView.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "",
        include(("base.urls", "base"), namespace="base"),
    ),
    path(
        "",
        include(
            ("access_control.urls", "access_control"),
            namespace="access_control",
        ),
    ),
    path(
        "account/",
        include(("accounts.urls", "accounts"), namespace="accounts"),
    ),
    path(
        "case/",
        include(("cases.urls", "cases"), namespace="cases"),
    ),
    path(
        "document/",
        include(("documents.urls", "documents"), namespace="documents"),
    ),
    path(
        "defendant/",
        include(("defendants.urls", "defendants"), namespace="defendants"),
    ),
    path(
        "plaintiff/",
        include(("plaintiffs.urls", "plaintiffs"), namespace="plaintiffs"),
    ),
    path(
        "customer/",
        include(("customers.urls", "customers"), namespace="customers"),
    ),
]
