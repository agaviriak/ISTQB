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
connection.end();