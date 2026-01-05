package application.entities;

import java.util.ArrayList;
import java.util.Calendar;
import java.util.List;

public class Trabalhador {
    private String nome;
    private NivelExperiencia nivel;
    private Double salarioBase;
    private List<ContratoHora> contratos = new ArrayList<>();

    public Trabalhador(String nome, NivelExperiencia nivel, Double salarioBase){
        this.nome = nome;
        this.nivel = nivel;
        this.salarioBase = salarioBase;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public NivelExperiencia getNivel() {
        return nivel;
    }

    public void setNivel(NivelExperiencia nivel) {
        this.nivel = nivel;
    }

    public Double getSalarioBase() {
        return salarioBase;
    }

    public void setSalarioBase(Double salarioBase) {
        this.salarioBase = salarioBase;
    }

    public List<ContratoHora> getContratos() {
        return contratos;
    }

    public  void addContract(ContratoHora contrato){
        contratos.add(contrato);
    }
    public void removeContract(ContratoHora contrato){
        contratos.remove(contrato);
    }

    public Double renda(int ano, int mes) {
        double soma = salarioBase;
        Calendar cal = Calendar.getInstance();
        for (ContratoHora c : contratos) {
            cal.setTime(c.getDate());
            int c_ano = cal.get(Calendar.YEAR);
            int c_mes = 1 + cal.get(Calendar.MONTH);
            if (ano == c_ano && mes == c_mes) {
                soma += c.ValorTotal();
            }
        }
        return soma;

    }
}
