package application;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class a_164 {
    public static void main(String[] args) {

        String [] lines = new String[] {"Good Morning", "Good afternoon", "Good night", "Good evening"};
        String caminho = "/home/youx/out.txt";

        try (BufferedWriter br = new BufferedWriter(new FileWriter(caminho, true))){
            for(String l: lines ){
                br.write(l);
                br.newLine();
            }
        } catch (IOException e) {
            System.out.print("Erro: " + e.getMessage());
        }
    }
}
