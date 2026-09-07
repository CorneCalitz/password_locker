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

  3) Open the pw.bat file and edit the two file paths in quotation marks. The first location should be the location of your python installation. It often is "C:\Users\username\AppData\Local\Python\pythoncore-3.14-64\python.exe". The second path should be the location of our script. Mine is "C:\Users\username\PythonScripts\password_locker-main\pw.py". The slashes do not need to have an escape sequence added to them.

  4) Open up your Windows search bar and type in "Environment variables". The result should be "Edit the system environment variables". Open it and look for the button on the lower right that says "Environment Variables" and click on it. You may need to add a path variable for your python installation but it should already be set if you correctly installed python. Click on the Path variable and then on the edit button below the listbox. Click on new and paste the path of the folder belonging to our script. Click OK once you are done.

  5) Now you have two options for running the generate_key.py file.
     You can configure your text editor to run python files and execute it through a text editor or,
     you can execute it through the windows command terminal. I will explain the second approach. Open the command prompt and use the cd command to change the active file directory to your scripts location. Example: cd C:\Users\username\PythonScripts\password_locker-main. Now type the following: python generate_key.py
     This should print your key as a byte, the encrypted data set and your decrypted data set in your terminal. What this script just did is generate a encrypted data file and key file in our locations we configured in the config.py file. DO UNDER NO CIRCUMSTANCE RUN THIS SCRIPT AGAIN IF YOU HAVE PASSWORDS SAVED IN THE LOCKER. THIS WILL SCRIPT WILL OVERWRITE YOUR CURRENT KEY AND PASSWORDS IF YOU DO NOT CHANGE THE KEYPATH AND FILEPATH VARIABLE IN THE config.py FILE. I suggest deleting this script entirely or commenting out the entire file.

  6) Now you should be able to run the script from the windows run command. Press WIN + R and input pw help to see a list of keywords.
