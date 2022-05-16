package main

import (
	"fmt"
	"strconv"
)

func main() {
	edad := 22
	edad_int := strconv.Itoa(edad) //Itoa devuelve un parámetro
	fmt.Println(edad_int)

	edad2 := "22"
	edad_str, err := strconv.Atoi(edad2) //Atoi devuelve 2 parámetros
	fmt.Print(edad_str, err)
}
