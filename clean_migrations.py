import os

project_root = r"E:\Python_berar_app"

for root, dirs, files in os.walk(project_root):
    if "migrations" in dirs:
        migration_path = os.path.join(root, "migrations")
        for file in os.listdir(migration_path):
            if file != "__init__.py" and file.endswith(".py"):
                os.remove(os.path.join(migration_path, file))
                print("Deleted:", os.path.join(migration_path, file))


## "for live"

import os

# Change this path to your project root inside the server
project_root = "/lead/backend"

for root, dirs, files in os.walk(project_root):
    if "migrations" in dirs:
        migration_path = os.path.join(root, "migrations")
        for file in os.listdir(migration_path):
            if file != "__init__.py" and file.endswith(".py"):
                os.remove(os.path.join(migration_path, file))
                print("Deleted:", os.path.join(migration_path, file))

#Save and exit (CTRL+O, Enter, CTRL+X in nano).
#2. Run the script with Python
#Since your virtual environment isn’t activated yet, run it with system Python:
#python delete_migrations.py


# /lead/backend/venv/bin/python manage.py makemigrations
# /lead/backend/venv/bin/python manage.py migrate --fake-initial
