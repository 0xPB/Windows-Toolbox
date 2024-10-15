# 🖥️ Windows Toolbox

This Python script allows you to easily launch various Windows system tools such as Command Prompt, Registry Editor, PowerShell, and System Information, all from a simple menu-based interface. 

## 🚀 Features
- **Command Prompt (CMD)**: Quickly open a new Command Prompt window.
- **Registry Editor (REGEDIT)**: Launch the Windows Registry Editor.
- **PowerShell**: Open a new PowerShell terminal.
- **System Information (MSINFO32)**: View detailed system information about your machine.
- **Exit Option**: Easily exit the program by selecting the exit option.

## 🛠️ Usage
1. Run the script using Python.
2. You will be prompted with a menu to choose a tool to launch.
3. Enter the corresponding number for the tool you want to open:
   - `0` for Command Prompt
   - `1` for Registry Editor
   - `2` for PowerShell
   - `3` for System Information
   - `4` to exit the script
4. After choosing an option, the selected tool will open, and the menu will clear for the next command.

## 📄 Requirements
- Python 3.x
- Works on Windows OS

## 💻 Example
```bash
> python main.py
Choix :
--------
Command Prompt (CMD): 0
Regedit (REG): 1
PowerShell (PWSHELL): 2
Msinfo32 (MSINFO32): 3
Quitter: 4
--------
Votre choix : 0
```
Selecting `0` will launch the Command Prompt.

## 📄 License
This repository is licensed under the GNU General Public License v3.0. You can read more about the terms and conditions here: [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html).
