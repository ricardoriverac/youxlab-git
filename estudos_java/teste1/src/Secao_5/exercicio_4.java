package Secao_5;
import java.util.Scanner;

public class exercicio_4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int start, end, duration;
        start = sc.nextInt();
        end = sc.nextInt();
        if (start<end) {
            duration = (end - start);
        }
        else {
            duration = 24 - start + end;
        }
        System.out.printf("This match lasted " + duration + " hour(s)");
    }
}
