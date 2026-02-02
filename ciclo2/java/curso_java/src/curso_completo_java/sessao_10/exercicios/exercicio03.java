package curso_completo_java.sessao_10.exercicios;

/* Fazer um programa para ler nome, idade e altura de N pessoas, conforme exemplo. Depois, mostrar na
tela a altura média das pessoas, e mostrar também a porcentagem de pessoas com menos de 16 anos,
bem como os nomes dessas pessoas caso houver. */


import java.util.Locale;
import java.util.Scanner;

public class exercicio03 {

    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        double somaAlturas = 0;
        int contMenor16 = 0;
        String nomesMenor16 = "";


        System.out.println("Quantas pessoas deseja cadastra?: ");
        int quantPessoas = sc.nextInt();



        String[] nomes = new String[quantPessoas];
        int[] idades = new int[quantPessoas];
        double[] alturas = new double[quantPessoas];

        for (int i=0; i<quantPessoas; i++ ) {
            System.out.println("Digite o nome: \n");
            nomes[i] = sc.next();

            System.out.println("Digite a idade: \n");
            idades[i] = sc.nextInt();

            System.out.println("Digite a altura: ");
            alturas[i] = sc.nextDouble();
        }

        for (int i=0; i<quantPessoas; i++ ) {
            somaAlturas += alturas[i];
            if (idades[i] <= 16) {
                contMenor16 ++;
                nomesMenor16 += " " + nomes[i];
            }

        }

        System.out.println("Altura média: %.2f" + (somaAlturas / quantPessoas) + "\n");
        System.out.println("Porcentagem de pessoas com menos de 16 anos: " + ((100.0 * contMenor16) / quantPessoas) + "%");
        System.out.println();



    }


}
