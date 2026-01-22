package application;

import application.entities.Produto;

public class a_201_teoria4 {
    public static int compareProdutos(Produto p1, Produto p2){
        return  p1.getPreco().compareTo(p2.getPreco());
    }
    public static void main(String[] args) {
        //(...)
        //list.sort(a_201_teoria4:compareProdutos());

        //list.sort((p1, p2) -> p1.getPreco.compareTo(p2.getPreco()));
    }
}
