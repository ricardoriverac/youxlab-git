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
        System.out.printf("Product data: %s, $ %.2f, %d units", x.nome, x.preco, x.quantidade);

        System.out.print("Caro usuário, quantas unidades você deseja adicionar ao estoque? ");
    }
}
