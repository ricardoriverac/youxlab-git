package application;

import application.entities.Estudantes;

import java.util.Locale;
import java.util.Scanner;

public class a_75_ex3 {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        Estudantes estudante;

        estudante = new Estudantes();

        System.out.print("Caro usuário, insira o nome do estudante: ");
        estudante.nome = sc.nextLine();
        System.out.print("Caro usuário, insira a nota do primeiro trimestre do estudante [de 0 a 30]: ");
        estudante.nota1 = sc.nextDouble();
        if (estudante.nota1 < 0 | estudante.nota1 > 30){
            while (estudante.nota1 < 0 | estudante.nota1 > 30){
                System.out.print("Caro usuário, insira uma nota válida para o primeiro trimestre [Maior que zero e menor ou igual a 30]: ");
                estudante.nota1 = sc.nextDouble();
            }
        }
        System.out.print("Caro usuário, insira a nota do segundo trimestre [de 0 a 35]: ");
        estudante.nota2 = sc.nextDouble();
        if(estudante.nota2 < 0 | estudante.nota2 > 35) {
            while (estudante.nota2 < 0 | estudante.nota2 > 35) {
                System.out.print("Caro usuário, insira uma nota válida para o segundo trimestre [maior que zero e menor ou igual a 35]: ");
                estudante.nota2 = sc.nextDouble();
            }
        }
        System.out.print("Caro usuário, insira a nota do terceiro trimestre [de 0 a 35]: ");
        estudante.nota3 = sc.nextDouble();
        if(estudante.nota3 < 0 | estudante.nota3 > 35){
            while (estudante.nota3 < 0 | estudante.nota3 > 35){
                System.out.print("Caro usuário, insira uma nota válida para o terceiro trimestre [maior que zero e menor ou igual a 35]: ");
                estudante.nota3 = sc.nextDouble();
            }
        }
        System.out.println("Nota final: " + estudante.notaFinal());
        if (estudante.notaFinal() < 60){
            System.out.println("FINAL GRADE = " + estudante.notaFinal());
            System.out.println("FAILED\n" + "MISSING " + estudante.missing());
        }
        else{
            System.out.println("FINAL GRADE = " + estudante.notaFinal());
            System.out.println("PASS");
        }
    }
}
