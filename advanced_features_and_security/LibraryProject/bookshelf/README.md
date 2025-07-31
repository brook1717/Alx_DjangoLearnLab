## Permissions and Groups Setup
### Custom Permissions:
Defined in model: can_view, can_create, can_edit, can_delete.

### Groups:
Viewers = can_view
Editors = can_view, can_create, can_edit
Admins =All permissions

### Views:
All views are protected using @permission_required decorators.
