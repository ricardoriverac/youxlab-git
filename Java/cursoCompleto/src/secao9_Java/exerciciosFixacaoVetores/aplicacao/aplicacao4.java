package secao9_Java.exerciciosFixacaoVetores.aplicacao;

import java.util.Scanner;

public class aplicacao4 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int quantidadePares, cont = 1 ;
        int [] numLista = new int[cont];
        char resp;
        while(true) {
            cont += 1;
            System.out.println("Digite um número: ");
            numLista[cont] = sc.nextInt();
            System.out.println("Deseja continuar? [S/N]");
            resp = sc.next().toUpperCase().charAt(0);
            if (resp == 'N') {
                break;
            }

        }
        quantidadePares = 0;
        for (int i = 0; i < numLista.length; i++) {
            if (numLista[i + 1] % 2 ==0) {
                quantidadePares += 1;
                System.out.println("Números pares: "+numLista[i + 1]);
                System.out.print("Quantidade de pares: "+quantidadePares);
            }
        }
    }
}
