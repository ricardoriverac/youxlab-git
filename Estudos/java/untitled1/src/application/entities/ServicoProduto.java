package application.entities;


import java.util.List;
import java.util.function.Predicate;

public class ServicoProduto {
    public double filteredSum(List<Produto> produtos, Predicate<Produto> criterio){
        double soma = 0.0;
        for(Produto p : produtos){
            if(criterio.test(p)){
                soma+= p.getPreco();
            }
        }
        return soma;
    }
}
