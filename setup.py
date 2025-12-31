import sys
from cx_Freeze import setup, Executable
import os

# Find the path to the Python DLL
python_dll = os.path.join(sys.base_prefix, 'DLLs')

# Replace 'your_script.py' with the name of your script
script = 'Estedad_yabi.py'

# Dependencies are automatically detected, but it might need fine-tuning.
build_exe_options = {
    "packages": [],
    "excludes": [],  # Exclude unnecessary modules,
    "include_files": [
        (python_dll, 'DLLs'),  # Include the entire DLLs folder
        ("images", "images"),   # Include your images folder
        ("data" , "data")
    ],
        "optimize": 2,  # Optimize bytecode (0, 1, or 2)
}

# Base is set to "Win32GUI" for GUI applications.
# For console applications, it should be None.
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # If your script is a GUI application

target = Executable(
    script="Estedad_yabi.py",
    base="Win32GUI",
    icon="cli.ico"
    )

setup(
    name="Estedad_yabi",
    version="0.1",
    description="Your application description",
    options={"build_exe": build_exe_options},
    executables=[target]
)
