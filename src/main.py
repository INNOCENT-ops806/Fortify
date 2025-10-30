import argparse
import os
from password_generator import generate
# import sys


def get_unique_filename(filename):
    """Return a unique filename by incrementing if needed."""
    filename = os.path.expanduser(filename)
    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    base, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(new_filename):
        new_filename = f"{base}{counter}{ext}"
        counter += 1
    return new_filename


def run_cli(args):
    length = args.length
    filename = args.filename or "output.txt"
    filename = get_unique_filename(filename)
    password = generate(length=length)
    with open(filename, "w") as f:
        f.write(password)
    print(f"Password saved to {filename}")


def run_gui():
    import fortifyGUI  # This will launch the GUI

    fortifyGUI.launch_gui()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fortify Password Generator")
    parser.add_argument("--gui", action="store_true", help="Run the GUI version")
    parser.add_argument(
        "--length", type=int, default=8, help="Password length (CLI only)"
    )
    parser.add_argument(
        "--filename", type=str, help="Output filename (CLI only, default: output.txt)"
    )
    args = parser.parse_args()

    if args.gui:
        run_gui()
    else:
        run_cli(args)
