"""An insecure password locker program"""


#! python3
import sys
import pyperclip
import json
from cryptography.fernet import Fernet
from passwordGenerator import Password
from config import FILEPATH, KEYPATH


KEYWORDS = {
    "help": 'Lists all available commands.',
    "list": 'Shows all user accounts.',
    'crt <account_name>' : 'Prompts user to generate if they want generate a custom password for their account',
    'gen': 'Prompts user to generate a custom password with specific length or characters without an account attached.',
    'get <account_name>':'Retrieves the password associated with the account name.',
    'del <account_name>': 'Deletes the password associated with the account name.'
            }

PASS_LEN = 24
HELP_TEXT = 'Usage: python pw.py <help> for list of commands in terminal / pw <help> in window run dialog box'

def get_key():
    """Retrieve key"""
    try:
        with open(KEYPATH, 'r') as k:
            key = k.read()
        return Fernet(key)
    except FileNotFoundError:
        print("Please insert passkey")
        sys.exit()


def decrypt_data(encrypted_data):
    """Decrypt the data"""
    decrypted_bytes = get_key().decrypt(encrypted_data)
    decrypted_data = json.loads(decrypted_bytes.decode('utf-8'))
    return decrypted_data


def encrypt_data(data):
    """Encrypt the data"""
    json_bytes = json.dumps(data).encode('utf-8')
    encrypted_data = get_key().encrypt(json_bytes)
    return encrypted_data


def read():
    """Reads data from file"""
    try:
        with open(FILEPATH, 'rb') as f:
            encrypted_data = f.read()
        return encrypted_data
    except FileNotFoundError:
        print("Please insert passkey")
        sys.exit()


def _list():
    """List all the available accounts"""
    source = read()
    data = decrypt_data(source)
    if len(data) == 0:
        print('No accounts within locker, use crt command to create a new account')
    else:
        for keys in data.keys():
            print(keys)


def _help():
    """Display list of commands and usage"""
    spacer = max([len(k) for k in KEYWORDS.keys()])
    print("\tCOMMAND KEYWORDS:")
    for key, value in KEYWORDS.items():
        space = (spacer-len(key))*' '
        print(f'\t{key}{space} - {value}')


def pass_create_prompt():
    """Handles the prompt logic when creating a password"""
    print("Entering nothing will default to a 'yes' response")
    # TODO ERROR HANDLING FUNCTION FOR THE STRING INPUT
    lower_flag = input("Should your password contain lowercase? (y/n): ").lower().strip() not in ('no', 'n')
    upper_flag = input("Should your password contain uppercase? (y/n): ").lower().strip() not in ('no', 'n')
    special_flag = input("Should your password contain special characters? (y/n): ").lower().strip() not in ('no', 'n')
    number_flag = input("Should your password contain numbers? (y/n): ").lower().strip() not in ('no', 'n')

    while True:
        pass_len = input("How long should your password be? (8 - 128): ")
        try:
            # Checks that input is integer
            valid_len = int(pass_len)

            # Checks that input is within range
            if 8 <= valid_len <= 128:
                break
            else:
                print('Number is not within valid range (8 - 128)')
        except ValueError:
            print('Input needs to be an integer')

    return lower_flag, upper_flag, special_flag, number_flag, valid_len


def gen():
    """Generate a password based on user requirements without an account name"""
    lower_flag, upper_flag, special_flag, number_flag, valid_len = pass_create_prompt()
    obj = Password(lower_flag, upper_flag, special_flag, number_flag, valid_len)
    pyperclip.copy(obj.get())
    print('Password copied to clipboard.')
    sys.exit()


def write_account(data, name, password):
    """Write account name and password into file"""
    data[name] = password
    source = encrypt_data(data)
    try:
        with open(FILEPATH, 'wb') as file:
            file.write(source)
    except FileNotFoundError:
        print('Please insert passkey')

    print('User account created')
    pyperclip.copy(data[name])
    print('Password for ' + name + ' copied to clipboard.')
    sys.exit()


def create_account():
    """Creates and saves a user account with default password"""

    account_name = sys.argv[2]
    source = read()
    data = decrypt_data(source)

    if account_name in data.keys():
        print('User account already exists')
        sys.exit()
    else:
        print("Entering nothing will default to a 'yes' response")
        is_custom = input("Do you want to customize password? (y/n): ").lower().strip() not in ('no', 'n')
        if is_custom:
            lower_flag, upper_flag, special_flag, number_flag, valid_len = pass_create_prompt()
            custom_password_obj = Password(lower_flag, upper_flag, special_flag, number_flag, valid_len)
            write_account(data, account_name, custom_password_obj.get())
        else:
            password_obj = Password(True, True, True, True, PASS_LEN)
            write_account(data, account_name, password_obj.get())


def retrieve_account():
    """Retrieves a user account password from dataset"""
    account_name = sys.argv[2]
    source = read()
    data = decrypt_data(source)
    if account_name in data.keys():
        pyperclip.copy(data[account_name])
        print('Password for ' + account_name + ' copied to clipboard.')
    else:
        print('User account does not exist')
        sys.exit()


def delete_account():
    """Deletes a user account password from dataset"""
    account_name = sys.argv[2]
    source = read()
    data = decrypt_data(source)
    if account_name in data.keys():
        response = input(f'Are you sure you want to remove {account_name} from dataset?\nType the name of the account if you are sure: ')
        if account_name == response:
            del data[account_name]
            new_source = encrypt_data(data)
            try:
                with open(FILEPATH, 'wb') as f:
                    f.write(new_source)
            except FileNotFoundError:
                print("Please insert passkey")

            print(f"{account_name} removed from dataset")
        else:
            print('Account not removed')
            sys.exit()
    else:
        print(f'{account_name} does not exist in dataset')
        sys.exit()


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print(HELP_TEXT)
        sys.exit()
    elif len(sys.argv) > 3:
        print(HELP_TEXT)
        sys.exit()

    command = sys.argv[1] # First command line argument is the keyword

    match command:
        case 'help':
            _help()
        case 'gen':
            gen()
        case 'list':
            _list()
        case 'crt' if len(sys.argv) == 3:
            create_account()
        case 'del' if len(sys.argv) == 3:
            delete_account()
        case 'get' if len(sys.argv) == 3:
            retrieve_account()
        case _:
            print(HELP_TEXT)
            sys.exit()
