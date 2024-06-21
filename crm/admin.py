from django.contrib import admin
from .models import Employee, LeaveRequest, ApprovalRequest, Project
from django.contrib.auth.models import User, Group

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'subdivision', 'position', 'status')
    list_filter = ('subdivision', 'position', 'status')
    search_fields = ('full_name',)
    ordering = ('full_name',)
    actions = ['deactivate_employees']

    def deactivate_employees(self, request, queryset):
        queryset.update(status='Inactive')
    deactivate_employees.short_description = "Deactivate selected employees"

class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'absence_reason', 'start_date', 'end_date', 'status')
    list_filter = ('absence_reason', 'status')
    search_fields = ('id', 'employee__full_name')
    ordering = ('id',)
    actions = ['approve_requests', 'reject_requests']

    def approve_requests(self, request, queryset):
        queryset.update(status='Approved')
    approve_requests.short_description = "Approve selected leave requests"

    def reject_requests(self, request, queryset):
        queryset.update(status='Rejected')
    reject_requests.short_description = "Reject selected leave requests"

class ApprovalRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'approver', 'leave_request', 'status')
    list_filter = ('status',)
    search_fields = ('id',)
    ordering = ('id',)
    actions = ['approve_requests', 'reject_requests']

    def approve_requests(self, request, queryset):
        for approval in queryset:
            approval.status = 'Approved'
            approval.leave_request.status = 'Approved'
            approval.leave_request.save()
            approval.save()
    approve_requests.short_description = "Approve selected approval requests"

    def reject_requests(self, request, queryset):
        for approval in queryset:
            approval.status = 'Rejected'
            approval.leave_request.status = 'Rejected'
            approval.leave_request.save()
            approval.save()
    reject_requests.short_description = "Reject selected approval requests"

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_type', 'start_date', 'end_date', 'status')
    list_filter = ('project_type', 'status')
    search_fields = ('id',)
    ordering = ('id',)
    actions = ['deactivate_projects']

    def deactivate_projects(self, request, queryset):
        queryset.update(status='Inactive')
    deactivate_projects.short_description = "Deactivate selected projects"

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(LeaveRequest, LeaveRequestAdmin)
admin.site.register(ApprovalRequest, ApprovalRequestAdmin)
admin.site.register(Project, ProjectAdmin)
