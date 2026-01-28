package Secao5.Aula44;

import java.util.Locale;
import java.util.Scanner;

public class aula44_exercicio5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Locale.setDefault(Locale.US);

                int codigo, quantidade;
                double preco = 0.0;
                double total;

                System.out.println("--- LANCHONETE---");
                System.out.println("1 - Cachorro Quente (R$ 4.00)");
                System.out.println("2 - X-Salada (R$ 4.50)");
                System.out.println("3 - X-Bacon (R$ 5.00)");
                System.out.println("4 - Torrada (R$ 2.00)");
                System.out.println("5 - Refrigerante (R$ 1.50)");
                System.out.print("Digite o código do que deseja: ");
                codigo = sc.nextInt();

                System.out.print("Digite a quantidade: ");
                quantidade = sc.nextInt();

                if (codigo == 1) {
                    preco = 4.00;
                } else if (codigo == 2) {
                    preco = 4.50;
                } else if (codigo == 3) {
                    preco = 5.00;
                } else if (codigo == 4) {
                    preco = 2.00;
                } else if (codigo == 5) {
                    preco = 1.50;
                } else {
                    System.out.println("Código inválido");
                }
                total = preco * quantidade;
                System.out.printf("Total a pagar: R$ %.2f\n", total);

                sc.close();
            }
        }

