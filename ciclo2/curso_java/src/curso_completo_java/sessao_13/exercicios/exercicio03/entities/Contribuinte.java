package curso_completo_java.sessao_13.exercicios.exercicio03.entities;

public abstract class Contribuinte {

    private String nome;
    private Double rendaAnual;

    public Contribuinte(String nome, Double rendaAnual) {
        this.nome = nome;
        this.rendaAnual = rendaAnual;
    }

    public String getNome() {
        return nome;
    }

    public Double getRendaAnual() {
        return rendaAnual;
    }

    public abstract Double imposto();
}
