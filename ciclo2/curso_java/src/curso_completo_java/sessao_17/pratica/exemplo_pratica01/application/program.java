package curso_completo_java.sessao_17.pratica.exemplo_pratica01.application;


import curso_completo_java.sessao_17.pratica.exemplo_pratica01.services.PrintService;

import java.util.Scanner;

public class program {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        PrintService<Integer> ps = new PrintService<>();

        System.out.print("How many values? ");
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            Integer value = sc.nextInt();
            ps.addValue(value);
        }

        ps.print();
        Integer x = ps.first();
        System.out.println("First: " + x);

        sc.close();
    }
}




