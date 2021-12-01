@echo off
echo *************************
echo Installing VMS Mimic Service
echo *************************
IF %1.==. set filePath=C:\vms-mimic-service& GOTO install
set filePath=%1\vms-mimic-service
:install
echo Installing to %filePath%
echo Building Python virtual environment
py -3 -m venv %filePath%\env
FOR /F "delims=" %%i IN ('dir /b vms_mimic_service*.whl') DO set target=%%i
call %filePath%\env\Scripts\activate
pip install %target%
mklink /H %filePath%\vms-mimic-service.exe %filePath%\env\Scripts\vms-mimic-service.exe
xcopy fonts %filePath%\fonts\ /E/Q
xcopy graphics %filePath%\graphics\ /E/Q
xcopy setup.yaml %filePath%\ /F/Q
echo *************************
echo Installation complete
echo *************************