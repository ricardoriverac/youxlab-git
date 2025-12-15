import java.util.Scanner;

public class exercicio5 {
    public static void main(String[] args) {
        int idPeca1, qntdPeca1, idPeca2, qntdPeca2;
        double valorUn1, valorUn2, valorPago1, valorPago2;

        Scanner sc = new Scanner(System.in);
        System.out.println("Digite as informações da primeira peça:");
        idPeca1 = sc.nextInt();
        valorUn1 = sc.nextDouble();
        qntdPeca1 = sc.nextInt();
        System.out.println("Digite as informações da segunda peça:");
        idPeca2 = sc.nextInt();
        valorUn2 = sc.nextDouble();
        qntdPeca2 = sc.nextInt();

        valorPago1 = (double) qntdPeca1 * valorUn1;
        valorPago2 = (double) qntdPeca2 * valorUn2;

        System.out.printf("ID da peça: ", idPeca1 + "\nValor a pagar: R$ %.2f%n", valorPago1);
        System.out.printf("ID da peça: ", idPeca2 + "\nValor a pagar: R$ %.2f%n", valorPago2);
    }
}
