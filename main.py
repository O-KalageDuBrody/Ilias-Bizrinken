from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "secret_key"

menu = [
    {"name": "msemen kefta", "price": 620.00},
    {"name": "", "price": 10.00},
    {"name": "Salade César", "price": 7.00}
]

users = {}
reservations = []
orders = {}
avis_list = []

@app.route('/')
def index():
    if 'username' in session:
        user = session['username']
        user_orders = orders.get(user, [])
        return render_template('index.html', avis_list=avis_list, user=user, orders=user_orders)
    return render_template('index.html', avis_list=avis_list, user=None)

@app.route('/menu')
def afficher_menu():
    return render_template('menu.html', menu=menu)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        if username in users:
            return "Ce nom d'utilisateur est déjà pris."
        password = generate_password_hash(request.form['password'])
        users[username] = {"password": password, "orders": []}
        session['username'] = username
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and check_password_hash(users[username]['password'], password):
            session['username'] = username
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

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
    if 'username' not in session:
        return redirect(url_for('login'))
    username = session['username']
    if request.method == 'POST':
        plats_selectionnes = request.form.getlist('plats')
        total = sum([plat['price'] for plat in menu if plat['name'] in plats_selectionnes])
        adresse = request.form['adresse']
        telephone = request.form['telephone']
        order_id = len(orders.get(username, [])) + 1
        order = {"id": order_id, "plats": plats_selectionnes, "total": total, "adresse": adresse, "telephone": telephone}
        
        if username not in orders:
            orders[username] = []
        orders[username].append(order)
        return redirect(url_for('confirmation', order_id=order_id))
    return render_template('commande.html', menu=menu)

@app.route('/confirmation/<int:order_id>')
def confirmation(order_id):
    if 'username' not in session:
        return redirect(url_for('login'))
    username = session['username']
    user_orders = orders.get(username, [])
    order = next((o for o in user_orders if o["id"] == order_id), None)
    if order:
        return render_template('confirmation.html', nom=username, order=order)
    return redirect(url_for('index'))

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nom = request.form['nom']
        email = request.form['email']
        message = request.form['message']
        return redirect(url_for('index'))
    return render_template('contact.html')

@app.route('/ajouter_avis', methods=['POST'])
def ajouter_avis():
    if 'username' in session:
        nom = session['username']
    else:
        nom = "Anonyme"
    commentaire = request.form['commentaire']
    avis_list.append({"nom": nom, "message": commentaire})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=8000)
