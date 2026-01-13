package application;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class a_167_ex_p1 {
    public static void main(String[] args) {
        try(BufferedWriter br = new BufferedWriter(new FileWriter("/home/youx/pastaexercicio/out/summary.csv"))) {
        }
        catch (IOException e){
            System.out.println("Erro: " + e.getMessage());
        }

    }
}
