import argparse
from core import DepSetup

def main():
    parser = argparse.ArgumentParser(description='Dependency Checker and Game Config Utility.')
    parser.add_argument('--init', action='store_true', help='Checks and installs required dependencies.')
    parser.add_argument('--ConfigGameDir', action='store_true', help='Intended for setting up game directory configuration.')
    args = parser.parse_args()

    if args.init:
        DepSetup.check_sqlite3()
        DepSetup.check_requests()
        DepSetup.check_xml()
    else:
        print("What operation do you want to perform?")
        parser.print_help()

if __name__ == "__main__":
    main()