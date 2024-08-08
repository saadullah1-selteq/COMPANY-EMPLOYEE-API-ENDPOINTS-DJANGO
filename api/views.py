from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import Company, Employee
from companyapi.serializers import CompanySerializer, EmployeeSerializer


# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True, methods=['GET'])
    def employee(self, request, pk=None):
        print("Fetching employees for company ID:", pk)
        try:
            company = self.get_object()  # Get the company instance
            ems = Employee.objects.filter(company=company)  # Fetch all employees for the company
            ems_serializer = EmployeeSerializer(ems, many=True, context={'request': request})
            return Response(ems_serializer.data)
        except Exception as e:
            print(e)
            return Response({ 'message': 'Not exist'})


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
