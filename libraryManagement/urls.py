from django.urls import path, include, re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Import views
import libraryManagement.error_handlers
from libraryManagement.views import AdminSignupView, home_view

# Swagger API Documentation Configuration
schema_view = get_schema_view(
    openapi.Info(
        title="Library Management API",
        default_version='v1',
        description="API documentation for managing books, users, and authentication.",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[AllowAny],  # Allow everyone to access docs
)

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),

    # API Endpoints
    path('api/', include('library.urls')),  # Scoped library APIs under /api/library/
    path('api/admin/signup/', AdminSignupView.as_view(), name='admin-signup'),
    path('api/admin/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/admin/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API Documentation URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]

# Custom Error Handlers
handler404 = 'libraryManagement.error_handlers.custom_404_handler'
handler401 = 'libraryManagement.error_handlers.custom_401_handler'

# Serve static files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
