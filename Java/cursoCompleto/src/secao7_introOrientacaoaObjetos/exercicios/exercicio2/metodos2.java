package secao7_introOrientacaoaObjetos.exercicios.exercicio2;

public class metodos2 {
    public String nome;
    public double salarioBruto;
    public double taxa;

    public double salarioLiquido() {
        return salarioBruto - taxa;
    }
    public void AumentoSalario(double porcentagem) {
       salarioBruto += salarioBruto * (porcentagem/100);
    }
    public String toString(){
        return nome + ", " + String.format("%.2f", salarioLiquido());

    }
}
