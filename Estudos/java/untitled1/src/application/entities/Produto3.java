package application.entities;

public class Produto3 {

        private String nome;
        private double preco;
        private int quantidade;

        public Produto3(){

        }

        public Produto3(String nome, double preco, int quantidade){
            this.nome = nome;
            this.preco = preco;
            this.quantidade = quantidade;
        }
        public Produto3(String nome, double preco){
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
        public void setName(String nome){
            this.nome = nome;
        }
        public String getName(){
            return nome;
        }
        public double getPreco(){
            return preco;
        }
        public void setPreco(double preco){
            this.preco = preco;
        }
    }
