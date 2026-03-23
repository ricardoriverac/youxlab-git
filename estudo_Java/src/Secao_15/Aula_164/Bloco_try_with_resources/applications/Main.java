package Secao_15.Aula_164.Bloco_try_with_resources.applications;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {

        String path = "src/Secao_15/Aula_163/FileReader_e_BufferedReader/file/in.txt";

        try (BufferedReader br = new BufferedReader(new FileReader(path))) {
            String line = br.readLine();

            while (line != null) {
                System.out.println(line);
                line = br.readLine();
            }
        }
        catch (IOException e) {
            System.out.println("Erro" + e.getMessage());
        }
    }
}
