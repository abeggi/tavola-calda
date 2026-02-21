# 1. Crea un virtual environment (opzionale ma consigliato)
python -m venv venv

## Attivalo:
# Su Linux/Mac:
source venv/bin/activate

# 2. Installa Flask
pip install flask

# 3. Crea la cartella per i dati
mkdir data

# 4. (Opzionale) Imposta variabili d'ambiente
export SECRET_KEY="la-tua-chiave-segreta"
export ADMIN_PASSWORD="tuapassword"

# 5. Avvia l'app
python app.py
