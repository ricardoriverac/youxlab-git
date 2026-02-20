package Aula_105.Listas.Exercicio_Fixacao;

public class Dados {

    private int id;
    private String nome;
    private double credito;

    public Dados(int id, String nome, double credito) {
        this.id = id;
        this.nome = nome;
        this.credito = credito;
    }

    public int getId() {
        return id;
    }

    public String getNome() {
        return nome;
    }

    public double getCredito() {
        return credito;
    }

    public void setCredito(double credito) {
        this.credito = credito;
    }
}
