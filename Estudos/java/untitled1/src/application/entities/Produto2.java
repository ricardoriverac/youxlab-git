package application.entities;

public class Produto2 {

    public String nome;
    public double preco;
    public int quantidade;

    public Produto2(){

    }

    public Produto2(String nome, double preco, int quantidade){
        this.nome = nome;
        this.preco = preco;
        this.quantidade = quantidade;
    }
    public Produto2(String nome, double preco){
        this.nome= nome;
        this.preco = preco;
    }
    public double estoque(){
        return preco * quantidade;
    }
    public void adicionarEstoque(int quantidade){
        this.quantidade += quantidade;
    }
    public void removerEstoque(int quantidade){
        this.quantidade -= quantidade;
    }
    public String toString(){
            return nome + " ,$" + preco + " ," + quantidade + " units" + " Total: $" + estoque();
    }
}
