from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('helloviewset',views.HelloApiViewSet,basename='hello-viewset')
router.register('hellomodelviewset',views.UserProfileViewset, 'hello-modelviewset')
router.register('status', views.ProfileFeedItemViewSet, 'status')

urlpatterns = [
    path('hello/', views.HelloAPIView.as_view()),
    path('login/', views.UserProfileLogin.as_view()),
    path('', include(router.urls))
]