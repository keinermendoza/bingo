# Bingo.py 

**Bingo.py** is a command line program whose purpose is to create sets of bingo cards in a printable format (pdf).

The program will fill each page of the pdf document with up to 6 bingo cards, adding as many pages to the document as necessary.
The page size is the same as the one accepted by default in fpdf2, that is, A4, and the orientation is vertical. These characteristics cannot be modified.
* * *

**Quick Start**
+ Create an enviorment with your favorite manager
> for example with venv
```shell
python -m venv venv
``` 
```shell
source venv/bin/activate
```
+ Install the requirements with 
```shell
pip install -r requirements.txt
```

+ follow the next [Simple Usage Guide](#simple-usage-guide)

* * *

**Help**

This program uses the argparse module to parse the command line and the order in wich the commands are written will not alter their behavior.

You can get help by typing one of the following options on the command line

```shell
bingo.py -h
```

```shell
bingo.py --help
```
* * *

## **Simple Usage Guide**

**Required argument**


## **-n**

For simple use it requires at least the "-n" argument that determines the number of cards the set will have. The value being an integer between 1 and 2000.

```shell
python bingo.py -n 2
```
When executing the program, it will check if there is a folder called "bingo" in the directory where the program is located, if not, it will create said folder, establishing as the destination path.

There are 4 other arguments which are optional and are explained below.

* * *

**Optional arguments**

## **-t**

Modifies the title that appears in the header of each bingo card, this can be a string of between 1 and 29 characters (counting blank spaces).
If the string is 15 characters or less, the title will be center justified in the header, with a font size of 16.
If it has more than 15  characters, the string will be left justified in the header with a font size of 12.
By defaul its value is "My Bingo".
The string is also used in the creation of the filename. 

```shell
python bingo.py -t "Bingo 2. A Longer Title" -n 3
```

## **-c**

Sets the font color of the bingo card header. Supports only 6 characters in hexadecimal format.
Its default value is "000000" that is, black.

```shell
python bingo.py -c "ff5733" -t "Bingo 3" -n 6
```

## **-bc**

Sets the background color of the bingo card header. Supports only 6 characters in hexadecimal format.
Its default value is "ffffff" that is, white.

```shell
Usage: python bingo.py -bc "ffc300" -t "Bingo 4" -n 1
```
## **-f**

Determines the font family used in the document. This program supports the 5 fonts integrated in fpdf2 which are:
"helvetica", "times", "courier", "symbol" and "zapfdingbats"; although only the first 3 are useful to represent the English alphabet.
Its default value is "helvetica"

```shell
python bingo.py -f "courier" -t "Bingo 5" -n 4
```

Finally, we can use all the arguments at once:

```shell
python bingo.py -bc "0000ff" -c "ffffff" -f "times" -t "I Love Bingo.py" -n 100
```

* * *
## tests
You can run the test with 
```shell 
pytest tests
```