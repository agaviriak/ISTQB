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
connection.query("select * from notas", function(error,resultado){
    /*console.log(resultado),*/
    console.log('Errores en la consulta:  ' + error),
    console.log("Total Registros: " + resultado.length),
    console.log(resultado[6])

});
/*var insertar= "insert into notas (Nombre,Materia,Nota) values ('Lucas','Matematicas',4)";
connection.query(insertar,function(error,resultado){
    console.log(error),
    console.log("Registros Insertados :"+resultado.affectedRows)
});*/
process.stdout.write("Esta es otra manera de imprimir\n", function(){

});
process.stdin.on('data',function(data){
    process.stdout.write(data.toString());
});

/*process.stdin.on('nombre',*/
connection.end();