package Aula_74;

import java.util.Locale;
import java.util.Scanner;

public class CodigoProduto {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        ClasseProduto prd = new ClasseProduto();

        System.out.println("Inserir dados do produto: ");
        System.out.print("Nome: ");
        prd.name = sc.nextLine();
        System.out.print("Produto: ");
        prd.price = sc.nextDouble();
        System.out.print("Quantidade em estoque: ");
        prd.quantity = sc.nextInt();

        System.out.println(prd.name + ", " + prd.price + ", " + prd.quantity);



    }
}