package application.entities;

public class Funcionarios2 {
    private Integer id;
    private String nome;
    private Double salario;

    public Funcionarios2(Integer id, String nome, Double salario){
        this.id = id;
        this.nome = nome;
        this.salario = salario;
    }

    public Integer getId() {
        return id;
    }


    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public Double getSalario() {
        return salario;
    }

    @Override
    public String toString() {
        return "Funcionarios: " + id + ", " + nome + ", " + salario + "\n";
    }

    public void AumentarSalario(double porcentagem){
        salario = salario * (1 + porcentagem / 100);
    }

}
