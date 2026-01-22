package curso_completo_java.sessao_17.pratica.exemplo_pratica02.application;

//  AULA 188 - Tipos curinga

import curso_completo_java.sessao_17.pratica.exemplo_pratica02.entities.product;
import curso_completo_java.sessao_17.pratica.exemplo_pratica02.services.CalculationService;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class program {

        public static void main(String[] args) {

            Locale.setDefault(Locale.US);

            List<product> list = new ArrayList<>();

            String path = "/home/youx/in.txt";

            try (BufferedReader br = new BufferedReader(new FileReader(path))) {

                String line = br.readLine();
                while (line != null) {
                    String[] fields = line.split(",");
                    list.add(new product(fields[0], Double.parseDouble(fields[1])));
                    line = br.readLine();
                }

                product x = CalculationService.max(list);
                System.out.println("Most expensive:");
                System.out.println(x);

            } catch (IOException e) {
                System.out.println("Error: " + e.getMessage());
            }
        }
    }

