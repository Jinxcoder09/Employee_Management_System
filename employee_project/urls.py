"""
URL configuration for employee_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from employees.views import EmployeeViewSet, DepartmentViewSet
from attendance.views import AttendanceViewSet
from performance.views import PerformanceViewSet
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from drf_yasg.generators import OpenAPISchemaGenerator
from .views import dashboard

class CustomSchemaGenerator(OpenAPISchemaGenerator):
    def get_security_definitions(self, *args, **kwargs):
        return {
            "Token": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header"
            }
        }
        
schema_view = get_schema_view(
    openapi.Info(
        title="Employee API",
        default_version='v1',
        description="API Docs",
    ),
    public=True,
    permission_classes=(AllowAny,),
    authentication_classes=[TokenAuthentication],
    url='https://greentree.up.railway.app',
    generator_class = CustomSchemaGenerator,
)

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'performance', PerformanceViewSet)




urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),  # for Token Auth
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
]
