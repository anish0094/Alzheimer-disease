import cx_Freeze
import sys
import os

# **1. Specify Application Information**
name = "AD Prediction"  
version = "1.0"


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

# **2. Define Executables**
executables = [cx_Freeze.Executable("app.py", icon="logo.ico")] 

# **3. Include Model File 
include_files = [
    (resource_path("Random_forest.pkl"), "Random_forest.pkl"),
    (resource_path("sklearn"), "sklearn")  # Include the sklearn package
]



# **5. Setup Call**
cx_Freeze.setup(
    name=name,
    version=version,
    description="Alzheimer's Disease Prediction Application",
    executables=executables, 
    include_files = include_files
)
