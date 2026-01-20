package application;

import application.entities.Login;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.IOException;
import java.time.Instant;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Date;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class a_194 {
    public static void main(String[] args) {
        DateTimeFormatter dateTimeFormatter = DateTimeFormatter.ISO_DATE;
        Scanner sc = new Scanner(System.in);
        String caminhoArquivo = "/home/youx/in.txt2";

        try (BufferedReader br = new BufferedReader(new FileReader(caminhoArquivo))) {
            Set<Login> logins = new HashSet<>();
            String line = br.readLine();
            while (line != null) {
                String[] fields = line.split(" ");
                String nomeUsuarioConvertido = fields[0];
                Date dataLogin = Date.from(Instant.parse(fields[1]));
                logins.add(new Login(dataLogin, nomeUsuarioConvertido));

                line = br.readLine();
            }
            System.out.println("Total de Usuários: " + logins.size());
        } catch (IOException e) {
            System.out.println("Erro: " + e.getMessage());
        }
        sc.close();
    }
}