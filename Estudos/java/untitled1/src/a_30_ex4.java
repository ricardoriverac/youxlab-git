import java.util.Scanner;

public class a_30_ex4 {
    public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int numero, horas;
    double salario, valorHora;

        System.out.print("Caro usuário, por favor digite o número do funcionário: ");
        numero = sc.nextInt();
        System.out.print("Caro usuário, por favor digite a carga horária mensal deste funcionário: ");
        horas = sc.nextInt();
        System.out.print("Caro usuário, por favor digite o valor da hora deste funcionário: ");
        valorHora = sc.nextDouble();
        salario = horas * valorHora;
        System.out.printf("Caro usuário, o salário do funcionário %d é %.2f", numero, salario);
    }
}
