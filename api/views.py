from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


#  http POST http://127.0.0.1:8000/gettoken/ username='admin' password='Admin@1994'
#  http POST http://127.0.0.1:8000/refreshtoken/ refresh="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMzYyNDQxMywiaWF0IjoxNzIzNTM4MDEzLCJqdGkiOiIxMTA4M2M5ZmFjNDU0NWNkYmQ4MGFlZDg3NTU4NzBkOCIsInVzZXJfaWQiOjF9.HrEtCvK66mj4fJbstoM4CwVGzB-pe2OD6sScYQTLnkc"
#  http http://127.0.0.1:8000/studentapi/ 'Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIzNTM4NTkxLCJpYXQiOjE3MjM1MzgwMTMsImp0aSI6IjA5MDY2ODRhM2U4NTQ0ZTY5ZmM4ZjlhZGUyNWE5YmQwIiwidXNlcl9pZCI6MX0.wdA4fvC6nwALnEypcX7g55FeO-E0MBQ44oD0iCVyOac'