package secao6_estruturasRepetitivas;

import java.util.Scanner;

public class testeFor {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int entrada = sc.nextInt();
        for (int i= 0; i < 4; i++) {
            System.out.println("valor de i: " + i + "\nValor digirado: " + entrada);
            entrada = sc.nextInt();
        }
    }
}
