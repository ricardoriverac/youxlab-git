package Estruturas_Repetitivas.aula_01;

import java.util.Scanner;

public class exer3 {
    static void main() {
        Scanner sc = new Scanner(System.in);

        int diesel = 0, alcool = 0, gasolina = 0;
        System.out.println("""
                1 - Álcool
                2 - Gasolina
                3 - Diesel
                4 - Fim""");
        int escolha = 0;


        while (escolha != 4) {
            escolha = sc.nextInt();
            if (escolha == 1) {
                alcool += 1;
            }
            else if (escolha == 2) {
                gasolina += 1;
            }
            else if (escolha == 3) {
                diesel += 1;
            }
        }
        System.out.println("MUITO OBRIGADO");
        System.out.println("Álcool = " + alcool);
        System.out.println("Gasolina = " + gasolina);
        System.out.println("Diesel = " + diesel);
    }
}
