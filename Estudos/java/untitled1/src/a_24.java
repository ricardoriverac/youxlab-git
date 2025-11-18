import java.util.Locale;

public class a_24 {
    public static void main(String[] args) {
        System.out.print("Bom dia!");
        System.out.println("Bom dia!");
        int y = 32;
        System.out.println(y);
        double x = 10.25784;
        System.out.println(x);
        System.out.printf("%.2f%n", x);
        System.out.printf("%.4f%n", x);
        Locale.setDefault(Locale.US);
        System.out.printf("%.4f%n", x);
        System.out.println("Resultado =" + x +  "Metros");
    }
}
