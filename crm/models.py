from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee_profile')
    full_name = models.CharField(max_length=100)
    subdivision = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])
    people_partner = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    out_of_office_balance = models.IntegerField()
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)

    def __str__(self):
        return self.full_name

class LeaveRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    absence_reason = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    comment = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        default="New",
        choices=[("New", "New"), ("Approved", "Approved"), ("Rejected", "Rejected")],
    )

    def __str__(self):
        return f"{self.employee.full_name} - {self.absence_reason}"


class ApprovalRequest(models.Model):
    approver = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="approvals"
    )
    leave_request = models.ForeignKey(LeaveRequest, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        default="New",
        choices=[("New", "New"), ("Approved", "Approved"), ("Rejected", "Rejected")],
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Approval for {self.leave_request.employee.full_name}"


class Project(models.Model):
    project_type = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    project_manager = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="managed_projects"
    )
    comment = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=20, choices=[("Active", "Active"), ("Inactive", "Inactive")]
    )

    def __str__(self):
        return self.project_type
