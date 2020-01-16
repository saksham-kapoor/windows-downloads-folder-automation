import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

path = "C:\\Users\\Saksham Kapoor\\Downloads"


def on_modified(event):
    full_path = event.dest_path
    file_name = full_path.replace(path + '\\', '')
    name, ext = os.path.splitext(file_name)
    if '\\' in name:
        return
    ext = ext[1:]
    if ext == 'tmp' or 'crdownload' in ext:
        return
    if os.path.exists(path+'\\'+ext):
        shutil.move(path + '\\' + file_name, path +
                    '\\' + ext + '\\' + file_name)
    elif not os.path.exists(path+'\\'+ext):
        os.mkdir(path + '\\' + ext)
        os.replace(path+'/'+file_name, path + '/' + ext + '/' + file_name)


if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = True
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(
        patterns, ignore_patterns, ignore_directories, case_sensitive)

    my_event_handler.on_moved = on_modified

    go_recursively = False
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)

    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
    my_observer.join()
