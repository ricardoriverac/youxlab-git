package application;

import java.io.File;
import java.util.Scanner;

public class a_165 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("Insira o caminho do arquivo: ");
        String strCaminho = sc.next();

        File caminho = new File(strCaminho);

        File[] folders = caminho.listFiles(File::isDirectory);
        System.out.println("Arquivos: ");
        for(File folder : folders){
            System.out.println(folder);
        }

        File[] files = caminho.listFiles(File::isFile);
        System.out.println("Files: ");
        for (File file : files){
            System.out.println(file);
        }

        boolean sucess = new File(strCaminho + "//pastateste").mkdir();
        System.out.println("DIretório criado com sucesso" + sucess);
        sc.close();
    }
}
