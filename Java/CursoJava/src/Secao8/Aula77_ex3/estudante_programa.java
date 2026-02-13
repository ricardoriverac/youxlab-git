package Secao8.Aula77_ex3;

import java.util.Locale;
import java.util.Scanner;

public class estudante_programa {

        public static void main(String[] args) {
            Locale.setDefault(Locale.US);
            Scanner sc = new Scanner(System.in);

            estudante Estudante = new estudante();
            System.out.print("Nome: ");
            Estudante.name = sc.nextLine();
            System.out.print("Primeira nota: ");
            Estudante.nota1 = sc.nextDouble();
            System.out.print("Segunda nota: ");
            Estudante.nota2 = sc.nextDouble();
            System.out.print("Terceira nota: ");
            Estudante.nota3 = sc.nextDouble();
            System.out.printf("NOTA FINAL: %.2f%n", Estudante.notafinal());
            if (Estudante.notafinal() < 60.0) {
                System.out.println("FAILED");
                System.out.printf("MISSING %.2f POINTS%n", Estudante.Pontosfalta());
            }
            else {
                System.out.println("PASS");
            }
            sc.close();
        }
    }

