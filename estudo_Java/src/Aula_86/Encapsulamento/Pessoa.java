package Aula_86.Encapsulamento;

public class Pessoa {

    private String nome;
    private int idade;

    // Retorna o valor
    public String getName() {
        return nome;
    }

    // Modifica o valor
    public void setName(String name) {
        this.nome = name;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade( int idade) {
        if (idade < 0) {
            System.out.println("Idade inválida!");
        }
        else this.idade = idade;
    }
}
