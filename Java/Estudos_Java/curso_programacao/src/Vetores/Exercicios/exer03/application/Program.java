package Vetores.Exercicios.exer03.application;

import Vetores.Exercicios.exer03.entities.Person;

import java.util.Locale;
import java.util.Scanner;

public class Program {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);


        System.out.print("Quantas pessoas serão digitadas? ");
        int qntPessoas = sc.nextInt();
        Person[] pessoas = new Person[qntPessoas];
        Person pessoaAtual = new Person();


        for (int i=0; i<qntPessoas; i++) {
            System.out.println("Digite a " + (i+1) +"a pessoa: ");
            System.out.print("Nome: ");
            pessoaAtual.setName(sc.next());

            System.out.print("Idade:");
            pessoaAtual.setIdade(sc.nextInt());

            System.out.print("Altura: ");
            pessoaAtual.setAltura(sc.nextDouble());

            pessoas[i] = pessoaAtual;
            pessoaAtual = new Person();
        }


        int countMenor16 = 0;
        String nomeMenor16 = "";
        double somaAltura = 0;

        for (int i = 0; i < qntPessoas; i++) {
            if (pessoas[i].getIdade() < 16) {
                countMenor16++;
                nomeMenor16 += " " + pessoas[i].getName();
            }
            somaAltura += pessoas[i].getAltura();
        }

        System.out.println();
        System.out.println("Altura média: " + (somaAltura / qntPessoas));
        System.out.println("Pessoas com menos de 16 anos: " + ((100.0 * countMenor16) / qntPessoas) + "%");
        System.out.print("Nomes com idade menos de 16 anos: " + nomeMenor16);

        sc.close();
    }
}
