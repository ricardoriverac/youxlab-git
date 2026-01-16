package curso_completo_java.sessao_15.pratica;

// AULA 164 - FileWriter e BufferedWriter

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class exemplo_pratica04 {

    public static void main(String[] args) {

        String[] lines = new String[] {"Good morning", "Good afternoon", "Good night"};

        String path = "/home/youx/out.txt";

        try (BufferedWriter bw = new BufferedWriter(new FileWriter(path))) {
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
