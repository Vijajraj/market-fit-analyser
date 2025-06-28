@echo off
echo ==================================================
echo     🚀 Starting Market Fit Analyser Environment
echo ==================================================

:: Navigate to project directory
cd /d C:\market-fit-analyser

:: Install required libraries
echo Installing dependencies...
pip install -r requirements.txt

:: Check if 'model' folder exists, if not, create it
if not exist model (
    mkdir model
)

:: Train the dummy ML model
echo Training dummy pricing model...
python train_dummy_model.py

:: Launch Streamlit app
echo Starting Streamlit app...
streamlit run app.py

pause
