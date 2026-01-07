package application.entities;

public class Funcionarios3 {
    private String nomeFuncionario;
    private Integer cargaHoraria;
    private Double valorHora;

    public Funcionarios3() {
    }

    public Funcionarios3(String nomeFuncionario, Integer cargaHoraria, Double valorHora) {
        this.nomeFuncionario = nomeFuncionario;
        this.cargaHoraria = cargaHoraria;
        this.valorHora = valorHora;
    }

    public String getNomeFuncionario() {
        return nomeFuncionario;
    }

    public void setNomeFuncionario(String nomeFuncionario) {
        this.nomeFuncionario = nomeFuncionario;
    }

    public Integer getCargaHoraria() {
        return cargaHoraria;
    }

    public void setCargaHoraria(Integer cargaHoraria) {
        this.cargaHoraria = cargaHoraria;
    }

    public Double getValorHora() {
        return valorHora;
    }

    public void setValorHora(Double valorHora) {
        this.valorHora = valorHora;
    }

    public Double pagamento(){
        return  valorHora * cargaHoraria;

    }


}
