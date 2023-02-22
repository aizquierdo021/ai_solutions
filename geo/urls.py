from django.urls import path

from . import views

urlpatterns = [
    # ex: /geo
    path('/', views.MunicipalitiesNlLocationList.as_view()),
    path('/<int:pk>', views.MunicipalitiesDetail.as_view())
]
