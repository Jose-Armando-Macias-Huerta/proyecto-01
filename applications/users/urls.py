from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.SimpleRouter()

router.register('usuario',viewset=views.UserSet)
router.register('usuario/eliminar',viewset=views.DeleteUser)
router.register('usuario/login',viewset=views.login)

urlpatterns = [
    path('',include(router.urls))
]