package Secao_16.Aula_182.Interface_Comparable.application;

import Secao_16.Aula_182.Interface_Comparable.entities.Employee;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
    public static void main(String[] args) {

        List<Employee> list = new ArrayList<>();
        String path = "/home/youx/youxlab-git/estudo_Java/src/Secao_16/Aula_182/Interface_Comparable/File/index";

        try (BufferedReader br = new BufferedReader(new FileReader(path))) {
            String employeeCsv = br.readLine();
            while (employeeCsv != null) {
                String[] fields = employeeCsv.split(",");
                list.add(new Employee(fields[0], Double.parseDouble(fields[1])));
                employeeCsv = br.readLine();
            }
            Collections.sort(list);
            for (Employee emp : list) {
                System.out.println(emp.getName() + ", " + emp.getSalary());
            }
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}