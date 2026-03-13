package Secao_13.Aula_144.Classes_Abstratas.entities;

public class Desenvolvedor extends Funcionario{

    private Integer horasExtras;
    private Double valorHoraExtra;

    public Desenvolvedor() {
        super();
    }

    public Desenvolvedor(String nome, Double salarioBase, Integer horasExtras, Double valorHoraExtra) {
        super(nome, salarioBase);
        this.horasExtras = horasExtras;
        this.valorHoraExtra = valorHoraExtra;
    }

    public Integer getHorasExtras() {
        return horasExtras;
    }

    public void setHorasExtras(Integer horasExtras) {
        this.horasExtras = horasExtras;
    }

    public Double getValorHoraExtra() {
        return valorHoraExtra;
    }

    public void setValorHoraExtra(Double valorHoraExtra) {
        this.valorHoraExtra = valorHoraExtra;
    }

    @Override
    double calcularSalario() {
        return super.salarioBase + (horasExtras * valorHoraExtra);
    }
}
