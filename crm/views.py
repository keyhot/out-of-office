from django.http import HttpResponse
from rest_framework import viewsets
from .models import Employee, LeaveRequest, ApprovalRequest, Project
from django.contrib.auth.models import User, Group
from .serializers import EmployeeSerializer, LeaveRequestSerializer, ApprovalRequestSerializer, ProjectSerializer

def index(request):
    return HttpResponse("Hello, world!")


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        user = User.objects.create_user(
            username=serializer.validated_data['full_name'],
            password='defaultpassword123',  # Or generate a random password
            first_name=serializer.validated_data['full_name'].split()[0],
            last_name=' '.join(serializer.validated_data['full_name'].split()[1:])
        )
        employee = serializer.save(user=user)
        
        # Assign the user to a group based on position
        if employee.position == 'HR Manager':
            hr_manager_group = Group.objects.get(name='HR Manager')
            user.groups.add(hr_manager_group)
        elif employee.position == 'Project Manager':
            project_manager_group = Group.objects.get(name='Project Manager')
            user.groups.add(project_manager_group)
        elif employee.position == 'Employee':
            employee_group = Group.objects.get(name='Employee')
            user.groups.add(employee_group)

class LeaveRequestViewSet(viewsets.ModelViewSet):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer

class ApprovalRequestViewSet(viewsets.ModelViewSet):
    queryset = ApprovalRequest.objects.all()
    serializer_class = ApprovalRequestSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
