from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
import logging

@receiver(post_migrate)
def create_roles(sender, **kwargs):
    if sender.name != 'crm':
        return

    hr_manager_group, created = Group.objects.get_or_create(name='HR Manager')
    project_manager_group, created = Group.objects.get_or_create(name='Project Manager')
    employee_group, created = Group.objects.get_or_create(name='Employee')

    models = ['Employee', 'LeaveRequest', 'ApprovalRequest', 'Project']
    for model_name in models:
        try:
            model = sender.get_model(model_name)
            content_type = ContentType.objects.get_for_model(model)
            permissions = Permission.objects.filter(content_type=content_type)
            hr_manager_group.permissions.add(*permissions)
        except Exception as e:
            logging.error(f"Error creating roles for {model_name}: {e}")

    logging.info("Roles created successfully.")
