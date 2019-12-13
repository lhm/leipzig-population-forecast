import tabula
from pathlib import Path
import urllib.request

root = Path(__file__).parents[1]

pdf = root / 'pdfs/bevoelkerungsvorausschaetzung-leipzig-2019.pdf'

if not pdf.exists():
    urllib.request.urlretrieve(
        "https://www.leipzig.de/fileadmin/mediendatenbank/leipzig-de/Stadt/02.1_Dez1_Allgemeine_Verwaltung/12_Statistik_und_Wahlen/Stadtforschung/Bevolkerungsvorausschatzung_2019.pdf",
        pdf
    )

headers = [
    'Jahr',
    'Geburten',
    'Sterbefälle',
    'Saldo (natürlich)',
    'Zuzüge',
    'Wegzüge',
    'Saldo (Aussenwanderungen)',
    'Gesamtsaldo',
    'Einwohner'
]

parse_thousands = lambda x: (int(float(x.replace(",", ".")) * 1000 ))

df = tabula.read_pdf(pdf, 
    area=(396.26,54.323,759.405,465.838), 
    pages=24, 
    stream=True,
    pandas_options={
        'header': None,
        'names': headers,
        'index_col': ['Jahr'],
        'decimal': ','
    }
)

out = root / 'data/population-forecast.csv'
df.to_csv(out)
