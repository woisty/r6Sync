

# R6 Sync

A very simply script that syncs ``GameSettings.ini`` files with all folders in a directory. 
## Requirements
Python 3 (& [PyInstaller](https://pyinstaller.org/en/stable/) for your own 'compiling'.)

## Installation
Place the ``.exe`` in your setting's folder and have your desired ``GameSettings.ini`` file outside of all the folders. **It'll only work if there is an already existing GameSettings.ini in the folder.**

Setup / File Structure example:
!['account 1' and 'account 2' will be your UID instead, they're just examples.](https://cdn.discordapp.com/attachments/1278054402296512625/1284624239277772810/image.png?ex=66e74f0d&is=66e5fd8d&hm=b3f247b9231203bf69d5a02a22c3eae37af3bfcab48fbeacf26b176d48fe7272&)

To turn it into a ``.exe`` from source, do the following:

 1. `pip install pyinstaller` - *installs* [PyInstaller](https://pyinstaller.org/en/stable/)
 2. `pyinstaller --onefile --sync.py`

## Usage
Double click it. A console will open and close. Check 1-2 folders to see if they're synced. You only need to look at the `Date Modified`

## Contributing / Pulling
No need to contribute, nor do I care about anyone modifying/copying this.

## Project Status
Finished - it does what I want.

## Credits
ChatGPT - for a base, it was about 12 lines total.

# NOTES
If you want to use this quick script and change it to sync other files, simply change the 7th line: 
*replace 'GameSettings.ini' to you're desired file*
`    settings_file = os.path.join(base_dir, "GameSettings.ini")`
(This won't change the echo's/prints)
