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
#  http POST http://127.0.0.1:8000/refreshtoken/ refresh="eyJhbGciOiJIUzIMDEzLCJqdGknkc"
#  http http://127.0.0.1:8000/studentapi/ 'Authorization:Bearer eyJhbGciOiJIUz4NTkxLCJpVyOac'