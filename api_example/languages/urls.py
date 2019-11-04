from django.urls import path, include
from . import views 
from rest_framework import routers 

router = routers.DefaultRouter()
router.register('Register', views.LanguageView)
# router.register('Login',views.Login)

urlpatterns = [
    path('', include(router.urls))
]
