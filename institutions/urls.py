from django.urls import path
from institutions.views import ListInstitution

urlpatterns = [
    path('institutions/', ListInstitution.as_view(), name='institution_list')
]