package curso_completo_java.sessao_15.pratica;

import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class exemplo_pratica01 {

    public static void main(String[] args) {

        File file = new File("/home/youx/in.txt");
        Scanner sc = null;

        try {
            sc = new Scanner(file);
            while (sc.hasNextLine()) {
                System.out.println(sc.nextLine());
            }

        } catch (IOException e) {
            System.out.println("Erro: " + e.getMessage());
        } finally {
            if (sc != null) {
                sc.close();
            }
        }

    }
}