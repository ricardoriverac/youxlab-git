package Programacao_Orientada_Objetos.Membros_Estaticos.util;

public class Calculator {
    public static final double PI = 3.14159;
    /* final = serve para que o valor atribuido é constante e não será alterado mais */

    public static double circumference(double radius) {
        return 2.0 * PI * radius;
    }

    public static double volume(double radius) {
        return 4.0 * PI * radius * radius * radius / 3.0;
    }
}
