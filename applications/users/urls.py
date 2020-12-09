from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('usuario',viewset=views.User)
router.register('usuario-create',viewset=views.UserCreate)
router.register('usuario-eliminar',viewset=views.DeleteUser)
router.register('usuario-editar',viewset=views.EditUser)

urlpatterns = [
    path('',include(router.urls))
]