from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _


class BaseProtecdArea(models.Model):
    name = models.CharField(_('name'), max_length=254)

    category = models.CharField(max_length=254, null=True, blank=True)
    creation_year = models.CharField(max_length=254, null=True, blank=True)
    country = models.CharField(max_length=254, null=True, blank=True)

    geometry = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()


class ProtectedAreaBrasil(BaseProtecdArea):
    # Brazilian protected areas, from Ministério do Meio Ambiente (Minstry of Enviroment)
    id_uc = models.CharField(max_length=254, null=True, blank=True)
    id_wcmc2 = models.CharField(max_length=254, null=True, blank=True)

    group = models.CharField(max_length=254, null=True, blank=True)
    esfera5 = models.CharField(max_length=254, null=True, blank=True)
    gid7 = models.CharField(max_length=254, null=True, blank=True)
    precision = models.CharField(max_length=254, null=True, blank=True)
    legal_act = models.CharField(max_length=254, null=True, blank=True)
    dt_ultim10 = models.CharField(max_length=254, null=True, blank=True)
    codigo_u11 = models.CharField(max_length=254, null=True, blank=True)
    org_name = models.CharField(max_length=254, null=True, blank=True)

