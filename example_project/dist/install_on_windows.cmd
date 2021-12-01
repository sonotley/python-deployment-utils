@echo off
echo *************************
echo Installing Example Project
echo *************************
IF %1.==. set filePath=C:\example-project& GOTO install
set filePath=%1\example-project
:install
echo Installing to %filePath%
echo Building Python virtual environment
py -3 -m venv %filePath%\env
FOR /F "delims=" %%i IN ('dir /b example_package*.whl') DO set target=%%i
call %filePath%\env\Scripts\activate
pip install %target%
mklink /H %filePath%\my-executable.exe %filePath%\env\Scripts\my-executable.exe
xcopy setup.yaml %filePath%\ /F/Q
echo *************************
echo Installation complete
echo *************************