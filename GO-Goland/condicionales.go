package main

import "fmt"

func main() {
	var valor1, valor2 int
	fmt.Print("Digita un valor: ")
	fmt.Scan(&valor1)
	fmt.Print("Digita otro valor: ")
	fmt.Scan(&valor2)
	if valor1 > valor2 {
		fmt.Printf("EL valor mas alto q dijitaste es : %d", valor1)
	} else {
		fmt.Printf("EL valor mas alto q dijitaste es : %d", valor2)
	}
}
