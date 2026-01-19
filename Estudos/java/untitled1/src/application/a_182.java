package application;

import application.entities.Funcionario2;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class a_182 {
    public static void main(String[] args){
        List<Funcionario2> funcionarios = new ArrayList<>();
        String path = "/home/youx/in.txt";

        try (BufferedReader br = new BufferedReader(new FileReader(path))) {
            String funcionarioCsv = br.readLine();
            while (funcionarioCsv != null) {
                String[] fields = funcionarioCsv.split(",");
                funcionarios.add(new Funcionario2(fields[0], Double.parseDouble(fields[1])));
                funcionarioCsv = br.readLine();
            }
            Collections.sort(funcionarios);
            for (Funcionario2 funcionario : funcionarios) {
                System.out.println(funcionario.getNome() + ", " + funcionario.getSalario());
            }
        } catch (IOException e) {
            System.out.println("Erro: " + e.getMessage());

        }




        }
    }
