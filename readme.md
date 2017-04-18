Installation
------------
Make sure that the release file is unpacked. You will see the following files.

file name  | contents of the file
----------------|----------------------
[gis.py](https://github.com/dbbdementev/gis/blob/master/gis.py)       | main module with code
[test_time.py](https://github.com/dbbdementev/gis/blob/master/test_time.py)       | module for testing the speed of the program
[translate.py](https://github.com/dbbdementev/gis/blob/master/translate.py)   | module used to translate text from translit to Russian
[result.csv](https://github.com/dbbdementev/gis/blob/master/result.csv)       | result of program execution
[testdata-small.csv](https://github.com/dbbdementev/gis/blob/master/testdata-small.csv)    | base with initial data
[readme.md](https://github.com/dbbdementev/gis/blob/master/readme.md)    | this file


Recommendations
------------

To run the program in the console, use the code: gis.py -i testdata-small.csv -o result.csv.
The code works well for a small amount of data, for large sizes it is necessary to change the structure of the code to read
Data occurred not entirely, but, for example, line by line.
At start in linux it is necessary to delete the encoding encoding = 'utf-8'
