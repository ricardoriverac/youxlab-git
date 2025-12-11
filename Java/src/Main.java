import java.util.Locale;
import java.util.Scanner;

public class Main {

    static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        int s1;
        String x, y, z;
        double m;
        m = sc.nextDouble();
        s1 = sc.nextInt();
        sc.nextLine();
        x = sc.nextLine();
        y = sc.nextLine();
        z = sc.nextLine();
        System.out.println(s1);
        System.out.println(x);
        System.out.println(y);
        System.out.println(z);

        sc.close();
    }
}
