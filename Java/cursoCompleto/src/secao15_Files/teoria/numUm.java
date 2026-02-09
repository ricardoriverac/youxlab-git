package secao15_Files.teoria;

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class numUm {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a folder path: ");
        String strPath = "/home/youx/youxlab-git/Java/cursoCompleto/src/secao15_Files/teoria";
        File path = new File(strPath);
        File[] folders = path.listFiles(File::isDirectory);
        System.out.println("FOLDERS:");
        for (File folder : folders) {
            System.out.println(folder);
        }
        File[] files = path.listFiles(File::isFile);
        System.out.println("FILES:");
        for (File file : files) {
            System.out.println(file);
        }
        boolean success = new File(strPath + "\subdir").mkdir();
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(path) )){
            File file = new File(strPath);
            String line = sc.nextLine();
            bw.write(line);
            bw.newLine();


        }
        catch(IOException e){
            System.out.println(e.getMessage() + "\n" + e.getCause());
        }
        System.out.println("Directory created successfully: " + success);
        sc.close();
    }


}
