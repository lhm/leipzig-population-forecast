# Bevölkerungsvorausschätzung Leipzig 2019

Population forecast for Leipzig, Germany as provided by the municipal statistics office.

Source: [Bevolkerungsvorausschatzung_2019.pdf](https://static.leipzig.de/fileadmin/mediendatenbank/leipzig-de/Stadt/02.1_Dez1_Allgemeine_Verwaltung/12_Statistik_und_Wahlen/Stadtforschung/Bevolkerungsvorausschatzung_2019.pdf)
Publisher: [Amt für Statistik und Zahlen](https://www.leipzig.de/buergerservice-und-verwaltung/unsere-stadt/statistik-und-zahlen/)

## Preparation

```
make data/population-forecast.csv
```

This will download the PDF, extract the relevant table and save the CSV in the data directory.

## Requirements

Python3 is used, all dependencies are installed automatically into a Virtualenv
when using the `Makefile`.

## License

The Python files in `scripts` are released under an
[CC0 Public Dedication License](https://creativecommons.org/publicdomain/zero/1.0/).
