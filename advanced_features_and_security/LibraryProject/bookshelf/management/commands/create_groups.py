# bookshelf/management/commands/create_groups.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

class Command(BaseCommand):
    help = "Create user groups and assign permissions"

    def handle(self, *args, **kwargs):
        content_type = ContentType.objects.get_for_model(Book)

        # Groups and their permissions
        groups = {
            "Editors": ["can_edit", "can_create"],
            "Viewers": ["can_view"],
            "Admins": ["can_edit", "can_create", "can_delete", "can_view"],
        }

        for group_name, perms in groups.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for codename in perms:
                permission = Permission.objects.get(
                    codename=codename, content_type=content_type
                )
                group.permissions.add(permission)

        self.stdout.write(self.style.SUCCESS("Groups and permissions created!"))

