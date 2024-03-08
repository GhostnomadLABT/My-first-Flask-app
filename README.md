# My-first-Flask-app
Implementar un formulario con nombre de usuario y contraseña usando Flask 
1)Primero se debe montar el entorno virtual con el siguiente comando:
  py -m venv virtual_environment
2)Despues habilitar el entorno virtual
   .\virtual_environment\Scripts\activate
3)Se descarga FLASK
  pip install flask
4) Habilitado el entorno virtual compilar app.py
    py app.py
5)Una vez que se realizo lo anterior poner en el buscador la siguiente liga
  http://localhost:8081/login
  esto mostrara el formulario de login con las especificaciones de:
  primer letra del nombre en mayuscula
  password con verificacion de numeros y letras
  ejemplo:
  Usuario: Luis
  Password: 1w2e3r4
  6) Si el usuario o contraseña son incorrectos se mantendra en el formulario, si los datos son correctos 
  aparece un mensaje de "Ingreso a la cuenta correctamente"
  7) La carpeta completa contiene el archivo app.py, una carpeta "templates" para archivos HTML y otra carpeta "static" para archivos CSS
