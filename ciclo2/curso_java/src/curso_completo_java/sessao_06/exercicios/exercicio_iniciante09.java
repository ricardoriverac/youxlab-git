package curso_completo_java.sessao_06.exercicios;

/* Ler um número inteiro N e calcular todos os seus divisores.*/

import java.util.Scanner;

public class exercicio_iniciante09 {

    public static void main(String[] args) {

            Scanner sc = new Scanner(System.in);


            System.out.println("Digite um número: ");
            int numero = sc.nextInt();

            for (int i=1; i<=numero; i++) {
                if (numero % i == 0) {
                    System.out.println("Seus divisores são:");
                    System.out.println(i);
                }
            }

            sc.close();
        }
    }
