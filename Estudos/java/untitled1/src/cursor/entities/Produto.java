package cursor.entities;

public class Produto{
    public String nome;
    public double preco;
    public int quantidade;

    public double estoque(){
        return preco * quantidade;
    }
    public void adicionarEstoque(int quantidade){
       this.quantidade += quantidade;
    }
    public void removerEstoque (int quantidade){
        this.quantidade -= quantidade;
    }
    public String toString(){
        return  nome + ", $ " + preco + ", " + quantidade + " units" + " Total: $ " + estoque();
    };
}
