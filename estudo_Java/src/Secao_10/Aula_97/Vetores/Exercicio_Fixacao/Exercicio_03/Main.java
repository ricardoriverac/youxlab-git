package Aula_97.Vetores.Exercicio_Fixacao.Exercicio_03;

import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("Quantas pessoas serao digitadas? ");
        int n = sc.nextInt();


        String nome;
        int idade;
        double altura;
        int c = 0;
        double soma = 0;
        double media = 0;
        double pessoasComMenos16Anos = 0;

        Exercicio_03[] vect = new Exercicio_03[n];

        for (int i=0; i<n; i++) {
            c++;

            System.out.printf("%nDados da %d° pessoa: %n", c);

            System.out.print("Nome: ");
            nome = sc.next();

            System.out.print("Idade: ");
            idade = sc.nextInt();

            System.out.print("Altura: ");
            altura = sc.nextDouble();

            vect[i] = new Exercicio_03(nome, idade, altura);

            soma += vect[i].getAltura();

            if (vect[i].getIdade() < 16) {
                pessoasComMenos16Anos++;

            }

        }

        media = soma / n;
        System.out.printf("Altura media: %.2f", media);

        double porcentagem = pessoasComMenos16Anos * 100 / n;
        System.out.printf("%nPessoas com menos de 16 anos: %.1f%%%n", porcentagem);


        for (int i = 0; i < n; i++) {
            if (vect[i].getIdade() < 16) {
                System.out.println(vect[i].getNome());
            }
        }
    }
}
