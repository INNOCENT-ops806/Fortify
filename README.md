# Fortify

![FORTIFY_ASCII](./assets/fortify_art.png)

## Description

Fortify is a command-line and GUI password generator to help you create strong, secure passwords for safe cyberspace practices. It is written in Python and leverages several easy-to-use modules.
I was forced to (kind of by situation) create this project because I have been focused on playing CTFs lately and I have been struggling a lot to come up with different passwords for different CTFs. This will make it easier for me(and anybody who will use this) to save passwords in the directory of their choice on a file.

![CTF_SCREENSHOT](./assets/CTF_Screenshot.png)

## Features

- Generate strong passwords with customizable length
- Choose between command-line and GUI modes
- Automatically saves passwords to a file (with auto-incremented filenames)
- Copies generated passwords to your clipboard
- Support for custom password vault directories

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/Yahm3/Fortify.git
   cd Fortify
   ```

2. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Binary Executable (No Python Required)

For users who do not have Python installed or prefer a standalone application, a single-file executable is provided.

1. **Download:** Download the latest compiled binary executable for your operating system (e.g., `Fortify.exe` for Windows, `Fortify` for Linux/macOS) from the [GitHub Releases Page](<https://github.com/Yahm3/Fortify/releases/tag/v1.0.0>).
2. **Run:** Place the downloaded file in a directory of your choice.
3. **Usage:** Run the executable directly from your terminal or command prompt:
   - **Linux/macOS:**

     ```sh
     ./Fortify --gui
     # or
     ./Fortify --length 12
     ```

   - **Windows (PowerShell/CMD):**

     ```sh
     .\Fortify.exe --gui
     # or
     .\Fortify.exe --length 12
     ```
### Command-Line (default)

```sh
python src/main.py --length 12 --filename mypass.txt

```

- `--length` : Password length (default: 8)
- `--filename` : Output filename (default: output.txt, auto-increments if exists)

#### Custom Directory Paths
You can specify custom directories for password storage:

```sh
# Save to home directory
python src/main.py --filename ~/passwords/mypass.txt

# Save to absolute path
python src/main.py --filename /home/user/secure/vault/pass.txt

# Save with auto-increment (creates pass1.txt if pass.txt exists)
python src/main.py --filename ~/passwords/pass.txt
````

The program will:

- Create directories automatically if they don't exist
- Expand `~` to your home directory
- Auto-increment filenames to prevent overwrites

### GUI

```sh
python src/main.py --gui
```

## Images

#### Using the GUI

![GUI_USAGE_EXAMPLE](./assets/GUI_USAGE_EXAMPLE.png)

### Using the CLI(recommended)

![CLI_USAGE_EXAMPLE](./assets/CLI_USAGE_EXAMPLE.png)

## License

MIT License
The project is Licensed under MIT License feel free to edit in any way that you want
