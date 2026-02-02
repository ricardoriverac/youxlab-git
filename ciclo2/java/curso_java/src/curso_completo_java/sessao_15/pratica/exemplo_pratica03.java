package curso_completo_java.sessao_15.pratica;

// AULA 163 - Bloco try-with-resouces

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class exemplo_pratica03 {

        public static void main(String[] args) {

            String path = "/home/youx/in.txt";

            try (BufferedReader br = new BufferedReader(new FileReader(path))) {

                String line = br.readLine();

                while (line != null) {
                    System.out.println(line);
                    line = br.readLine();
                }
            }
            catch (IOException e) {
                System.out.println("Error: " + e.getMessage());
            }

            }
        }



