


import os

project_root = r"E:\Berar_api_gatway"

for root, dirs, files in os.walk(project_root):
    # Skip virtual environment folders
    if "venv" in root.split(os.sep):
        continue

    if "migrations" in dirs:
        migration_path = os.path.join(root, "migrations")
        for file in os.listdir(migration_path):
            file_path = os.path.join(migration_path, file)
            if file != "__init__.py" and file.endswith(".py"):
                os.remove(file_path)
                print("Deleted:", file_path)


##-----=====================================================================
## "for live"

# import os

# Oh… 😬 I see exactly what happened. Your script deleted almost all migration files, including Django’s built-in migrations in your virtual environment (venv\Lib\site-packages). That’s why you see all those paths from django\contrib\auth\migrations and other system apps.

# This is dangerous because Django’s system migrations are required for your project to run properly. If you try python manage.py migrate now, it will fail or create a completely broken database state.

# # Change this path to your project root inside the server
# project_root = "/lead/backend"

# for root, dirs, files in os.walk(project_root):
#     if "migrations" in dirs:
#         migration_path = os.path.join(root, "migrations")
#         for file in os.listdir(migration_path):
#             if file != "__init__.py" and file.endswith(".py"):
#                 os.remove(os.path.join(migration_path, file))
#                 print("Deleted:", os.path.join(migration_path, file))

#.\venv\Scripts\activate

# Reinstall Django (this will restore missing core files):
# pip install --force-reinstall django
# If you use DRF or other packages, also reinstall them:
# pip install --force-reinstall djangorestframework

# After reinstalling, try:
# python manage.py makemigrations

# (venv) E:\Berar_api_gatway>python manage.py makemigrations
# Migrations for 'auth_system':
#   auth_system\migrations\0001_initial.py
#     + Create model Department
#     + Create model Menu
#     + Create model Role
#     + Create model TblUser
#     + Create model APILog
#     + Create model LoginSession
#     + Create model RolePermission
# Migrations for 'kyc_api_gateway':
#   kyc_api_gateway\migrations\0001_initial.py
#     + Create model ClientManagement
#     + Create model PanDetails
#     + Create model VendorManagement
#     + Create model PanRequestLog
#     + Create model ApiManagement
# Migrations for 'token_blacklist':
#   venv\Lib\site-packages\rest_framework_simplejwt\token_blacklist\migrations\0001_initial.py
#     + Create model OutstandingToken
#     + Create model BlacklistedToken

# (venv) E:\Berar_api_gatway>python manage.py migrate
# Operations to perform:
#   Apply all migrations: admin, auth, auth_system, contenttypes, kyc_api_gateway, sessions, token_blacklist
# Running migrations:
#   No migrations to apply.

# shows “No migrations to apply”.
# How to check
# python manage.py showmigrations

# SELECT * FROM django_migrations;

# DELETE FROM django_migrations WHERE app='auth_system';
# DELETE FROM django_migrations WHERE app='kyc_api_gateway';

# For your project apps
# python manage.py migrate auth_system --fake
# python manage.py migrate kyc_api_gateway --fake

# # Also fake the initial migrations for built-in apps if needed
# python manage.py migrate contenttypes --fake
# python manage.py migrate sessions --fake
# python manage.py migrate admin --fake
# python manage.py migrate auth --fake

# database table se bhi sare migration delete hone chahiye varna migrations run nhi hote --fake uper wali command chaline hongi aur migration no change apply message aayega 

# 2 :next way
#_____________ another solution but not production bcoz i am sure its safe for production

#DELETE FROM django_migrations;
# DROP SCHEMA public CASCADE;
# CREATE SCHEMA public;


# python manage.py makemigrations
# python manage.py migrate


import os

project_root = r"E:\Berar_api_gatway"

for root, dirs, files in os.walk(project_root):
    # Skip virtual environment folders
    if "venv" in root.split(os.sep):
        continue

    if "migrations" in dirs:
        migration_path = os.path.join(root, "migrations")
        for file in os.listdir(migration_path):
            file_path = os.path.join(migration_path, file)
            if file != "__init__.py" and file.endswith(".py"):
                os.remove(file_path)
                print("Deleted:", file_path)


#Save and exit (CTRL+O, Enter, CTRL+X in nano).
#2. Run the script with Python
#Since your virtual environment isn’t activated yet, run it with system Python:
#python delete_migrations.py


# /lead/backend/venv/bin/python manage.py makemigrations
# /lead/backend/venv/bin/python manage.py migrate --fake-initial
