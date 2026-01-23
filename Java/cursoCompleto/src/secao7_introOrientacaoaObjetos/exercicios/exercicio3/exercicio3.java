package secao7_introOrientacaoaObjetos.exercicios.exercicio3;

import java.util.Scanner;

public class exercicio3 {
    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);
        metodos3 metTres = new metodos3();
        String nome;
        System.out.println("Insira o nome do aluno: ");
        nome = metTres.nome = sc.next();
        System.out.println("Insira as notas de " + nome);
        metTres.adicionandoNotas();

        System.out.println("<<<SITUAÇÃO FINAL>>>");
        metTres.aproveitamento();
        sc.close();
    }
}
