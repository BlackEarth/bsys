
import os, subprocess, sys

def notify(message):
    """on macOS, send a notification to the system with the given message"""
    if 'darwin' in sys.platform.lower().strip():
        scriptfn = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'osx_notification.scpt')
        _=subprocess.call(['osascript', scriptfn, message])