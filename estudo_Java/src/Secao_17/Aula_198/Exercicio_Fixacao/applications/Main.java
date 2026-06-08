package Secao_17.Aula_198.Exercicio_Fixacao.applications;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Digite o caminho do arquivo: ");
        String path = sc.nextLine();

        Map<String, Integer> votos = new HashMap<>();

        try (BufferedReader br = new BufferedReader(new FileReader(path))) {

            String linha = br.readLine();

            while (linha != null) {

                String[] campos = linha.split(",");

                String candidato = campos[0];
                int quantidadeVotos = Integer.parseInt(campos[1]);

                votos.put(candidato, votos.getOrDefault(candidato, 0) + quantidadeVotos);
            }

            System.out.println("RESULTADO DA ELEIÇÃO:");
            for (Map.Entry<String, Integer> entry : votos.entrySet()) {
                System.out.println(entry.getKey() + ": " + entry.getValue());
            }

        } catch (IOException e) {
            System.out.println("Erro: " + e.getMessage());
        }
    }
}