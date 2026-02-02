package curso_completo_java.sessao_15.pratica;

// AULA 165 - Manipulando pastas com File

import java.io.File;
import java.util.Scanner;

public class exemplo_pratica05 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("Enter a folder path: ");
        String strPath = sc.nextLine();

        File path = new File(strPath);

        File[] folders = path.listFiles(File::isDirectory);
        System.out.println("\n »»» FOLDERS ««« \n");
        for (File folder : folders) {
            System.out.println(folder);
        }

        File[] files = path.listFiles(File::isFile);
        System.out.println("\n »»» FILES ««« \n");
        for (File file : files) {
            System.out.println(file);
        }

        boolean success = new File(strPath + "//subdir").mkdir();
        System.out.println("Directory created sucessfuly: " + success);

        sc.close();
    }
}
