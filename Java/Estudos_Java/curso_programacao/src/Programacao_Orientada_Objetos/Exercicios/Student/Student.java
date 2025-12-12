package Programacao_Orientada_Objetos.Exercicios.Student;

public class Student {
    public String name;
    public double nota1;
    public double nota2;
    public double nota3;

    public double boletim(double finalGrade) {
        if ((nota1 + nota2 + nota3) < 60) {
            finalGrade = 60 - nota1 - nota2 - nota3;
        }
        return finalGrade;
    }

}
