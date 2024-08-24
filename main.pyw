import win32api, win32con, pystray
from PIL import Image

MONITOR_INDEX = None

def set_refresh_rate(refresh_rate, monitor):
    global MONITOR_INDEX
    devmode = win32api.EnumDisplaySettings(monitor, win32con.ENUM_CURRENT_SETTINGS)
    devmode.DisplayFrequency = refresh_rate

    result = win32api.ChangeDisplaySettingsEx(monitor, devmode, win32con.CDS_UPDATEREGISTRY)

    if result == win32con.DISP_CHANGE_SUCCESSFUL:
        print(f"Refresh rate changed to {refresh_rate}Hz")
    else:
        print(f"Refresh rate change failed\n{result}")


def get_all_monitors():
    monitors = []
    i = 0
    while True:
        try:
            device = win32api.EnumDisplayDevices(None, i)
            if device.DeviceName:
                monitors.append(device.DeviceName)
            i += 1
        except:
            break
    return monitors


def get_device_name(index):
    device = win32api.EnumDisplayDevices(None, index)
    if device and device.DeviceName:
        return device.DeviceName
    return None


def get_refresh_rates(monitor_index):
    device_name = get_device_name(monitor_index)
    if device_name is None:
        print(f"Monitor with index {monitor_index} not found.")
        return []

    i = 0
    refresh_rates = set()
    while True:
        try:
            devmode = win32api.EnumDisplaySettings(device_name, i)
            refresh_rates.add(devmode.DisplayFrequency)
            i += 1
        except Exception:
            break

    return sorted(refresh_rates)


def on_select(rate, monitor):
    def handler(icon, item):
        set_refresh_rate(rate, monitor)
    return handler


def create_menu(monitors):
    menus = []
    for index, monitor in enumerate(monitors):
        options = []
        for refresh_rate in get_refresh_rates(index):
            options.append(pystray.MenuItem(f"{refresh_rate}Hz", on_select(refresh_rate, monitor)))
        monitor_menu = pystray.Menu(*options)
        menus.append(pystray.MenuItem(f"{index}: {monitor}", monitor_menu))
    menus.append(pystray.MenuItem("Quit", quit))
    return pystray.Menu(*menus)



def quit(icon, item):
    icon.stop()


def main():
    monitors = get_all_monitors()
    icon = pystray.Icon("RefreshRateSwitch")

    icon.menu = create_menu(monitors)

    icon.icon = Image.open("brick.png")
    icon.title = "Refresh Rate Switch"
    icon.run()

if __name__ == "__main__":
    main()
