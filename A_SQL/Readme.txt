*** Pasos para establecer la conexión desde JS a MySQL
1) Levantar BD en MySQL y verificar los siguientes parámetros:
    host: 'localhost/IP/o DNS NAME del servicio MYSQL',
    user: 'USUARIO',
    password: 'PASSWORD',
    database: 'BDNAME',
    port: 3306
2) Crear una carpeta para el proyecto de conexión en su editor de código
    Ej: c:\MySQL
3) en la carpeta del proyecto se crea un archivo js donde se pondrán los parámetro de la conexión
    Ej: mysql.js
4) En consola de terminal sobre la carpeta de proyecto se inicializa el package.json
   necesario para la conexión. (Gestiona de una forma clara y sencilla las dependencias necesarias para que la aplicación pueda funcionar correctamente)
    c:\MySQL>npm init -y
5) Instalar el módulo de conexión a BD MySQL
    c:\MySQL>npm install mysql
6) Crear las instrucciones de conexión en el archivo .js (mysql.js)
    const mysql = require('mysql');
const connection = mysql.createConnection({
   host: 'localhost',
   user: 'root',
   password: '',
   database: 'agaviria',
   port: 3306
});
connection.connect(function(error){
   if(error){
      throw error;
   }else{
      console.log('Conexion correcta.');
   }
});

