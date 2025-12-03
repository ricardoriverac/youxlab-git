package application.entities;

public class Funcionarios {
    public String nome;
    public double salarioBruto, imposto;

    public double salarioLiquido(){
        return salarioBruto - imposto;
    }
    public void aumentarSalario(double porcentagem){
        salarioBruto += salarioBruto * porcentagem / 100.0;
    }
    public String toString(){
        return nome + ", " + "$ " + salarioLiquido();
    }


}
