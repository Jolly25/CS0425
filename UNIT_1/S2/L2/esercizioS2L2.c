/*
Lo scopo di oggi sarà realizzare due programmi in C:
1 - Si scriva un programma che esegua l'operazione di divisione tra due numeri inseriti dall'utente. 
*/

#include <stdio.h>

int main () {
    float num1;
    float num2;
    float risultato;

    printf("Inserisci il primo numero: "); 
    scanf("%f", &num1);

    printf("Inserisci il secondo numero: "); 
    scanf("%f", &num2);

    risultato = num1/num2;

    printf("Il risultato tra %.f e %.f è %.1f\n", num1, num2, risultato);

    return 0;
}

//OUTPUT CON 4 E 2:
/*
iriscanole@Mac Esercizi in C % gcc esercizioS2L2.c -o esercizioS
iriscanole@Mac Esercizi in C % ./esercizioS                     
Inserisci il primo numero: 4
Inserisci il secondo numero: 2
Il risultato tra 4 e 2 è 2.0
*/