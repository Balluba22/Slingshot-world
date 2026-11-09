@echo off
REM Ruleaza acest fisier pe Windows (necesita Python 3.9+ instalat, cu "Add to PATH")
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m PyInstaller --noconfirm --clean --onefile --windowed --name SlingshotWorld --icon icon.ico --add-data "..\index.html;." slingshot_app.py
echo.
echo Gata! Aplicatia este in: dist\SlingshotWorld.exe
pause
