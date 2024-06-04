import importlib.util
from subprocess import call


@staticmethod
def install_package(package):
    try:
        # Attempts to install the package using pip and confirms installation
        call(["pip", "install", package])
        print(f"{CnLanguageRoot.find("language_word/installed").text} {package}")
    except Exception as e:
        # Reports failure to install the package along with the error message
        print(f"{CnLanguageRoot.find("language_word/falled_to_install").text} {package}: {e}")

@staticmethod
# Checks for SQLite3 dependency and installs if missing
def check_sqlite3():
    if importlib.util.find_spec("sqlite3"):
        import sqlite3
        sqlite_version = sqlite3.sqlite_version
        print(f"{CnLanguageRoot.find("language_word/installed").text} SQLite: {sqlite_version}")
    else:
        install_package("sqlite3")  # Installs SQLite3 if not found

@staticmethod
# Checks for Requests library and installs if missing
def check_requests():
    if importlib.util.find_spec("requests"):
        import requests
        requests_version = requests.__version__
        print(f"{CnLanguageRoot.find("language_word/installed").text}: {requests_version}")
    else:
        install_package("requests")  # Installs Requests if not found
@staticmethod
def check_xml():
    if importlib.util.find_spec("lxml"):
        print("有XML")
    else:
        print("未找到XML库，正在安装...")
        install_package("lxml")