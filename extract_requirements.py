import pkg_resources
import os

# Adjust this path to your broken venv's site-packages folder
site_packages_path = r"C:\Users\Jer\Bootcamp_project\venv\Lib\site-packages"

# Set up working environment to use that folder
working_env = pkg_resources.Environment([site_packages_path])

with open("recovered_requirements.txt", "w") as f:
    for dist in working_env:
        try:
            f.write(f"{dist.project_name}=={dist.version}\n")
        except Exception as e:
            print(f"Error writing {dist}: {e}")