from django.http import Http404
from rest_framework.response import Response

from .models import MunicipalitiesNl
from rest_framework_gis.pagination import GeoJsonPagination
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import generics, status
from rest_framework.views import APIView


class LocationSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = MunicipalitiesNl
        fields = '__all__'
        geo_field = 'geom'
        auto_bbox = True


class MyPaginator(GeoJsonPagination):
    page_size = 10
    max_page_size = 100


class MunicipalitiesNlLocationList(generics.ListCreateAPIView):
    queryset = MunicipalitiesNl.objects.all()
    serializer_class = LocationSerializer
    pagination_class = MyPaginator


class MunicipalitiesDetail(APIView):
    def get_object(self, pk):
        try:
            return MunicipalitiesNl.objects.get(pk=pk)
        except MunicipalitiesNl.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        municipality = self.get_object(pk)
        serializer = LocationSerializer(municipality)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        municipality = self.get_object(pk)
        municipality.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
