REM Startet das Venv, mithilfe eines Batch - Files und braucht somit keinen Interpreter.
REM Sobald aber das Venv gestartet ist, kann main.py auf den mitgelieferten Interpreter zugreifen, da dieser im Venv steckt
REM Am Ende wird das venv wieder geschlossen (nur für Logik, hat wahrscheinlich keinen praktischen Nutzen)

@echo off
cd /d %~dp0
call venv\Scripts\activate
python main.py
deactivate
