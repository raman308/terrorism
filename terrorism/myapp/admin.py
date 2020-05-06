from django.contrib import admin
from myapp.models import LatestNews
from myapp.models import Agencies
from myapp.models import MostWantedCriminals
from myapp.models import Person



# Register your models here.


admin.site.register(LatestNews)
admin.site.register(Agencies)
admin.site.register(MostWantedCriminals)
admin.site.register(Person)


