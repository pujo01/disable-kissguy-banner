import ctypes, utility
from ctypes import wintypes
from consts import *
import os

kernel32 = ctypes.windll.kernel32

pid = utility.GetProcId("GenshinImpact.exe")
handle = kernel32.OpenProcess(PROCESS_ALL_ACCESS, 0, ctypes.wintypes.DWORD(pid))
base_address = utility.GetModuleBaseAddress(pid, "mhyprot.dll")
objectPointer = base_address + 0x377064
objectPointersecond = base_address + 0x377064 - 0x14
menuPointer = base_address + 0x265D98


while True:
    utility.nopBytes(handle, menuPointer, 2)
    utility.nopBytes(handle, objectPointer, 2)
    utility.nopBytes(handle, objectPointersecond, 2)
    print("Done!")
# Close handle
    kernel32.CloseHandle(handle)
    print("[ INFO ] Handle closed!")
    os.system("pause")
    break
# If you want to lock your values, comment line 76
