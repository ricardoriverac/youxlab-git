package Topios_basios_java.Funcoes_String;

public class codigo {
    static void main() {
        String original = "abcde FGHIJ ABC abc DEFG   ";

        String toLowerCase = original.toLowerCase();
        String toUpperCase = original.toUpperCase();
        String trim = original.trim();
        String substring = original.substring(2);
        String substring2 = original.substring(2, 9);
        String replace = original.replace('a', 'x'); // troca os 'a' por 'x' aspas simples para caracter (uma letra)
        String replace2 = original.replace("abc", "xy"); // troca os "abc" por "xyz" aspas duplas para string
        int indexOf = original.indexOf("bc");
        int lastIndexOf = original.lastIndexOf("bc"); //ultima ocorrencia

        System.out.println("Original: -> " + original + "<-");
        System.out.println("toLowerCase: -> " + toLowerCase + "<-");
        System.out.println("toUpperCase: -> " + toUpperCase + "<-");
        System.out.println("trim: -> " + trim + "<-");
        System.out.println("substring(2): -> " + substring + "<-");
        System.out.println("substring(2, 9): -> " + substring2 + "<-");
        System.out.println("replace('a', 'x'): -> " + replace + "<-");
        System.out.println("replace('abc', 'xy'): -> " + replace2 + "<-");
        System.out.println("Index of 'bc': " + indexOf);
        System.out.println("Last index of 'bc': " + lastIndexOf);

    }
}
