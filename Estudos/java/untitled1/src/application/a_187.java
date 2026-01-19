package application;


import application.entities.Produto;
import application.entities.ServicoCalculo;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class a_187 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);

        List<Produto> list = new ArrayList<>();

        String caminho = "/home/youx/in.txt";
        try (BufferedReader br = new BufferedReader(new FileReader(caminho))){
            String line = br.readLine();

            while (line != null){
                String[] fields = line.split(",");
                list.add(new Produto(fields[0], Double.parseDouble(fields[1])));
                line = br.readLine();
            }
            Produto x = ServicoCalculo.max(list);
            System.out.println("Maior valor: ");
            System.out.println(x);
        } catch (IOException e){
            System.out.println("Erro" + e.getMessage());
        }

    }
}
