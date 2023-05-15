import os 
import sys
import time
import keyboard
import pyautogui
import ctypes

from termcolor import colored

from Handlers.settingsHandler import GetSettings
from Handlers.programHandler import Program

settings = GetSettings()

resolusiMonitor = pyautogui.size()
CENTER_X, CENTER_Y = resolusiMonitor.width // 2, resolusiMonitor.height // 2


def main():
    os.system('cls')
    os.system('color')
    os.system(f"title {settings.GetSetupAppName()}")

    bettercmd()

    status = 'Disabled'
    
    mainProgram = Program(CENTER_X, CENTER_Y)

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
        print(colored('●', 'yellow'), colored('AimBot\t\t=\t', 'white'), colored('ENABLED', 'green'))
    else:
        print(colored('●', 'yellow'), colored('AimBot\t\t=\t', 'white'), colored('DISABLED', 'red'))
    # TriggerBot Status 
    if settings.GetTriggerbotEnabled():
        print(colored('●', 'yellow'), colored('TriggerBot\t\t=\t', 'white'), colored('ENABLED', 'green'))
    else:
        print(colored('●', 'yellow'), colored('TriggerBot\t\t=\t', 'white'), colored('DISABLED', 'red'))
    # SilentBot Status
    if settings.GetSilentbotEnabled():
        print(colored('●', 'yellow'), colored('SilentBot\t\t=\t', 'white'), colored('ENABLED', 'green'))
    else:
        print(colored('●', 'yellow'), colored('SilentBot\t\t=\t', 'white'), colored('DISABLED', 'red'))

    print()

    print(colored('[KEY BIND INFORMATION]', 'green'))
    print(colored('●', 'yellow'), colored(f"Toggle ON/OFF\t\t=\t Press {settings.GetSettingsToggleKey()}", 'white'))
    print(colored('●', 'yellow'), colored(f"AimBot\t\t=\t Hold {settings.GetAimbotKeyBindConvert()}", 'white'))
    print(colored('●', 'yellow'), colored(f"TriggerBot\t\t=\t Hold {settings.GetTriggerbotKeyBindConvert()}", 'white'))
    print(colored('●', 'yellow'), colored(f"SilentBot\t\t=\t Press {settings.GetSilentbotKeyBindConvert()}", 'white'))

    print()

    try:
        while True:
            if keyboard.is_pressed(settings.GetSettingsToggleKey()):
                mainProgram.toggle()
                status = 'Enabled' if mainProgram.TOGGLED else 'Disabled'
            print(f"{colored('[STATUS]', 'green')}{colored(status, 'white')}", end='')
            time.sleep(1.01)

    except (KeyboardInterrupt, SystemExit):
        print(colored('[INFO]', 'green'), colored('Exiting...', 'white') + '\n')
        sys.exit()

def bettercmd():
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd:
        style = ctypes.windll.user32.GetWindowLongW(hwnd, -16)
        style &= -262145
        style &= -65537
        ctypes.windll.user32.SetWindowLongW(hwnd, -16, style)

if __name__ == '__main__':
    main()