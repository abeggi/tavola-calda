## Crea un virtual environment (opzionale ma consigliato)
python -m venv venv

## Attivalo:
source venv/bin/activate

## Installa Flask
pip install flask

## Crea la cartella per i dati
mkdir data

## (Opzionale) Imposta variabili d'ambiente
export SECRET_KEY="la-tua-chiave-segreta"
export ADMIN_PASSWORD="tuapassword"

## Avvia l'app
python app.py
