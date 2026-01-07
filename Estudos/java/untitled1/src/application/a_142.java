package application;

import application.entities.Produto;
import application.entities.ProdutoImportado;
import application.entities.ProdutoUsado;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class a_142 {
    public static void main(String[] args) {
       Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        List<Produto> produtos = new ArrayList<>();

        System.out.print("Caro usuário, por favor insira quantos produtos serão cadastrados: ");
        int quantidadeProdutos = sc.nextInt();
        for (int i = 0; i < quantidadeProdutos; i++) {
            System.out.print("Caro usuário, seu produto é comum, importado ou usado? [c/i/u]");
            char tipoProduto = sc.next().charAt(0);
            System.out.print("Caro usuário, por favor informe o nome do produto: ");
            String nomeProduto = sc.next();
            System.out.print("Caro usuário, por favor informe o preço do produto: ");
            Double precoProduto = sc.nextDouble();
            if(tipoProduto == 'c'){
                produtos.add(new Produto(nomeProduto, precoProduto));

            } else if (tipoProduto == 'i') {
                System.out.print("Caro usuário, por favor informe o valor da taxa alfandegária do produto: ");
                Double taxaAlfandegaria = sc.nextDouble();
                produtos.add(new ProdutoImportado(nomeProduto, precoProduto, taxaAlfandegaria));
            }
            else {
                System.out.print("Caro usuário, por favor informe a data de fabricação do produto: [dd/MM/yyyy]");
                String data = sc.next();
                LocalDate dataFabricacao = LocalDate.parse(data, DateTimeFormatter.ofPattern("dd/MM/yyyy"));
                produtos.add(new ProdutoUsado(nomeProduto, precoProduto, dataFabricacao));
            }
        }
        System.out.print("Produtos: ");
        for (Produto p : produtos){
            System.out.println(p.etiquetaPreco());
        }
    }
}
