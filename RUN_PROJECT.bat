@echo off
call venv\Scriptsctivate
python simulator\generate_dataset.py
python ml	rain_model.py
python backendpp.py
