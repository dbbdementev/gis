-----------------------|-------------------------------------------

[gis.py](https://github.com/dbbdementev/gis/blob/master/gis.py)               | главный модуль с кодом
[test_time.py](https://github.com/dbbdementev/gis/blob/master/test_time.py)      | тестирование на скорость работы программы
[translate.py](https://github.com/dbbdementev/gis/blob/master/translate.py)         | перевод с транскрипции на русский
[result.csv](https://github.com/dbbdementev/gis/blob/master/result.csv)           | результат выполнения кода программы
[testdata-small.csv](https://github.com/dbbdementev/gis/blob/master/testdata-small.csv)   | база с начальными данными

-----------------------|-------------------------------------------
Для запуска программы в консоле используйте код gis.py -i testdata-small.csv -o result.csv.
Код хорошо работает при небольшом объёме данных, при больших размерах нужно изменить структуру кода, чтобы чтение
данных происходило не целиком, а, например построчно.
при запуске в linux нужно удалить кодировку encoding='utf-8'



