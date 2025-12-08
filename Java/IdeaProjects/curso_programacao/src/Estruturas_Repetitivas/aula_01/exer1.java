package Estruturas_Repetitivas.aula_01;

import java.util.Scanner;

public class exer1 {
    static void main() {
        Scanner sc = new Scanner(System.in);

        int senha = sc.nextInt();
        while (senha != 2002) {
            System.out.println("Senha Inválida");
            senha = sc.nextInt();
            if (senha == 2002) {
                System.out.println("Acesso Permitido");
            }
        }
    }
}
