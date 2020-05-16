from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time

class FileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_start):
            scr = folder_start + "/" + filename
            new_dest = folder_end + "/" + filename
            os.rename(scr, new_dest)


folder_start = "/Users/frede/Downloads"
folder_end = "/Users/frede/Random"

event_handler = FileHandler()
observer = Observer()
observer.schedule(event_handler, folder_start, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()