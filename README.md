A simple script used to recover and store passwords in an encrypted file.

Firstly, I do not claim that this script is 100% secure. My only goal with this was to create a program that I can use to store my passwords.
I will not be held accountable for passwords files being overwritten or lost keys so please use this script at your own risk.

Future plans might include packaging everything into an installer for ease of installation but for now it is important that you read the instructions listed below if you want to use this script.

Prerequisites:
  - Python 3.14 or later
  - Text editor (Notepad++, Sublime text, Visual Studio, Recommended PyCharm Community edition)
  - Windows 10 operating system (Might work on 11, not sure)

Dependencies:
  - cffi 2.1.1
  - cryptography 50.0.1
  - pip 26.0.1
  - pycparser 3.0
  - pyperclip 1.11.0

Installation steps:
  1) Download zip file of source code. Extract the folder preferably to PythonScripts folder located in your Users folder. (Just remember the location since you need to setup environment variables later)
     
  2) Open the config.py folder using your text editor and change the FILEPATH and KEYPATH variables to the location you want to store your encrypted folder and its encryption key. It is recommended that both these files are stored in the same folder and I also recommend making copies of the key. DELETING THE KEY OR THE ENCRYPTED FILE MEANS YOU WILL LOSE ACCESS TO YOUR PASSWORDS. I highly suggest setting up a path to a USB flash drive as this can act as a physical key. Python requires an escape character between file paths so the FILEPATH string should look like this "H:\\please_do_not_delete\\secure_data.json.enc". You can change the name of file as long as the extension remains the same. The KEYPATH string can look like this "H:\\please_do_not_delete\\data_key.txt"

  3) Open 
