from flask import Flask, request, jsonify, render_template, redirect, url_for, make_response

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Cambia esto a una clave secreta segura

# Rutas
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)