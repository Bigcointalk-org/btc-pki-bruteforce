# btc-pki-bruteforce

A tool for testing the security of pubkey privkey infrastructure used in popular cryptocurrencies.

"Bitcoin uses public key cryptography to create a key pair that controls access to bitcoin. The key pair consists of a private key and—derived from it—a unique public key. The public key is used to receive funds, and the private key is used to sign transactions and spend funds."

## Features
 - VERY FAST because it don't communicate with the network
 - A current (Dec. 2022) list of funded wallets (~1.5GB)
 - Multiple instances (per core)
 - Debug mode for testing
 - Writes findings to file (output.txt)

*Funded Wallets:*

https://bigcointalk.org/download/wallets1.txt

https://bigcointalk.org/download/wallets2.txt

## Requirements
Python3, base58, bit

https://bigcointalk.org/
