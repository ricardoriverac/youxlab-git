package curso_completo_java.sessao_14.pratica;

// AULA 152- Bloco finally

import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class exemplo_pratica02 {

    public static void main(String[] args) {
        File file = new File("C:\\temp\\in.txt");
        Scanner sc = null;
        try {
            sc = new Scanner(file);
            while (sc.hasNextLine()) {
                System.out.println(sc.nextLine());
            }
        }
        catch (IOException e) {
            System.out.println("Error opening file: " + e.getMessage());
        }
        finally {
            if (sc != null) {
                sc.close();
            }
        }
    }
}
