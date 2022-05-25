from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from api.views import *


router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('laundry', LaundryViewSet, basename='laundry')
router.register('laundry-entries', LaundryEntryViewSet, basename='laundry-entries')
router.register('rooms', RoomsViewSet, basename='rooms')
router.register('room-entries', RoomEntryViewSet, basename='room-entries')
urlpatterns = router.urls

urlpatterns.append(path('rooms-entries/<int:year>/<int:month>/<int:day>/', room_entry_for_day_list, name='room-entry-for-day-list'))
urlpatterns.append(path('laundry-entries/<int:year>/<int:month>/<int:day>/', laundry_entry_for_day_list, name='laundry-entry-for-day-list'))

'''user_lisr = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('users/', user_lisr, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detatil'),
]

urlpatterns = format_suffix_patterns(urlpatterns)'''
