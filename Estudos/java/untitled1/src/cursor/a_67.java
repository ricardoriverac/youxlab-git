package cursor;

import cursor.entities.Produto;

import java.util.Locale;
import java.util.Scanner;

public class a_67 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        Produto x;
        x = new Produto();

        System.out.print("Caro usuário, insira o nome de seu produto: ");
        x.nome = sc.nextLine();
        System.out.print("Caro usuário, insira o preço de seu produto: ");
        x.preco = sc.nextDouble();
        System.out.print("Caro usuário, insira a quantidade em estoque de seu produto: ");
        x.quantidade = sc.nextInt();
        System.out.println("Dados do produto: " + x);

        System.out.print("Caro usuário, quantas unidades você deseja adicionar ao estoque? ");
        int quantidadeAdicionar = sc.nextInt();
        x.adicionarEstoque(quantidadeAdicionar);
        System.out.println("Dados do produto atualizados: " + x);

        System.out.println("Caro usuário, quantas unidades você deseja remover do estoque? ");
        int quantidadeRemover = sc.nextInt();
        x.removerEstoque(quantidadeRemover);
        System.out.println("Dados do produto autalizados: " + x);

        sc.close();
    }
}
