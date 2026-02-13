package Secao8.Aula77_ex3;

public class estudante {

    public String name;
    public double nota1;
    public double nota2;
    public double nota3;

    public double notafinal() {
        return nota1 + nota2 + nota3;
    }

    public double Pontosfalta() {
        if (notafinal() < 60.0) {
            return 60.0 - notafinal();
        } else {
            return 0.0;
        }
    }
}
