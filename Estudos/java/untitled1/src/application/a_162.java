package application;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class a_162 {
    public static void main(String[] args) {
        String caminho = "/home/youx/in.txt";
        try (BufferedReader br = new BufferedReader(new FileReader(caminho))){


            String line = br.readLine();

            while(line != null){
                System.out.println(line);
                 line = br.readLine();
            }
        }
        catch (IOException e){
            System.out.print("Erro: " + e.getMessage());
        }
    }
}
