# 🍔 La Casse-Crouterie

<h1 align="center">🍽️ La Casse-Crouterie</h1>
<h3 align="center">Restaurant & Application Web — Projet Flask 2026</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/Framework-Flask-black.svg?logo=flask" alt="Flask">
  <img src="https://img.shields.io/badge/Database-SQLite-lightgrey.svg" alt="SQLite">
  <img src="https://img.shields.io/badge/UI-Dark%20Mode%20Ready-purple.svg" alt="Dark Mode">
</p>

<hr>

<h2 align="center">🏪 Présentation du Restaurant</h2>

<p>
<strong>La Casse-Crouterie</strong> est un restaurant moderne et convivial où la street-food rencontre les cuisines du monde 🌍.<br>
Notre objectif est de proposer des plats variés, gourmands et accessibles, dans une ambiance chaleureuse et dynamique.
</p>

<p>
Que ce soit pour un repas rapide, une commande à emporter ou une réservation entre amis,  
La Casse-Crouterie offre une expérience simple, fluide et savoureuse.
</p>

<h3>🍴 Spécialités</h3>

<ul>
  <li>🥙 Chawarma</li>
  <li>🥞 Msemen Kefta</li>
  <li>🍛 Couscous Royale</li>
  <li>🍌 Futu Banane</li>
  <li>🌶️ Street-food indienne</li>
</ul>

<hr>

<h2 align="center">🌐 Présentation du Site</h2>

<p>
Ce projet est une application web complète développée avec <strong>Flask</strong>.  
Elle permet de gérer toutes les fonctionnalités essentielles d’un restaurant moderne :
</p>

<ul>
  <li>📖 Consultation du menu</li>
  <li>🔍 Détails des plats avec image, prix et description</li>
  <li>🛒 Commande en ligne</li>
  <li>📅 Réservation de tables</li>
  <li>📝 Avis clients</li>
  <li>👤 Gestion des comptes utilisateurs</li>
  <li>🌙 Mode sombre / clair</li>
</ul>

<hr>

<h2>✨ Fonctionnalités principales</h2>

<h3>👤 Utilisateurs</h3>
<ul>
  <li>Inscription & connexion</li>
  <li>Mots de passe sécurisés (hash)</li>
  <li>Sessions utilisateurs</li>
</ul>

<h3>🍽️ Menu</h3>
<ul>
  <li>Affichage dynamique des plats</li>
  <li>Page de détail pour chaque plat</li>
  <li>Images associées</li>
</ul>

<h3>🛒 Commandes</h3>
<ul>
  <li>Sélection multiple de plats</li>
  <li>Calcul automatique du total</li>
  <li>Saisie de l’adresse et du téléphone</li>
  <li>Historique par utilisateur</li>
</ul>

<h3>📅 Réservations</h3>
<ul>
  <li>Nom, date, heure, nombre de personnes</li>
  <li>Stockage en base de données</li>
</ul>

<h3>📝 Avis clients</h3>
<ul>
  <li>Choix libre du nom</li>
  <li>Si vide → username de session</li>
  <li>Sinon → “Anonyme”</li>
  <li>Affichage du plus récent au plus ancien</li>
</ul>

<h3>🌙 Mode sombre</h3>
<ul>
  <li>Bouton de bascule 🌙 / ☀️</li>
  <li>Préférence sauvegardée</li>
  <li>Transitions fluides</li>
</ul>

<h3>🎨 UI & UX</h3>
<ul>
  <li>Animations CSS</li>
  <li>Transitions entre pages</li>
  <li>Interface moderne et responsive</li>
</ul>

<hr>

<h2>🧩 Structure du projet</h2>

<pre>
Ilias-Bizrinken/
│
├── main.py            → Application Flask principale
├── init_db.py         → Initialisation de la base de données
├── database.db        → Base SQLite
│
├── templates/
│   ├── index.html
│   ├── menu.html
│   ├── plat_detail.html
│   ├── reservation.html
│   ├── commande.html
│   ├── contact.html
│   ├── login.html
│   ├── register.html
│   └── confirmation.html
│
├── static/
│   ├── style.css
│   ├── transition.js
│   ├── darkmode.js
│   ├── logo.jpeg
│   └── detail/
│       └── *.jpg        → Images des plats
</pre>

<hr>

<h2>🛠️ Technologies utilisées</h2>

<ul>
  <li>🐍 Python</li>
  <li>⚗️ Flask</li>
  <li>🗃️ SQLite</li>
  <li>🧱 HTML / CSS</li>
  <li>✨ JavaScript</li>
  <li>🧩 Jinja2</li>
</ul>

<hr>

<h2>🧠 Sécurité</h2>

<ul>
  <li>Mots de passe hashés (Werkzeug)</li>
  <li>Sessions sécurisées</li>
</ul>

<hr>

<h2>▶️ Installation & Lancement</h2>

<ol>
  <li>Installer les dépendances :</li>
</ol>

<pre><code class="language-bash">
pip install flask werkzeug
</code></pre>

<ol start="2">
  <li>Lancer le serveur :</li>
</ol>

<pre><code class="language-bash">
python main.py
</code></pre>

<p>Ouvrir ensuite dans le navigateur :</p>

<pre>
http://localhost:8000
</pre>

<hr>

<h2>🧹 Reset de la base de données</h2>

<pre><code class="language-bash">
1. Arrêter le serveur
2. Supprimer database.db
3. python init_db.py
4. python main.py
</code></pre>

<hr>

<h2>🎯 Objectif du projet</h2>

<p>
Ce projet démontre la capacité à :
</p>

<ul>
  <li>Construire une application web complète</li>
  <li>Gérer une base de données</li>
  <li>Sécuriser les utilisateurs</li>
  <li>Créer une interface moderne</li>
  <li>Réaliser un site proche d’un produit professionnel</li>
</ul>

<hr>

<h2>👨‍💻 Auteur</h2>

<table>
  <tr><th>Rôle</th><th>Nom</th></tr>
  <tr><td>🧑‍💻 Développeur</td><td>Waroc GUERNALEC</td></tr>
  <tr><td>📆 Année</td><td>2024–2025</td></tr>
  <tr><td>💬 Langage</td><td>Python/HTML/SQL</td></tr>
</table>

<hr>

<p align="center"><em>🍔 La Casse-Crouterie — Le goût du code et de la cuisine réunis.</em></p>
