package application;

import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class a_152 {
    public static void main(String[] args) {
        File file = new File("/home/youx/in.txt");
        Scanner sc = null;
        try {
            sc = new Scanner(file);
            while (sc.hasNextLine()) {
                System.out.print(sc.nextLine());
            }
        }
        catch (IOException e){
            System.out.print("Erro ao abrir o arquivo " + e.getMessage());
        }
        finally {
            if(sc != null){
                sc.close();
            }
            System.out.println("Finally bloco executado");
        }
    }
}
