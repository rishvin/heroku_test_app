python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

export FLASK_APP=src/apps/carbon_emission_app.py

python run_services.py
