import py2exe

py2exe.freeze(
    windows=[{"script": "main.pyw", "dest_base": "RefreshRateSwitcher"}],
    options={"bundle_files": 1}
)
