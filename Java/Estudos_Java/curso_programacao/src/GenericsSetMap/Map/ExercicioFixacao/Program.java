package GenericsSetMap.Map.ExercicioFixacao;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Program {

    static void main() {

        Scanner sc = new Scanner(System.in);

        Map<String, Integer> eleicao = new HashMap<>();
        String[] split;

        System.out.print("Enter file full path: ");
        String file = sc.nextLine();

        try (BufferedReader br = new BufferedReader(new FileReader(file))) {

            String line = br.readLine();
            String name = "";
            while (line != null) {
                split = line.split(",");
                name = split[0];
                int votos = Integer.parseInt(split[1]);

                if (eleicao.containsKey(name)){
                    int countVotos = eleicao.get(name);
                    eleicao.put(name, votos + countVotos);
                }
                else {
                    eleicao.put(name, votos);
                }

                line = br.readLine();

            }

            for (String s : eleicao.keySet()){
                System.out.println(s + ": " + eleicao.get(s));
            }

        }
        catch (FileNotFoundException f) {
            System.out.println("Error: " + f.getMessage());
        }
        catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }

        sc.close();
    }
}
