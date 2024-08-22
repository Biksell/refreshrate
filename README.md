Switch refresh rates easily from your system tray

## Usage
(Python 3.11)
```
pip install -r requirements.txt

python main.py <MONITOR_INDEX> <RATE1,RATE2,...>
```

Or if you're using the .exe
```
RefreshRateSwitcher.exe <MONITOR_INDEX> <RATE1,RATE2,...>
```

## Example

```
python main.py 0 60,144,165
```
OR
```
RefreshRateSwitcher.exe 0 60,144,165
```

## Startup

If you want to start the program on Windows startup:
- Create a shortcut of the .bat file
- `Win+R` -> `shell:startup`
- Place the shortcut in the Startup folder
