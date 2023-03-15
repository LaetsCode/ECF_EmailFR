# EmailFR

EmailFR is a Python script to extract french email adresses from a text file.
The email pattern has to follow a few rules :
- some special characters are unauthorized, following [gmail](https://support.google.com/mail/answer/9211434?hl=en) rules
- it can't start with a "." 
- it must end in ".fr"

## Installation

The script uses Python3 (3.10.10) and the Python libraries re and sys.
The project can be cloned using
```bash
git clone https://github.com/LaetsCode/ECF_EmailFR.git

```

## Usage

The script takes one argument in the command line : the text file you want to extract french emails from.

```bash
python3 EmailFR.py inputfile.txt

```
And the console output will be the adresses.

## Contributing

Pull requests and suggestions are welcome. 
