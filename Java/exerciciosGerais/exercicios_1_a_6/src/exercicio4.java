import java.util.Locale;
import java.util.Scanner;

public class exercicio4 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        double valorHora, horaTrabalho, salario;
        int idFunc;

        idFunc = sc.nextInt();
        horaTrabalho = sc.nextDouble();
        valorHora = sc.nextDouble();

        salario = valorHora * horaTrabalho;

        System.out.println("O ID do funcionário " + idFunc);
        System.out.printf("\nO salário é U$ %.2f%n", salario);
        sc.close();
    }

}
