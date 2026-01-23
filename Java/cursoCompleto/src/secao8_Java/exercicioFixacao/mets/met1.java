package secao8_Java.exercicioFixacao.mets;

public class met1 {
    //declarando atributos
    private String nome;
    private int numConta;
    private double saldo;


    //adicionando constructor
    public met1(String nome, int numConta, double depInicial) {
        this.nome = nome;
        this.numConta = numConta;
        deposito(depInicial);
    }
    public met1(String nome, int numConta) {
        this.nome = nome;
        this.numConta = numConta;
    }
    public int getNumConta (int numConta) {
        return numConta;
    }
    public String getNome(String nome){
        return nome;
    }
    public void setNome(String nome){
        this.nome = nome;
    }
    public void deposito(double quantidade) {
        saldo += quantidade;
    }
    public void sacar(double quantidade) {
        saldo -= quantidade + 5;
    }
    public String toString(){
        return "Dados da conta: \n" + "Número da conta: "
                + numConta + "\nUsuário: "
                + nome +
                "\nSaldo: "
                + String.format("%.2f", saldo);


    }


}
