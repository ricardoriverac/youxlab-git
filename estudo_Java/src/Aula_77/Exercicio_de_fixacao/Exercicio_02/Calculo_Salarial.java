package Aula_77.Exercicio_de_fixacao.Exercicio_02;

public class Calculo_Salarial {

    public  String nome;
    public double salarioBruto;
    public double imposto;

    public double salarioLiqido() {
        return salarioBruto - imposto;

    }

    public void AumentarSalario(double porcentagem) {
        this.salarioBruto = this.salarioBruto * (1+ porcentagem/100);
    }

    public String toString() {
        return "Employee: "
                + nome
                + ", $ "
                + String.format("%.2f", salarioLiqido());
    }

}
