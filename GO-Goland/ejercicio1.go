package main

import (
	"fmt"
	"strconv"
)

func main() {
	fmt.Println("Hola mundo")    //impresion en pantalla
	cadena := "Alberto"          //asi se inicia una variable
	cadena = cadena + " Gaviria" //así se cambia el valor a una variable existente
	fmt.Println(cadena)
	edad := strconv.Itoa(22) //convierte integer a string
	fmt.Println("Mi edad es " + edad)
}
