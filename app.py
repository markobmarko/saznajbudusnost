import random
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

PREDVIĐANJA = [
    "Sledeće godine dobijaš na lotou, ali gubiš ključeve od auta. Kupuješ jahtu u CG.",
    "Upoznaćeš osobu iz dijaspore koja će te voditi u Beč na kafu. Budućnost ti je svetla i puna eura.",
    "Postaješ lokalni tajkun. Svi će te mrzeti, ali će ti svi tražiti pare na zajam.",
    "Tvoja budućnost je vezana za tehnologiju. Pravićeš viralne sajtove i kupiti Mercedes do 2030."
]

@app.route('/', methods=['GET', 'POST'])
def index():
    rezultat = None
    if request.method == 'POST':
        # Prikupljanje podataka iz forme
        data = {
            "Ime": request.form.get('ime'),
            "Prezime": request.form.get('prezime'),
            "Datum": request.form.get('datum'),
            "Mesto": request.form.get('mesto')
        }
        
        # Slanje podataka u tvoju Google Tabelu
        api_url = "https://sheetdb.io/api/v1/3jl2x60m2hsgh" 
        try:
            requests.post(api_url, json={"data": [data]})
        except Exception as e:
            print(f"Greška pri slanju: {e}")
            
        rezultat = random.choice(PREDVIĐANJA)
        
    return render_template('index.html', rezultat=rezultat)

if __name__ == '__main__':
    app.run(debug=True)
