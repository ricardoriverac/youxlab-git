package Secao_15.Exercicio;

import java.io.*;
import java.util.Scanner;

public class Program {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("Enter a file path: ");
        String path = sc.nextLine();

        try (BufferedReader br = new BufferedReader(new FileReader(path))) {
            System.out.println("Arquivo CSV criado com sucesso!");
            String line;
            while ((line = br.readLine()) != null) {
                String[] values = line.split(",");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        sc.close();
    }
}
