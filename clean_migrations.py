import os

project_root = r"E:\Python_berar_app"

for root, dirs, files in os.walk(project_root):
    if "migrations" in dirs:
        migration_path = os.path.join(root, "migrations")
        for file in os.listdir(migration_path):
            if file != "__init__.py" and file.endswith(".py"):
                os.remove(os.path.join(migration_path, file))
                print("Deleted:", os.path.join(migration_path, file))
