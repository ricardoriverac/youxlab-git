package secao_07;

import java.util.Scanner;

import static sun.swing.MenuItemLayoutHelper.max;

public class aula_66 {
    static void main() {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter three numbers: ");
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        int higher = max(a, b, c);
        sc.close();
    }
    public static int max(int x, int y, int z){
        int aux;
        if (x > y && x > z){
            aux = x;
        } else if (y > z) {
            aux = z;
            
        }else {
            aux = z;
        }
        return aux;
    }
    public static void showREsult(int value){
        System.out.println("Higher = " + value);

    }

}

