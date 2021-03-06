from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

from rest_framework import routers
from Movies.views import Movies
from Profiles.views import Profiles, Register

router = routers.DefaultRouter()
router.register('Movies', Movies, basename='Movies')
router.register('Profiles', Profiles, basename='Profiles')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register', Register.as_view()),
    path('api/', include((router.urls, 'Movies'), namespace='Movies')),
    path('api/', include((router.urls, 'Profiles'), namespace='Profiles')),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
]


for url in router.urls:
    print(url)
