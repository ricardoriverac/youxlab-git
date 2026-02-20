import java.util.Locale;
import java.util.Scanner;

public class Exercicio_04 {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        Double numero_funcionario, horas_trabalhadas, rebe_hora, resultado;

        System.out.print("Digite o número do funcionário: ");
        numero_funcionario = sc.nextDouble();

        System.out.print("Digite as o valor por horas trabalhadas: ");
        rebe_hora = sc.nextDouble();

        System.out.print("Digite as horas trabalhadas: ");
        horas_trabalhadas = sc.nextDouble();

        resultado = (rebe_hora * horas_trabalhadas);

        System.out.printf("Número do trabalhador: %.2f %n", numero_funcionario);
        System.out.printf("O salário é: %.2f", resultado);




    }
}