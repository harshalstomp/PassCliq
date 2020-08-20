# PassCliq 

PassCliq because everything is just a click away!

A credential fort knox's first version released.

PassCliq is an intuitive tool to generate strong passwords and preserving the credentials in the vault.

PassCliq never shares the vault with the internet.


## Objective 

I was finding a hard time to manage all my gaming and other services credentials. The sole purpose of this application was to make credential management easy. I will be using this application to store all my drive, placement and gaming credentials. It is recommended to always have a backup of the vault file, so that in the case of a hard drive or OS failure the credentials are safe. Good luck using it :smile:. 

## Contents
* [Features](https://github.com/harshalstomp/PassCliq#features)
  * [Future release](https://github.com/harshalstomp/PassCliq#features)
* [Usage](https://github.com/harshalstomp/PassCliq#screenshots)
  * [Generating Password](https://github.com/harshalstomp/PassCliq/blob/master/README.md#generating-password)
  * [Database Window](https://github.com/harshalstomp/PassCliq/blob/master/README.md#the-database-window)
  * [Adding Credentials](https://github.com/harshalstomp/PassCliq/blob/master/README.md#adding-credentials)
  * [Deleting Credentials](https://github.com/harshalstomp/PassCliq/blob/master/README.md#deleting-credentials)
  * [Accessing the Database](https://github.com/harshalstomp/PassCliq/blob/master/README.md#accessing-credentials)
* [Development](https://github.com/harshalstomp/PassCliq#development)
* [Contributors](https://github.com/harshalstomp/PassCliq#contributors)

## Features
* Strong password generator which includes numbers,letters and symbols
* Simple and consistent UI
* Readily accessible credential manager
* Local database storage system
* Can be run on any system where Python is installed

### Future releases
* AES Encryption System while storing the credentials in the CSV file.
* A password strength analyzer.
* Backup of the VAULT.


## Usage

### Generating Password

Generate a random strong password.

![__IMAGE__](https://github.com/harshalstomp/PassCliq/blob/master/Screenshots/Screenshot%20(72).png)


### The database window

This window offer a variety of features like adding credentials, viewing credentials and deleting credentials.

![__IMAGE__](https://github.com/harshalstomp/PassCliq/blob/master/Screenshots/Screenshot%20(73).png)


### Adding Credentials

You can add credentials by entering the service name, username and password.

![__IMAGE__](https://github.com/harshalstomp/PassCliq/blob/master/Screenshots/Screenshot%20(75).png)


### Deleting Credentials

You can delete the previously added credentials by entering the service name and username.

![__IMAGE__](https://github.com/harshalstomp/PassCliq/blob/master/Screenshots/Screenshot%20(76).png)


### Accessing Credentials

You can view the credentials and access them here.

![__IMAGE__](https://github.com/harshalstomp/PassCliq/blob/master/Screenshots/Screenshot%20(74).png)


## Development

* This application is purely written in `Python`.
* The packages used in this application are `TKinter`, `Pandas`, `Pyperclip`, `OS`, `pandastable` and `random`.
* The VAULT is just a `.csv` file, it can be externally edited and accessed using `MSExcel`.

## Code Reviews

If you have any code improvements:

* Clone [PassCliq](https://github.com/harshalstomp/PassCliq/)
* Make your edits
* Add your name to the contributors
* Send a PR

Or, if you’re feeling lazy, create an issue and we’ll think about it.

## Contributors

* [harshalstomp](https://github.com/harshalstomp/)


