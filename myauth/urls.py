from django.urls import include, path
from rest_framework import routers
from myauth import views

app_name = 'myauth'

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('current_user/', views.current_user),
    path('users/', views.UserList.as_view())
]