import os 
import sys
import time
import keyboard     # pip install keyboard
import pyautogui    # pip install pyautogui
import ctypes
import hashlib

from termcolor import colored  # pip install termcolor

from Handlers.settingsHandler import GetSettings
from Handlers.programHandler import *

settings = GetSettings()

resolusiMonitor = pyautogui.size()
CENTER_X, CENTER_Y = resolusiMonitor.width // 2, resolusiMonitor.height // 2


def main():
    os.system('color')
    os.system(f"title {settings.GetSetupAppName()}")
    
    # bettercmd()
    
    print(colored('         ██▀███ ▓████▓██   ██▓    ▄████▄  ▒█████ ▓█████▄▓█████  ██████ ', 'magenta'))
    print(colored('        ▓██ ▒ ██▓█   ▀▒██  ██▒   ▒██▀ ▀█ ▒██▒  ██▒██▀ ██▓█   ▀▒██    ▒ ', 'magenta'))
    print(colored('        ▓██ ░▄█ ▒███   ▒██ ██░   ▒▓█    ▄▒██░  ██░██   █▒███  ░ ▓██▄   ', 'magenta'))
    print(colored('        ▒██▀▀█▄ ▒▓█  ▄ ░ ▐██▓░   ▒▓▓▄ ▄██▒██   ██░▓█▄   ▒▓█  ▄  ▒   ██▒', 'magenta'))
    print(colored('        ░██▓ ▒██░▒████▒░ ██▒▓░   ▒ ▓███▀ ░ ████▓▒░▒████▓░▒████▒██████▒▒', 'magenta'))
    print(colored('        ░ ▒▓ ░▒▓░░ ▒░ ░ ██▒▒▒    ░ ░▒ ▒  ░ ▒░▒░▒░ ▒▒▓  ▒░░ ▒░ ▒ ▒▓▒ ▒ ░', 'magenta'))
    print(colored('          ░▒ ░ ▒░░ ░  ▓██ ░▒░      ░  ▒    ░ ▒ ▒░ ░ ▒  ▒ ░ ░  ░ ░▒  ░ ░', 'magenta'))
    print(colored('          ░░   ░   ░  ▒ ▒ ░░     ░       ░ ░ ░ ▒  ░ ░  ░   ░  ░  ░  ░  ', 'magenta'))
    print(colored('           ░       ░  ░ ░        ░ ░         ░ ░    ░      ░  ░     ░  ', 'magenta'))
    print(colored('                      ░ ░        ░                ░                    ', 'magenta'))
    
    print()
    
    print(colored('[INFO]', 'green'), colored('Successfully loaded all functions', 'white'))
    print(colored('[INFO]', 'green'), colored(f"Detected screen size = {resolusiMonitor.width} x {resolusiMonitor.height}", 'white'))
    
    print()
    
    print(colored('[PROGRAM STATUS]', 'green'))
    # AimBot Status
    if settings.GetAimbotEnabled():
        print(colored('●', 'yellow'), colored('AimBot \t=\t', 'white'), colored('ENABLED', 'green'))
    else:
        print(colored('●', 'yellow'), colored('AimBot \t=\t', 'white'), colored('DISABLED', 'red'),)
    # TriggerBot Status 
    if settings.GetTriggerbotEnabled():
        print(colored('●', 'yellow'), colored('TriggerBot \t=\t', 'white'), colored('ENABLED', 'green'))
    else:
        print(colored('●', 'yellow'), colored('TriggerBot \t=\t', 'white', colored('DISABLED', 'red'),))
    # SilentBot Status
    if settings.GetSilentbotEnabled():
        print(colored('●', 'yellow'), colored('SilentBot \t=\t', 'white'), colored('ENABLED', 'green'))
    else:
        print(colored('●', 'yellow'), colored('SilentBot \t=\t', 'white'), colored('DISABLED', 'red'),)

    print()
    
    print(colored('[KEY BIND INFORMATION]', 'green'))
    print(colored('●', 'yellow'), colored(f"Press\t {settings.GetSettingsToggleKey()} \t=\t Toggle ON/OFF", 'white'))
    print(colored('●', 'yellow'), colored(f"Hold\t {settings.GetAimbotKeyBind()} \t=\t AimBot", 'white'))
    print(colored('●', 'yellow'), colored(f"Press\t {settings.GetTriggerbotKeyBind()} \t=\t TriggerBot", 'white'))
    print(colored('●', 'yellow'), colored(f"Hold\t {settings.GetSilentbotKeyBind()} \t=\t SilentBot", 'white'))
    
def bettercmd():
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd:
        style = ctypes.windll.user32.GetWindowLongW(hwnd, -16)
        style &= -262145
        style &= -65537
        ctypes.windll.user32.SetWindowLongW(hwnd, -16, style)

if __name__ == '__main__':
    main()