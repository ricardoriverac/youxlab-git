package application;

import application.entities.Produto;

import java.util.Comparator;

public class a_200_comparator implements Comparator<Produto> {
    @Override
    public int compare(Produto p1, Produto p2){
        return p1.getNome().toUpperCase().compareTo(p2.getNome().toUpperCase());
    }
}
