

# Company and Employee API

This Django project implements a REST API for managing Company and Employee records using Django Rest Framework (DRF). The API supports CRUD operations for both `Company` and `Employee` models.

## Project Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/saadsaleem011/API-CUSTOM-API-S-EMPLOYEE-COMPANY
   cd your-repository
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the database:**
   Update your `settings.py` to configure the database settings, including the `ENGINE`, `NAME`, `USER`, `PASSWORD`, `HOST`, and `PORT`.

5. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## Models

### Company
- `company_id`: AutoField (Primary Key)
- `name`: CharField (max_length=100)
- `location`: CharField (max_length=100)
- `about_me`: TextField
- `type`: CharField (choices=['IT', 'NON-IT', 'mobile phone'])
- `added_date`: DateField (auto_now_add=True)
- `active`: BooleanField (default=True)

### Employee
- `employee_id`: AutoField (Primary Key)
- `name`: CharField (max_length=100)
- `position`: CharField (max_length=100)
- `company`: ForeignKey (to `Company`, on_delete=models.CASCADE)
- `date_joined`: DateField (auto_now_add=True)
- `active`: BooleanField (default=True)

## Serializers

### CompanySerializer
Located in `serializers.py`, the `CompanySerializer` converts the `Company` model instances to JSON and vice versa.

```python
from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
```

### EmployeeSerializer
Located in `serializers.py`, the `EmployeeSerializer` converts the `Employee` model instances to JSON and vice versa.

```python
from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
```

## Views

### CompanyViewSet
Located in `views.py`, the `CompanyViewSet` provides CRUD operations for the `Company` model using DRF's `ModelViewSet`.

```python
from rest_framework import viewsets
from .models import Company
from .serializers import CompanySerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
```

### EmployeeViewSet
Located in `views.py`, the `EmployeeViewSet` provides CRUD operations for the `Employee` model using DRF's `ModelViewSet`.

```python
from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
```

## URLs

### Router Configuration
Located in `urls.py`, the DRF router automatically generates URL patterns for the viewsets.

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, EmployeeViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
```

## Testing the API

With the development server running, you can test the API endpoints using tools like `curl`, `Postman`, or the browser:

### List all companies
```bash
GET http://127.0.0.1:8000/api/companies/
```

### Create a new company
```bash
POST http://127.0.0.1:8000/api/companies/
```
Request body:
```json
{
    "name": "New Company",
    "location": "New York",
    "about_me": "An innovative tech company.",
    "type": "IT",
    "active": true
}
```

### Retrieve a specific company
```bash
GET http://127.0.0.1:8000/api/companies/{id}/
```

### Update a company
```bash
PUT http://127.0.0.1:8000/api/companies/{id}/
```
Request body:
```json
{
    "name": "Updated Company",
    "location": "San Francisco",
    "about_me": "Updated company description.",
    "type": "NON-IT",
    "active": true
}
```

### Delete a company
```bash
DELETE http://127.0.0.1:8000/api/companies/{id}/
```

Similarly, you can test the `Employee` endpoints by replacing `companies` with `employees` in the above examples.

