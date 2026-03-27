package Secao_15.Aula_168.Exercicio_Proposto.application;

import Secao_15.Aula_168.Exercicio_Proposto.entities.Calculo;

import java.io.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Digite o caminho do arquivo: ");
        String strPath = sc.nextLine();

        File path = new File(sc.nextLine());

        try (BufferedReader br = new BufferedReader(new FileReader(path))) {
            String line = br.readLine();

            while (line != null) {

                String[] vect = line.split(",");

                Double precoTotal = Double.parseDouble(vect[1]);
                Integer quantidade = Integer.parseInt(vect[2]);

                Calculo cl = new Calculo(vect[0], precoTotal, quantidade);

                boolean success = new File(path.getParent() + "/out").mkdir();

                String localeFile = path.getParent();

                try (BufferedWriter bw = new BufferedWriter(new FileWriter(localeFile + "/out/summary.csv", true))) {

                    bw.write(cl.getNomeProduto() + ", " + cl.precoTotal());
                    bw.newLine();

                    line = br.readLine();
                }
                catch (IOException e ) {
                    System.out.println(e.getMessage());
                }

            }
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }
}