package Aula_104.Laco_for_each;

public class Exercicio_01 {
    public static void main(String[] args) {

        int[] vect = {4, 23, 43, 233, 12};
        int sum = 0;

        for (int n : vect) {
            System.out.println(n);
            sum += n;
        }
        System.out.println("Soma total: " + sum);
    }
}
