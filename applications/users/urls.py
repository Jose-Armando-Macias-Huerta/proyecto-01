from django.urls import path, include
#
from rest_framework import routers
#
from . import views

router = routers.DefaultRouter()

router.register('User-list', viewset=views.listUserAdmin)
router.register('User-create', viewset=views.createUserAdmin)
router.register('User-delete', viewset=views.deleteUser)
router.register('User-edit', viewset=views.edittUserAdmin)

urlpatterns = [
    path('',include(router.urls))
]
