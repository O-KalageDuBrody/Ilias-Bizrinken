from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

menu = [
    {"name": "Burger Maison", "price": 8.50},
    {"name": "Pizza Margherita", "price": 10.00},
    {"name": "Salade César", "price": 7.00}
]
reservations = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def afficher_menu():
    return render_template('menu.html', menu=menu)

@app.route('/reservation', methods=['GET', 'POST'])
def reservation():
    if request.method == 'POST':
        nom = request.form['nom']
        date = request.form['date']
        heure = request.form['heure']
        personnes = request.form['personnes']
        reservations.append({"nom": nom, "date": date, "heure": heure, "personnes": personnes})
        return redirect(url_for('index'))
    return render_template('reservation.html')

@app.route('/commande', methods=['GET', 'POST'])
def commande():
    if request.method == 'POST':
        nom = request.form['nom']
        adresse = request.form['adresse']
        telephone = request.form['telephone']
        plats = request.form.getlist('plats')
        total = sum([plat['price'] for plat in menu if plat['name'] in plats])
        return render_template('confirmation.html', nom=nom, adresse=adresse, telephone=telephone, plats=plats, total=total)
    return render_template('commande.html', menu=menu)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nom = request.form['nom']
        email = request.form['email']
        message = request.form['message']
        return redirect(url_for('index'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
