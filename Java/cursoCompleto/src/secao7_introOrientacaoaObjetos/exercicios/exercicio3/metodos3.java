package secao7_introOrientacaoaObjetos.exercicios.exercicio3;

import java.util.Scanner;

public class metodos3 {
    Scanner sc = new Scanner(System.in);
    public String nome;
    public double notaDif, notaFinal, nota;

    public double adicionandoNotas() {
        for (int i = 0; i < 3; i++){
            nota = sc.nextDouble();
            notaFinal += nota;
        }
        return notaFinal;
    }

    public double aproveitamento() {
        System.out.println("NOTA FINAL = " + notaFinal);
        notaDif = 60 - notaFinal;
        if (notaFinal < 60) {
            System.out.println("REPROVADO\nFALTANDO " + notaDif + " PONTOS");
        }
        else {
            System.out.println("APROVADO");
        }
        return notaDif;
    }
}