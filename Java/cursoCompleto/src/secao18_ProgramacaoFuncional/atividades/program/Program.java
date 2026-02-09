package secao18_ProgramacaoFuncional.atividades.program;

import secao12_Enumerates.exercicioPropost.entities.Product;
import secao18_ProgramacaoFuncional.atividades.entities.Employees;

import java.io.*;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Program {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Locale.setDefault(Locale.US);

        System.out.println("ADD YOUR FILE PATH: ");
        String path = sc.next();
        List<Employees> list = new ArrayList<>();


        try (BufferedWriter bw = new BufferedWriter(new FileWriter(path))) {
            System.out.println("How much employees do you wnat to register?");
            int n = sc.nextInt();

            for (int i = 0; i < n; i++) {
                System.out.println("NAME:");
                String name = sc.next();
                bw.write(name + ",");
                System.out.println("EMAIL");
                String email = sc.next();
                bw.write(email + ",");
                System.out.println("Salary: ");
                Double salary = sc.nextDouble();
                bw.write(String.valueOf(salary) + ",");
                bw.newLine();
                list.add(new Employees(name, email, salary));
            }
        }
        catch (IOException ex){

        }
        try(BufferedReader br = new BufferedReader(new FileReader(path))){
            String line = br.readLine();
            while(line!=null){
                String[] fields = line.split(",");
                list.add(new Employees<>(fields[0], fields[1], Double.parseDouble(fields[2])));
                line = br.readLine();
            }
        }

        catch (IOException e){
            System.out.println("DEU CERTO NAO PIA");
        }
        System.out.println("What's the value you want to filter? ");
        Comparator<String> comp = (s1, s2) -> s1.toUpperCase().compareTo(s2.toUpperCase());
        System.out.println("Define the value of the filter: ");
        double value = sc.nextDouble();

        List<String> names = list.stream()
                .filter(p -> p.getSalary() > value)
                .map(p -> p.getName())
                .sorted(comp)
                .collect(Collectors.toList());
        names.forEach(System.out::println);


        sc.close();
    }
}
