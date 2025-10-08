# Dictapp.py

import os

apps = {
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "vs code": "C:\\Users\\ABHISHEK KARMAKAR\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
    "paint": "mspaint.exe",
    "word": "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
    "excel": "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
}

def openappweb(query):
    for app in apps:
        if app in query:
            os.startfile(apps[app])
            return
    print("App not found.")

def closeappweb(query):
    for app in apps:
        if app in query:
            os.system(f"taskkill /f /im {os.path.basename(apps[app])}")
            return
    print("App not found.")
