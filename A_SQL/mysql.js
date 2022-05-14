const { error } = require('console');
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
   }
   else{
      console.log('Conexion correcta.');
   }
});
connection.query("select * from notas", function(error,rows){
    console.log(rows),
    console.log('Errores en la consulta:  ' + error),
    console.log("Total Registros: " + rows.length),
    console.log(rows[6])

});
/*var insertar= "insert into notas (Nombre,Materia,Nota) values ('Lucas','Matematicas',4)";
connection.query(insertar);*/
connection.end();