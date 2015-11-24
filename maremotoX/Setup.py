import sys
from cx_Freeze import setup, Executable

build_exe_options = {
	"packages": ["os","pygame","cx_Freeze", "Pil", "pip"],
	"include_files": ["recursos"]
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  
	name = "Maremoto",
    version = "0.1",
    description = "Maremoto",
    options = {"build_exe": build_exe_options},
    executables = [Executable("principal/App.py", base=base)]
)