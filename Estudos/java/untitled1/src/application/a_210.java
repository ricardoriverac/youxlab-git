package application;

import application.entities.Funcionarios5;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;
import java.util.stream.Collectors;

public class a_210 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        String caminhoArquivo = "/home/youx/in.txt5";

        try(BufferedReader br = new BufferedReader(new FileReader(caminhoArquivo))){
            List<Funcionarios5> funcionarios = new ArrayList<>();
            String line = br.readLine();
            while (line != null){
                String[] fields = line.split(",");
                funcionarios.add(new Funcionarios5(fields[0], fields[1], Double.parseDouble(fields[2])));
                line = br.readLine();
            }
            System.out.println("Caro usuário, qual o valor de salário minimo que você deseja filtrar? ");
            Double valorMinimo = sc.nextDouble();
            List<String> emails = new ArrayList<>();
            for(Funcionarios5 f : funcionarios){
                if(f.getSalarioFuncionario() > valorMinimo){
                    String email = f.getEmailFuncionario();
                    emails.add(email);
                }
            }
            System.out.println("Emails: ");
            emails.forEach(System.out::println);

            Double somaM = funcionarios.stream().filter(f -> f.getNomeFuncionario().charAt(0) == 'M').map(Funcionarios5::getSalarioFuncionario).reduce(0.0, (x, y) -> x+y);
            System.out.println("Soma: " + somaM);
        } catch (IOException e){
            System.out.println("Erro: " + e.getMessage());
        }
    }
}
