package application;

import java.io.File;
import java.util.Scanner;

public class a_166 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Caro usuário, insira o caminho do arquivo: ");
        String strCaminho = sc.nextLine();

        File caminho = new File(strCaminho);

        System.out.println("Get path: " + caminho.getPath());
        System.out.println("GetParent " + caminho.getParent());
        System.out.println("GetName " + caminho.getName());


    }
}
