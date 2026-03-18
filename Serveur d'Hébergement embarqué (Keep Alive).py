# --- EXTRAIT : Serveur Flask embarqué pour empêcher la mise en veille (Hosting) ---
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot Premium is Running! (Keep Alive Active)"

def keep_alive():
    # Lance le serveur web dans un thread séparé pour ne pas bloquer le bot Discord
    t = Thread(target=lambda: app.run(host='0.0.0.0', port=8080))
    t.start()
