package Aula_97.Vetores.Exercicio_pensionato;

public class Classe {

    private String nome;
    private String gmail;
    private int numeroquarto;

    public Classe(int numeroQuarto, String nome, String gmail) {
        this.nome = nome;
        this.gmail = gmail;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getGmail() {
        return gmail;
    }

    public void setGmail(String gmail) {
        this.gmail = gmail;
    }

    public int getNumeroquarto() {
        return numeroquarto;
    }

    public void setNumeroquarto(int numeroquarto) {
        this.numeroquarto = numeroquarto;
    }
}
