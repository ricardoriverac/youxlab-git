package Secao_15.Aula_162.Lendo_arquivo_texto_com_classes_File_e_Scanner.application;

import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        File file = new File("/home/youx/youxlab-git/estudo_Java/src/Secao_15/Aula_162/Lendo_arquivo_texto_com_classes_File_e_Scanner/file/in.txt");
        Scanner sc = null;

        try {
            sc = new Scanner(file);
            while (sc.hasNextLine()) {
                System.out.println(sc.nextLine());
            }
        }
        catch (IOException e) {
            System.out.println("Erro: " + e.getMessage());
        }
        finally {
            if (sc != null) {
                sc.close();
            }
        }
    }
}
