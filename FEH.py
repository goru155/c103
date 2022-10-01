import sys;
import time;
import random;
import os;
import shutil;
from watchdog.observers import Observer;
from watchdog.events import FileSystemEventHandler;

from_dir = "E:/Users/Admin/Downloads"

#Eventv handler class
class FileEventHandler(FileSystemEventHandler):
    
    def on_created(self,event):
        print(f"Hey,{event.src_path} has been created!")

    def on_modified(self, event):
        print(f"{event.src_path} has been modified!")

    def on_deleted(self, event):
        print(f"someone deleted {event.src_path}")

    def on_moved(self, event):
        print(f"{event.src_path} has been has been moved.")
    
#initialize evnet obsrever class
event_handler = FileEventHandler()

#initialize the obsrever class
observer = Observer()

#schedule the obsrever
observer.schedule(event_handler,from_dir,recursive = True)

#strat the obsrever
observer.start()

try :
    while True:
        time.sleep(2)
        print("running.......")
except KeyboardInterrupt:
    print('stopped!')
    observer.stop()