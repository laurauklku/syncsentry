import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class SyncHandler(FileSystemEventHandler):
    def __init__(self, source_dir, target_dir):
        self.source_dir = source_dir
        self.target_dir = target_dir

    def on_modified(self, event):
        self.sync_files()

    def on_created(self, event):
        self.sync_files()

    def on_deleted(self, event):
        self.sync_files()

    def on_moved(self, event):
        self.sync_files()

    def sync_files(self):
        for root, dirs, files in os.walk(self.source_dir):
            relative_path = os.path.relpath(root, self.source_dir)
            target_path = os.path.join(self.target_dir, relative_path)
            
            if not os.path.exists(target_path):
                os.makedirs(target_path)
            
            for file_name in files:
                source_file = os.path.join(root, file_name)
                target_file = os.path.join(target_path, file_name)

                if not os.path.exists(target_file) or os.path.getmtime(source_file) > os.path.getmtime(target_file):
                    shutil.copy2(source_file, target_file)
                    print(f"Copied: {source_file} to {target_file}")

        for root, dirs, files in os.walk(self.target_dir):
            relative_path = os.path.relpath(root, self.target_dir)
            source_path = os.path.join(self.source_dir, relative_path)

            for file_name in files:
                target_file = os.path.join(root, file_name)
                source_file = os.path.join(source_path, file_name)

                if not os.path.exists(source_file):
                    os.remove(target_file)
                    print(f"Removed: {target_file}")

def start_sync(source_dir, target_dir):
    event_handler = SyncHandler(source_dir, target_dir)
    observer = Observer()
    observer.schedule(event_handler, path=source_dir, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    source_directory = r"C:\path\to\source"
    target_directory = r"C:\path\to\target"
    print(f"Starting SyncSentry from {source_directory} to {target_directory}")
    start_sync(source_directory, target_directory)