package application.entities;

public class Estudantes {
   public String nome;
    public double nota1, nota2, nota3;

    public double notaFinal(){
        return nota1+ nota2+ nota3;
    }
    public double missing(){
        return 60 - notaFinal();
    }
}
