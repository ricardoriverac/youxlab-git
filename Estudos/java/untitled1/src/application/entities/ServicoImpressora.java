package application.entities;

import java.util.ArrayList;
import java.util.List;

public class ServicoImpressora<T> {
    private List<T> list = new ArrayList<>();

    public void addValor(T valor){
        list.add(valor);
    }

    public T primeiro(){
        if(list.isEmpty()){
            throw new IllegalStateException("Lista está vazia");
        }
        return list.get(0);
    }

    public void imprimir(){
        System.out.print("[");
        if(!list.isEmpty()){
            System.out.println(list.get(0));
        }

        for (int i = 0; i < list.size(); i++) {
            System.out.print(", " + list.get(i));
        }
        System.out.println("]");
    }
}
