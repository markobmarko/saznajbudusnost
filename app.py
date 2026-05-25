import random
from flask import Flask, render_template, request
from datetime import datetime

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
        # Uzimamo podatke iz forme
        ime = request.form.get('ime')
        prezime = request.form.get('prezime')
        datum = request.form.get('datum')
        mesto = request.form.get('mesto')
        
        # Upis u fajl (tvoja baza podataka)
        with open("baza_korisnika.txt", "a", encoding="utf-8") as f:
            vreme = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{vreme} | {ime} | {prezime} | {datum} | {mesto}\n")
            
        rezultat = random.choice(PREDVIĐANJA)
        
    return render_template('index.html', rezultat=rezultat)

if __name__ == '__main__':
    app.run(debug=True)