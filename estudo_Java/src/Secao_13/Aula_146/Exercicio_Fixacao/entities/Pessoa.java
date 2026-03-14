package Secao_13.Aula_146.Exercicio_Fixacao.entities;

public abstract class Pessoa {

    private Double rendaAnual;
    private String nome;

    public Pessoa() {}

    public Pessoa(Double rendaAnual, String nome) {
        this.rendaAnual = rendaAnual;
        this.nome = nome;
    }

    public Double getRendaAnual() {
        return rendaAnual;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void exibirDados() {
        System.out.print("\n" + getNome());
        System.out.print(": $ ");
        System.out.print(String.format("%.2f", calculoImposto()));
    }

    abstract double calculoImposto();

    public Double getCalculoImposto() {
        return  calculoImposto();
    }


}
