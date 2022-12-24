from privatekey import PrivateKey
from bit import Key
from multiprocessing import cpu_count, Process
from requests import get
from time import sleep
#from file_management import FileManagement

with open('wallets-test.txt', 'r') as file:
    #list of funded wallets
    wallets = set(file.read().split('\n'))
    if '' in wallets:
        wallets.remove('')
        
#inputfile = 'default_wordlist.txt'
outputfile = 'output.txt'
#file = FileManagement(outputfile, inputfile)
#wordlist = file.read_dictionary()

def bruteforce(y):
    
    print(f'Instance y{y + 1}: - Raising hell...')
    
    pkey = PrivateKey()
    
    for passphrase in wallets:
        
        pkey.from_passphrase(passphrase)
        wif1 = pkey.privatekey_to_wif(compressed=True)
        wif2 = pkey.privatekey_to_wif()
        key1 = Key(wif1)
        key2 = Key(wif2)
        
        if (key1.address or key2.address) in wallets:
            print(f'y{y + 1} Got a Match! C: {key1.address} : P: {passphrase}')
            print(f'y{y + 1} Got a Match! U: {key2.address} : P: {passphrase}')
            with open(outputfile, 'a') as result:
                result.write(f'P: {passphrase} - C: {key1.address} - U: {key2.address}')

def debug_bruteforce(y):
    
    print(f'Instance y{y + 1}: - Raising hell...')
    
    pkey = PrivateKey()
    for passphrase in wallets:
        pkey.from_passphrase(passphrase)
        wif1 = pkey.privatekey_to_wif(compressed=True)
        wif2 = pkey.privatekey_to_wif()
        key1 = Key(wif1)
        key2 = Key(wif2)

        print(f'Instance y{y + 1}: - {key1.address} : {key2.address} : {passphrase} : 0')
        
        if (key1.address or key2.address) in wallets:
            print(f'y{y + 1} Got a Match! C: {key1.address} : P: {passphrase}')
            print(f'y{y + 1} Got a Match! U: {key2.address} : P: {passphrase}')
            with open(outputfile, 'a') as result:
                result.write(f'P: {passphrase} - C: {key1.address} - U: {key2.address}')
                
def main():
  
    menu_string = 'We\'re all mad here.\m\m\m\mA tool by Bigcointalk.org\n\n\n\nSelect bruteforce mode:\n'
    mode = (None, bruteforce, debug_bruteforce)
    for count, function in enumerate(mode):
        try:
            if 'debug' in function.__name__:
                menu_string += f'{count} - {function.__name__} (Debug Mode)\n'
            else:
                menu_string += f'{count} - {function.__name__}\n'
        except AttributeError:
            menu_string += f'{count} - Exit\n'
    print(menu_string)

    try:
        choice = int(input('> '))
        print(f'On a scale from 1 to {cpu_count()}, how much hell would you like to raise?')
        cpu_cores = int(input('> '))
        cpu_cores = cpu_cores if 0 < cpu_cores < cpu_count() else cpu_count()
        option = choice if 0 < choice <= len(mode) - 1 else 0
    except ValueError:
        option = 0
        cpu_cores = 0

    print(f'Starting bruteforce with {cpu_cores} hardcore(s)...\n')
    
    if mode[option] and 'debug' in mode[option].__name__:
        print(f'Debug mode...\n')
        
    instances = []
    for i in range(cpu_cores):
        instance = Process(target=mode[option], args=(i))
        instances.append(instance)
        instance.start()
    for instance in instances:
        instance.join()

    print('tehehe')

if __name__ == '__main__':
    main()
