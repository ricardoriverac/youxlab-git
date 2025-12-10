package secao_07;

import java.util.Locale;

public class aula_64 {
    static void main() {
        String original = "abcde FGHIJ ABC abc DEFG";

        String s01 = original.toLowerCase();
        String s02 = original.toUpperCase();
        String s03 = original.trim();
        String s04 = original.substring(2);
        String s05 = original.substring(2, 9);
        String s06 = original.replace('a', 'x');

        System.out.println("Original: " + original + "-");
        System.out.println("toLowerCase : -" + s01 + "-");
        System.out.println("toUpperCase : -" + s02 + "-");
        System.out.println("trim : -" + s03 + "-");
        System.out.println("subistring(2): -" + s04 + "-");
        System.out.println("subistring(2, 9): -" + s05 + "-");

    }
}
