package secao7_introOrientacaoaObjetos.exercicios.exercicio2;

import java.util.Scanner;

public class exercicio2 {
    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);
        metodos2 metTwo = new metodos2();

        System.out.print("Nome: ");
        metTwo.nome = sc.next();
        System.out.print("Salário bruto: ");
        metTwo.salarioBruto = sc.nextDouble();
        System.out.print("Taxa: ");
        metTwo.taxa = sc.nextDouble();

        System.out.println("Employee: " + metTwo);

        System.out.print("Which percentage to increase salary? ");
        double porcentagem = sc.nextDouble();
        metTwo.AumentoSalario(porcentagem);
        System.out.print("Updated data: " + metTwo);
    }

}
