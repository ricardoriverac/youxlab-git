package application;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;


public class a_197 {
    public static void main(String[] args) {
        String caminhoArquivo = "/home/youx/in .txt3";

        try(BufferedReader br = new BufferedReader(new FileReader(caminhoArquivo))){
            Map<String, Integer> urna = new HashMap<>();
            String line = br.readLine();
            while (line != null){
                String [] fields = line.split(",");
                String nomeCandidato = fields[0];
                String votos = fields[1];
                int votosConvertido = Integer.parseInt(votos);
                if (urna.containsKey(nomeCandidato)){
                    int valorTotalCandidato = urna.get(nomeCandidato);
                    urna.put(nomeCandidato, valorTotalCandidato + votosConvertido);
                }
                else{
                    urna.put(nomeCandidato, votosConvertido);
                }
                line = br.readLine();
            }
            for (String candidato : urna.keySet()){
                System.out.println(candidato + " " + urna.get(candidato));
            }
        } catch (IOException e){
            System.out.println("Erro: " + e.getMessage());
        }
    }
}
