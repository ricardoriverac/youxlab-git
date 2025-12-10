package application;

import java.util.Locale;
import java.util.Scanner;

public class a96_ex10 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("Caro usuário, quantas pessoas serão cadastradas? ");
        int quantidadePessoas = sc.nextInt();
        double[] altura = new double[quantidadePessoas];
        char[] genero = new char[quantidadePessoas];
        int countHomens = 0;
        int countMulheres = 0;
        for (int i = 0; i < quantidadePessoas; i++) {
            System.out.printf("Caro usuário, qual a altura da %da pessoa? ", i+1);
            altura[i] = sc.nextDouble();
            System.out.printf("Caro usuário, qual o gênero da %da pessoa  ? ", i+1);
            char gen = sc.next().charAt(0);
            if (gen == 'F'){
                genero[i] = 'F';
                countMulheres ++;
            }
            else{
                genero[i] = 'M';
                countHomens ++;
            }
        }
        double menor = 999.90;
        System.out.print("Menor altura: ");
        for (int i = 0; i < quantidadePessoas; i++) {
            if (menor > altura[i]) {
                menor = altura[i];
            }
        }
            System.out.print(menor);
            double maior = 0.0;
            System.out.print("\n Maior altura: ");
            for (int j = 0; j <quantidadePessoas ; j++) {
                if(altura[j] > maior){
                    maior = altura[j];
                }
            }
            System.out.print(maior);
            double soma = 0.0;
            System.out.print("\n Média das alturas das mulheres: ");
            for (int j = 0; j < quantidadePessoas; j++) {
                if(genero[j] == 'F'){
                    soma+= altura[j];
                }
            }
            System.out.printf("%.2f", soma/countMulheres);
            System.out.printf("\nNúmero de Homens: %d", countHomens);

        }

    }

