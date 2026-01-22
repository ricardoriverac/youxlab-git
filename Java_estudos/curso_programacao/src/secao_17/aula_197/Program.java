package secao_17.aula_197;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class Program {
    public static void main(String[] args) {
    Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        Map<String, Integer> votos = new HashMap<>();

        System.out.print("Enter file full path: ");
        String arquivo = sc.nextLine();

        try (BufferedReader br = new BufferedReader(new FileReader(arquivo))) {

            String line = br.readLine();
            while (line != null) {

                String[] campo = line.split(",");
                String name = campo[0];
                int count = Integer.parseInt(campo[1]);

                if (votos.containsKey(name)) {
                    int votesSoFar = votos.get(name);
                    votos.put(name, count + votesSoFar);
                }
                else {
                    votos.put(name, count);
                }

                line = br.readLine();
            }

            for (String key : votos.keySet()) {
                System.out.println(key + ": " + votos.get(key));
            }

        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }

        sc.close();
    }
}


