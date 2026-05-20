package Arquivos.FileE_BufferedWriter;

import java.io.*;

public class Program {

    static void main() {

        String[] lines = new String[] {"Good morning", "Good afternoon", "Good night"};

        String path = "//home//youx//Projetos//out.txt";

        // try (BufferedWriter bw = new BufferedWriter(new FileWriter(path)))

        try (BufferedWriter bw = new BufferedWriter(new FileWriter(path, true))){

            for (String line : lines){
                bw.write(line);
                bw.newLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
