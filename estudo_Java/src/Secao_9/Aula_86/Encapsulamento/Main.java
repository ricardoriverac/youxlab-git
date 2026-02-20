package Aula_86.Encapsulamento;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        Pessoa pss = new Pessoa();

        int valor;
        valor = sc.nextInt();

        pss.setIdade(valor);
        System.out.println("Digite a sua idade: " + pss.getIdade());
    }
}
