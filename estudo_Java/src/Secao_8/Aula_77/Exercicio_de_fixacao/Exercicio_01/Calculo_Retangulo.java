package Aula_77.Exercicio_de_fixacao.Exercicio_01;

public class Calculo_Retangulo {

    public double altura;
    public double largura;

    public double area() {
        return altura * largura;

    }

    public double perimetro() {
        double area = altura * largura;
        double comprimento =  area / largura;
        return 2 * (comprimento + largura);

    }

    public double diagonal() {
        return Math.sqrt(Math.pow(altura, 2) + Math.pow(largura, 2));

    }


}