package secao15_Files.teoria;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class num2 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String [] line = new String[n];
        for (int i = 0; i < n; i++){
            line[i] = sc.nextLine();
        }
        String strPath = "/home/youx/youxlab-git/Java/cursoCompleto/src/secao15_Files/in2.csv";
        File path = new File(strPath);
        try(BufferedWriter bw = new BufferedWriter(new FileWriter(path, true))){
            for (String l : line){
                bw.write(l);
                bw.newLine();
            }
        }
        catch(IOException e){

        }
        sc.close();

    }

}
