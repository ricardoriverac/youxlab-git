package curso_completo_java.sessao_17.exercicios.exercicio03;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Scanner;

public class Program {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        Map<String, Integer> votos = new LinkedHashMap<>();

        System.out.print("Digite o caminho: ");
        String caminho = sc.nextLine();

        // /home/youx/youxlab-git/ciclo2/arquivos_aula_java/votos.csv


        try (BufferedReader br = new BufferedReader(new FileReader(caminho))) {

            String linha;
            while ((linha = br.readLine()) != null) {

                String[] campos = linha.split(",");

                String candidato = campos[0];
                int quantidade = Integer.parseInt(campos[1]);

                votos.put(
                        candidato,
                        votos.getOrDefault(candidato, 0) + quantidade
                );
            }

        } catch (IOException e) {
            System.out.println("Este arquivo não existe: " + e.getMessage());
        }

        for (Map.Entry<String, Integer> entry : votos.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue() + " votos");
        }
    }
}
