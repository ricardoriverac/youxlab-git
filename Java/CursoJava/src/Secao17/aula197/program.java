package Secao17.aula197;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;


public class program {
    public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
            Map<String, Integer> totais = new HashMap<>();

            System.out.print("Enter file full path: ");
            String caminhoArquivo = sc.nextLine();

            try (BufferedReader leitor = new BufferedReader(new FileReader(caminhoArquivo))) {
                String linha;
                while ((linha = leitor.readLine()) != null) {
                    linha = linha.trim();
                    if (linha.isEmpty()) continue;

                    String[] partes = linha.split(",");
                    String candidato = partes[0].trim();
                    int votos = Integer.parseInt(partes[1].trim());

                    totais.put(candidato, totais.getOrDefault(candidato, 0) + votos);
                }

                for (Map.Entry<String, Integer> entrada : totais.entrySet()) {
                    System.out.println(entrada.getKey() + ": " + entrada.getValue());
                }

            } catch (IOException e) {
                System.out.println("Erro ao ler o arquivo: " + e.getMessage());
            } catch (NumberFormatException e) {
                System.out.println("Formato inválido de votos no arquivo.");
            } finally {
                sc.close();
            }
        }
    }

