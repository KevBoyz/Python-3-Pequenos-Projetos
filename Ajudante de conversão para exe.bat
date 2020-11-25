@echo off
: Menu
color a
echo.
echo Ajudante de conversao PyToExe
echo.
echo Selecione a opcao:
echo [1] Requisitos
echo [2] Instalar AutoPyToExe
echo [3] Executar AutoPyToExe
echo [4] Sair
echo. 
set /p slc=Opcao:
if %slc% == 1 (echo Como pre requisito e nessesario ter instalado o pip, voce pode instala-lo a parte mais o ideal e que ele seja instalado junto ao Python3 para prevencao de bugs.No caso de erros ao ultilzar o pip adicione ao Path do cmd manualmente)
if %slc% == 2 (pip install auto-py-to-exe)
if %slc% == 3 (python -m auto_py_to_exe)
if %slc% == 4 (exit)
goto Menu
