rem Example batch script to run the project
START firefox http://localhost:5000
python -m venv venv
call venv\Scripts\activate.bat
pip install -r requirements.txt
flask --app app run

