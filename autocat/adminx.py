import xadmin
from xadmin import views
from . forms import PersonForm
from .models import Person, Country

class PersonAdmin(object):
    form = PersonForm

xadmin.site.register(Person, PersonAdmin)

xadmin.site.register(Country)