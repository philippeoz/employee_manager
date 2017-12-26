from django.conf.urls import url

from backend.core.views import EmployeeList
from backend.core.views import EmployeeDetail

from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    url(r'^(?P<pk>[0-9]+)', csrf_exempt(EmployeeDetail.as_view())),
    url(r'^', csrf_exempt(EmployeeList.as_view())),
]
