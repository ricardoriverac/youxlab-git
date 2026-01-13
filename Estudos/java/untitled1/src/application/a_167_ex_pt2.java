package application;

import application.entities.Produto2;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class a_167_ex_pt2 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        List<Produto2> produtos = new ArrayList<>();
        try (BufferedWriter br = new BufferedWriter(new FileWriter("/home/youx/pastaexercicio/out/summary.csv", true))) {


            System.out.print("Caro usuário, quantos produtos serão cadastrados? ");
            int quantidadeProdutos = sc.nextInt();
            for (int i = 0; i < quantidadeProdutos; i++) {
                System.out.print("Caro usuário, qual o nome do produto a ser cadastrado? ");
                String nomeProduto = sc.next();
                System.out.printf("Caro usuário, qual o preço unitário do(a) %s", nomeProduto);
                Double precoUni = sc.nextDouble();
                System.out.print("Caro usuário, quantas unidades em estoque tem? ");
                Integer quantidade = sc.nextInt();
                Produto2 produto = new Produto2(nomeProduto, precoUni, quantidade);
                produtos.add(produto);
            }
            for (Produto2 produto : produtos){
                br.write(produto.getNome() + "," + produto.getPreco() * produto.getQuantidade());
                br.newLine();
            }
        }
        catch (IOException e){
            System.out.println("Erro: " + e.getMessage());
        }
    }
}
