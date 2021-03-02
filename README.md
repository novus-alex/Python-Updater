# Python-Updater
This python module allow you to update files from url to your programs.
Please install the libraries bellow before using the module.
```
pip install requests
pip install shutil
```

There's an example:
```python
from update import Update

updater = Update("your old file", "your update file url")
updater.get_new_file()
updater.update()
```
