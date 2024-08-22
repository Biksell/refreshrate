import sys,win32api, win32con, pystray
from PIL import Image

MONITOR_INDEX = 0

def set_refresh_rate(refresh_rate):
    devmode = win32api.EnumDisplaySettings(win32api.EnumDisplayDevices(None, MONITOR_INDEX).DeviceName, win32con.ENUM_CURRENT_SETTINGS)
    devmode.DisplayFrequency = refresh_rate

    result = win32api.ChangeDisplaySettings(devmode, win32con.CDS_UPDATEREGISTRY)

    if result == win32con.DISP_CHANGE_SUCCESSFUL:
        print(f"Refresh rate changed to {refresh_rate}Hz")
    else:
        print("Refresh rate change failed")

def quit(icon, item):
    icon.stop()

def on_select(rate):
    def handler(icon, item):
        set_refresh_rate(rate)
    return handler

def create_menu(refresh_rates):
    items = []
    for rate in refresh_rates:
        items.append(pystray.MenuItem(f"{rate}Hz", on_select(rate)))
    items.append(pystray.MenuItem("Quit", quit))
    return pystray.Menu(*items)

def main():
    global MONITOR_INDEX
    try:
        MONITOR_INDEX = sys.argv[1]
        rates = sys.argv[2].split(",")
    except:
        MONITOR_INDEX = 0
        rates = [60]
    icon = pystray.Icon("RefreshRateSwitch")

    icon.menu = create_menu(rates)

    icon.icon = Image.open("brick.png")
    icon.title = "Refresh Rate Switch"
    icon.run()

if __name__ == "__main__":
    main()
