from django.urls import path

from measurement.views import SensorUpdateView, SensorView, MeasurementsView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    # path('sensors/', SensorViewSet.as_view(
    #     {'get': 'list',
    #      'post': 'create'})),
    # path('sensors/<pk>/', SensorViewSet.as_view(
    #     {'get': 'retrieve',
    #      'patch': 'update'})),
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', SensorUpdateView.as_view()),
    path('measurements/', MeasurementsView.as_view()),
]
