from rest_framework import viewsets
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Job, User, Application
from .serializers import ApplicationSerializer, JobSerializer, UserSerializer


@api_view(["GET"])
def api_home(request):
    return Response(
        {
            "message": "Job Portal API is running",
            "endpoints": {
                "jobs": "/api/jobs/",
                "users": "/api/users/",
                "applications": "/api/applications/",
            },
        }
    )


def favicon(request):
    return HttpResponse(status=204)

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer    