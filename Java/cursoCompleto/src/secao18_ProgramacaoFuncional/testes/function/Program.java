package secao18_ProgramacaoFuncional.testes.function;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Function;
import java.util.stream.Collectors;

public class Program {
    public static void main(String[] args) {
        List<Product> p = new ArrayList<>();
        p.add(new Product("Camiseta", 50.00));
        p.add(new Product("Bermuda", 20.00));

        Function<Product, String> func = pr -> pr.getNome().toUpperCase();
        List<String> names = p.stream().map(func).collect(Collectors.toList());
        //List<String> names = p.stream().map(new UpperCaseName()).collect(Collectors.toList());
        //versão sem lambda
        names.forEach(System.out::println);
    }
}
