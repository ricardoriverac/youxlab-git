package secao_06;

import java.util.Scanner;

public class exercicio_3 {
    static void main() {
        Scanner sc = new Scanner(System.in);
        int alcool = 0;
        int gasolina = 0;
        int diesel = 0;
        System.out.println(
                "1 - Alcool\n" +
                        "2 - Gasolina\n" +
                        "3 - Diesel\n" +
                        "4 - Fim");

        int tipo = sc.nextInt();

        while(tipo != 4){
            if (tipo == 1) {
                alcool = alcool + 1;
            }
            else if (tipo == 2) {
                gasolina = gasolina + 1;
            }
            else if (tipo == 3) {
                diesel = diesel + 1;
            }
            tipo = sc.nextInt();

        }
        System.out.println("Muito obrigada");
        System.out.println("Alcool = " + alcool);
        System.out.println("Gasolina =" + gasolina);
        System.out.println("Diesel =" + diesel);

    }
}
