import importlib.util
from subprocess import call

@staticmethod
def install_package(package):
    try:
        # Attempts to install the package using pip and confirms installation
        call(["pip", "install", package])
        print(f"Installed: {package}")
    except Exception as e:
        # Reports failure to install the package along with the error message
        print(f"Failure to install{package}: {e}")

@staticmethod
# Checks for SQLite3 dependency and installs if missing
def check_sqlite3():
    if importlib.util.find_spec("sqlite3"):
        import sqlite3
        sqlite_version = sqlite3.sqlite_version
        print(f"SQLite3 Installed: {sqlite_version}")
    else:
        install_package("sqlite3")  # Installs SQLite3 if not found

@staticmethod
# Checks for Requests library and installs if missing
def check_requests():
    if importlib.util.find_spec("requests"):
        import requests
        requests_version = requests.__version__
        print(f"Requests Installed: {requests_version}")
    else:
        install_package("requests")  # Installs Requests if not found
@staticmethod
def check_xml():
    if importlib.util.find_spec("lxml"):
        import lxml
        lxml_version = lxml.__version__
        print(f"Lxml Installed: {lxml_version}")
    else:
        install_package("lxml")