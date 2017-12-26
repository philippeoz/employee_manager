from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from backend.core.models.employee import Employee

from backend.core.serializers import EmployeeSerializer


class EmployeeMixin(object):
    """
    Mixin to inherit from.
    Here we're setting the query set and the serializer
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeList(EmployeeMixin, ListCreateAPIView):
    """
    Return a list of all the employees, or
    create new ones
    """
    pass


class EmployeeDetail(EmployeeMixin, RetrieveUpdateDestroyAPIView):
    """
    Return a specific employee, update it, or delete it.
    """
    pass
