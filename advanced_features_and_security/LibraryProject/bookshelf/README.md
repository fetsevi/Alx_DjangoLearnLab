# Groups and Permissions Setup

We use Django Groups + Permissions to control access:

## Custom Permissions
Defined in `Book` model:
- `can_view`
- `can_create`
- `can_edit`
- `can_delete`

## Groups
- **Editors**: `can_edit`, `can_create`
- **Viewers**: `can_view`
- **Admins**: All permissions

## Usage
- Run `python manage.py create_groups` to create groups and assign permissions.
- Assign users to groups in `/admin/`.
- Views are protected using `@permission_required`.
