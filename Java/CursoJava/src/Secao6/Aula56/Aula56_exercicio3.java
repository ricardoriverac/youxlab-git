package Secao6.Aula56;

import java.util.Scanner;

public class Aula56_exercicio3 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int alcool = 0;
        int gasolina = 0;
        int diesel = 0;

        while (true) {
            System.out.print("----POSTO DE COMBUSTÍVEIS-----\n");
            System.out.print(
                    "1-ALCOOL\n" +
                            "2-GASOLINA\n" +
                            "3-DIESEL\n" +
                            "4-FIM\n");
            System.out.print("Digite sua escolha: ");
            int escolha = sc.nextInt();

            if (escolha == 1) {
                alcool++;
            }
            else if (escolha == 2) {
                gasolina++;
            }
            else if (escolha == 3) {
                diesel++;
            }
            else if (escolha == 4) {
                System.out.println("Muito obrigado");
                break;
            }
                }

                System.out.println("Alcool: " + alcool);
                System.out.println("Gasolina: " + gasolina);
                System.out.println("Diesel: " + diesel);

                sc.close();
            }
        }


