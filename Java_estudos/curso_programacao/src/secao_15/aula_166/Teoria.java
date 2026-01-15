package secao_15.aula_166;

import java.io.File;
import java.util.Scanner;

public class Teoria {
   static void main() {

        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a folder path: ");
        String strPath = sc.nextLine();
        File path = new File(strPath);

        System.out.println("getPath: " + path.getPath());
        System.out.println("getParent: " + path.getParent());
        System.out.println("getName: " + path.getName());
        sc.close();
    }
}
