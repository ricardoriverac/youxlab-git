package secao9_Java.exerciciosFixacaoVetores.aplicacao;

import java.util.Scanner;

public class aplicacao2 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        System.out.print("Quantos números você irá digitar? ");
        int n = sc.nextInt();
        int [] numerosLista = new int[n];
        for(int i = 0; i < n; i++){
            numerosLista[i] = sc.nextInt();
        }
        System.out.print("Valores = " );
        for (int i = 0; i<numerosLista.length; i++){
            System.out.print(numerosLista[i] + " ");
        }
        int soma = 0;
        System.out.print("\nSoma = ");
        for (int i = 0; i < numerosLista.length; i++){
            soma += numerosLista[i];
        }
        System.out.print(soma);
        double media = soma/numerosLista.length;
        System.out.print("\nMedia = " + media);
    }
}
