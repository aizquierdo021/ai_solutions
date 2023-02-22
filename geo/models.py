from django.db import models
from django.contrib.gis.db import models


# Create your models here.
class MunicipalitiesNl(models.Model):
    geom = models.GeometryField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'municipalities_nl'