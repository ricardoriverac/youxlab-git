package Secao_15.Aula_165.FileWriter_e_BufferedWriter.applications;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {


        String[] lines = new String[] { "\nGood morning", "Good afternoon", "Good night"};

        String path = "src/Secao_15/Aula_165/FileWriter_e_BufferedWriter/file/in.txt";

        try (BufferedWriter bw = new BufferedWriter(new FileWriter(path, true))) {
            for (String line : lines) {
                bw.write(line);
                bw.newLine();
            }
        }
        catch (IOException e) {
            e.printStackTrace();
        }
    }
}
