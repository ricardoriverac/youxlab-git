package secao_10.Aula_96.Exerciciofixa;

import secao_10.Aula_96.Exerciciofixa.EntitiesA97.Person;

import java.util.Locale;
import java.util.Scanner;

public class exercicio02vet {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        System.out.println("Quantas pessoas serao digitadas? ");
        int qtdPessoas = sc.nextInt();

        Person[] pessoas = new Person[qtdPessoas];
        Person pessoaAtual = new Person();

        for (int i = 0; i < qtdPessoas; i++) {

            System.out.println("Dados da "+ (i+1) +"a pessoa: ");
            System.out.print("Nome: ");
            pessoaAtual.setName(sc.next());

            System.out.print("Idade: ");
            pessoaAtual.setAge(sc.nextInt());

            System.out.print("Altura: ");
            pessoaAtual.setHeight(sc.nextDouble());

            pessoas[i] = pessoaAtual;
            pessoaAtual = new Person();

        }

        for (int i = 0; i < qtdPessoas; i++) {

            System.out.println(pessoas[i].toString());


        }


        int soma_idade = 0;
        double soma_altura = 0;
        int countMenor16 = 0;
        String nomesMenor16 = "";


        for (int i = 0; i < qtdPessoas; i++) {

            soma_altura += pessoas[i].getHeight();
            if (pessoas[i].getAge() < 16){
                countMenor16++;
                nomesMenor16 += " " + pessoas[i].getName();
            }

        }

        System.out.println("Média de altura das pessoas: " + (soma_altura / qtdPessoas));
        System.out.println("Porcentagem de pessoas com menos de 16 anos: " + (100.0 * countMenor16 / qtdPessoas) + "%");
        System.out.println("Nome das pessoas menores de 16 anos: " + nomesMenor16);


    }
}
