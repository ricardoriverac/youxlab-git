package application;

import application.entities.Produto;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
import java.util.stream.Collectors;

public class a_209 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        String caminhoArquivo = "/home/youx/in.txt4";

        try(BufferedReader br = new BufferedReader(new FileReader(caminhoArquivo))){
        List<Produto> list = new ArrayList<>();

        String line = br.readLine();
        while (line != null){
            String[] fields = line.split(",");
            list.add(new Produto(fields[0], Double.parseDouble(fields[1])));
            line = br.readLine();
        }

        double avg = list.stream().map(Produto::getPreco).reduce(0.0, Double::sum)/ list.size();

            System.out.println("Preço médio: " + String.format("%.2f", avg));

            Comparator<String> comp = (s1, s2) -> s1.toUpperCase().compareTo(s2.toUpperCase()));
            List<String> nomes = new ArrayList<>();
            for (Produto p : list) {
                if (p.getPreco() < avg) {
                    String nome = p.getNome();
                    nomes.add(nome);
                }
            }
            nomes.sort(comp.reversed());

            nomes.forEach(System.out::println);
        } catch (IOException e){
            System.out.println("Erro: " + e.getMessage());
        }
        sc.close();
    }
}
