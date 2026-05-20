package Arquivos.informacoesCaminhoArquivo;

import java.io.File;
import java.util.Scanner;

public class Program {

    static void main() {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a file path: ");
        String strPath = sc.nextLine();

        File path = new File(strPath);

        System.out.println("getName: " + path.getName()); // só nome do arquivo

        System.out.println("getParent: " + path.getParent()); // só caminho do arquivo

        System.out.println("getPath: " + path.getPath()); // nome e caminho do arquivo



        sc.close();
    }
}
