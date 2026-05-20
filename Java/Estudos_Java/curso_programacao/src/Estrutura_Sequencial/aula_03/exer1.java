package Estrutura_Sequencial.aula_03;

public class exer1 {
    static void main() {
        int num1 = 10;
        int num2 = 30;
        int A, B;
        A = Math.addExact(num1, num2);
        System.out.println("Soma = " + A);

        num1 = -30;
        num2 = 10;
        A = Math.addExact(num1, num2);
        System.out.println("Soma = " + A);

        num1 = 0;
        num2 = 0;
        A = Math.addExact(num1, num2);
        System.out.println("Soma = " + A);

    }
}
