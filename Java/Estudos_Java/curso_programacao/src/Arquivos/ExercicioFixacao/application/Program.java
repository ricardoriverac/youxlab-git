package Arquivos.ExercicioFixacao.application;

import Arquivos.ExercicioFixacao.entities.Products;
import herancaPolimorfismo.Exercicios.ExerciciosFixacao.exer01.entities.Product;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class Program {

    static void main() {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter quantity products: ");
        int quantityProducts = sc.nextInt();

        List<Products> productsList = new ArrayList<>();
        try (BufferedWriter bw = new BufferedWriter(new FileWriter("/home/youx/exercicio_CSV/out/summary.csv", true))) {
            for (int i = 0; i < quantityProducts; i++) {
                System.out.println("Enter product #" + (i + 1) + " data: ");
                System.out.print("Name: ");
                sc.nextLine();
                String nameProduct = sc.nextLine();
                System.out.print("Price: R$");
                double price = sc.nextDouble();
                System.out.print("Quantity: ");
                int quantity = sc.nextInt();

                productsList.add(new Products(nameProduct, price, quantity));

                for (Products product : productsList){
                    bw.write(product.getName() + ", " + product.total());
                    bw.newLine();
                }
            }
        }
        catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }

        sc.close();

    }

}
