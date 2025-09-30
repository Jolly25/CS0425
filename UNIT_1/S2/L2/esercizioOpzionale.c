/*
Si scriva un programma in linguaggio C che legga due valori interi e visualizzi la loro media aritmetica.
*/

#include <stdio.h>

int main() {
    int num1, num2;
    double avg;

    printf("Inserisci il primo numero: ");
    scanf("%d", &num1);

    printf("Inserisci il secondo numero: ");
    scanf("%d", &num2);

    avg = (num1 + num2) / 2.0;

    printf("la media tra %d e %d è %.2f\n", num1, num2, avg);

    return 0;
}
//OUTPUT CON 4 E 2
/*
iriscanole@Mac Esercizi in C % gcc esercizioOpzionale.c -o opzionale
iriscanole@Mac Esercizi in C % ./opzionale                          
Inserisci il primo numero: 4
Inserisci il secondo numero: 2
la media tra 4 e 2 è 3.00
*/


//Versione con più valori in entrata

// int main() {
//     int n, i;
//     int sum = 0;
//     double avg;

//     printf("Quanti numeri vuoi inserire? ");
//     scanf("%d", &n);
     
//     int numeri[n];

//     for (i=0; i<n; i++){
//         printf("Inserisci un numero: ");
//         scanf("%d", &numeri[i]);
//         sum += numeri[i];
//     }
//     avg = (double) sum/i;

//     printf("La media è %.2f\n", avg);

//     return 0;
// }

//OUTPUT CON 2 5 7 3:
/*
iriscanole@Mac Esercizi in C % gcc esercizioOpzionale.c -o opzionale
iriscanole@Mac Esercizi in C % ./opzionale                          
Quanti numeri vuoi inserire? 4
INnserisci un numero: 2
INnserisci un numero: 5
INnserisci un numero: 7
INnserisci un numero: 3
La media è 4.25
*/