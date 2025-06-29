import ctypes
from ctypes import c_int, c_double, c_bool, POINTER
import platform
import os

lib_dir = os.path.dirname(__file__) #path zu gravitation_interface

system = platform.system()

if system == "Windows":
    lib_path = os.path.join(lib_dir, "gravitation.dll")
elif system == "Darwin":  # macOS
    lib_path = os.path.join(lib_dir, "gravitation.dylib")
elif system == "Linux":
    lib_path = os.path.join(lib_dir, "gravitation.so")
else:
    raise RuntimeError(f"Unbekanntes Betriebssystem: {system}")

# Library laden
lib = ctypes.CDLL(lib_path)

# init_objects(int, double)
lib.init_objects.argtypes = [c_int, c_double]
lib.init_objects.restype = None

# import_objects(double, double, double, double, double, bool)
lib.import_objects.argtypes = [c_double, c_double, c_double, c_double, c_double, c_bool]
lib.import_objects.restype = None

# position_calculator(double)
lib.position_calculator.argtypes = [c_double]
lib.import_objects.restype = None

# export_objects(int, double*, double*, double*, double*)
lib.export_objects.argtypes = [c_int,
                               POINTER(c_double), POINTER(c_double),
                               POINTER(c_double), POINTER(c_double)]
lib.export_objects.restype = None
