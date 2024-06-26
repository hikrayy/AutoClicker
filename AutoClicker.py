from pynput.mouse import Button, Controller as MouseController
import keyboard
import ctypes
import time
from threading import Thread
from colorama import init, Fore, Style

init(autoreset=True)

kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleTitleW("Autoclicker | By hirangesh")

print(Fore.RED + " ▄▀▀█▄▄   ▄▀▀▄ ▀▀▄      ▄▀▀▄ ▄▄   ▄▀▀█▀▄    ▄▀▀▄▀▀▀▄  ▄▀▀█▄   ▄▀▀▄ ▀▄  ▄▀▀▀▀▄   ▄▀▀█▄▄▄▄  ▄▀▀▀▀▄  ▄▀▀▄ ▄▄" + Style.RESET_ALL)
print(Fore.RED + "▐ ▄▀   █ █   ▀▄ ▄▀     █  █   ▄▀ █   █  █  █   █   █ ▐ ▄▀ ▀▄ █  █ █ █ █        ▐  ▄▀   ▐ █ █   ▐ █  █   ▄▀" + Style.RESET_ALL)
print(Fore.RED + "  █▄▄▄▀  ▐     █       ▐  █▄▄▄█  ▐   █  ▐  ▐  █▀▀█▀    █▄▄▄█ ▐  █  ▀█ █    ▀▄▄   █▄▄▄▄▄     ▀▄   ▐  █▄▄▄█" + Style.RESET_ALL)
print(Fore.RED + "  █   █        █          █   █      █      ▄▀    █   ▄▀   █   █   █  █     █ █  █    ▌  ▀▄   █     █   █" + Style.RESET_ALL)
print(Fore.RED + " ▄▀▄▄▄▀      ▄▀          ▄▀  ▄▀   ▄▀▀▀▀▀▄  █     █   █   ▄▀  ▄▀   █   ▐▀▄▄▄▄▀ ▐ ▄▀▄▄▄▄    █▀▀▀     ▄▀  ▄▀" + Style.RESET_ALL)
print(Fore.RED + "█    ▐       █          █   █    █       █ ▐     ▐   ▐   ▐   █    ▐   ▐         █    ▐    ▐       █   █" + Style.RESET_ALL)
print(Fore.RED + "▐            ▐          ▐   ▐    ▐       ▐                   ▐                  ▐                 ▐   ▐" + Style.RESET_ALL)

print("")
print("")
print(Fore.GREEN + "      F6 to start" + " " * 10 + Fore.RED + "F7 to stop" + " " * 10 + Fore.YELLOW + "F8 to increase speed" + " " * 10 + Fore.CYAN + "F9 to decrease speed")

mouse = MouseController()
is_running = False
click_delay = 0.01

def toggle_clicker():
    global is_running
    is_running = not is_running
    if is_running:
        print(Fore.GREEN + "Autoclicker Launched." + Style.RESET_ALL)
        thread = Thread(target=auto_clicker)
        thread.start()
    else:
        print(Fore.RED + "Autoclicker Stopped." + Style.RESET_ALL)

def auto_clicker():
    while is_running:
        mouse.click(Button.left)
        time.sleep(click_delay)

def stop_clicker():
    global is_running
    is_running = False
    print(Fore.RED + "Autoclicker Stopped." + Style.RESET_ALL)

def increase_speed():
    global click_delay
    if click_delay > 0.001:
        click_delay -= 0.001
    print(Fore.YELLOW + f"Speed increased, delay: {click_delay:.3f} seconds")

def decrease_speed():
    global click_delay
    click_delay += 0.001
    print(Fore.CYAN + f"Speed decreased, delay: {click_delay:.3f} seconds")

def on_key_press(event):
    global is_running
    if event.name == 'f6':
        if not is_running:
            toggle_clicker()
    elif event.name == 'f7':
        if is_running:
            stop_clicker()
    elif event.name == 'f8':
        increase_speed()
    elif event.name == 'f9':
        decrease_speed()

keyboard.on_press(on_key_press)
keyboard.wait('')
keyboard.unhook_all()
