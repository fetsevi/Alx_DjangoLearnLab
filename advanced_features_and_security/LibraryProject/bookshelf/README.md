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


# Security Measures in LibraryProject

1. **Settings Security**
   - DEBUG = False in production
   - Browser protections: SECURE_BROWSER_XSS_FILTER, X_FRAME_OPTIONS, SECURE_CONTENT_TYPE_NOSNIFF
   - Secure cookies: CSRF_COOKIE_SECURE, SESSION_COOKIE_SECURE

2. **Forms Security**
   - All forms include `{% csrf_token %}` to prevent CSRF attacks.

3. **Views Security**
   - ORM queries used to avoid SQL injection.
   - All user input validated through Django Forms.

4. **Content Security Policy (CSP)**
   - Implemented using django-csp middleware to prevent XSS.


# HTTPS & Security Configuration

- All HTTP requests are redirected to HTTPS (`SECURE_SSL_REDIRECT = True`).
- HSTS is enabled for 1 year with subdomains included and preload set.
- Session and CSRF cookies are secure-only.
- Security headers enabled:
  - `X_FRAME_OPTIONS = DENY` (clickjacking protection)
  - `SECURE_CONTENT_TYPE_NOSNIFF = True`
  - `SECURE_BROWSER_XSS_FILTER = True`
- Certificates are managed via Let's Encrypt (Certbot).
- Production server runs behind Nginx with SSL termination.

