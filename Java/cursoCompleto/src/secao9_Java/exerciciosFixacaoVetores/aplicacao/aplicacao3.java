package secao9_Java.exerciciosFixacaoVetores.aplicacao;

import java.util.Locale;
import java.util.Scanner;

public class aplicacao3 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        double porcentagemIdade, somaMenor, somaAltura, mediaAltura;
        System.out.print("QUantas pessoas serão digitadas?");
        int n = sc.nextInt();
        String[] nomes = new String[n];
        int[] idade = new int[n];
        double[] altura = new double[n];
        int count = 0;
        for (int i = 0 ; i < n ; i ++) {
            System.out.printf("Digite os dados da %da pessoa:\n", i + 1);
            System.out.print("Nome: ");
            nomes[i] = sc.next();
            System.out.print("\nIdade: ");
            idade[i] = sc.nextInt();
            System.out.print("\nAltura: ");
            altura[i] = sc.nextDouble();
        }
        somaAltura = 0;
        for (int i = 0; i < altura.length; i++) {
            somaAltura += altura[i];
        }
        mediaAltura = somaAltura/altura.length;
        System.out.println("Média da altura: " + mediaAltura);
        somaMenor = 0;
        System.out.println("Pessoas com menos de 16 anos: ");
        for (int i = 0; i < idade.length ; i++) {
            if (idade[i] < 16) {
                somaMenor += 1;
                System.out.println(nomes[i]);
            }
        }
        porcentagemIdade = somaMenor/idade.length * 100;
        System.out.print("Porcentagem de pessoas com menos de 16 anos: %d %" + porcentagemIdade);
        sc.close();
    }
}
