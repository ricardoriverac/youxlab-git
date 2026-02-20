package Aula_77.Exercicio_de_fixacao.Exercicio_03;

public class Class_notaAluno {

    public double nota1;
    public double nota2;
    public double nota3;

    public double somatorioNotas() {
        return nota1 + nota2 + nota3;
    }
    public String verificador() {

        if(somatorioNotas() > 60) {
            return String.format("%nPassou");
        }
        else {
            return String.format("%nNão passou");
        }
        }
    }

