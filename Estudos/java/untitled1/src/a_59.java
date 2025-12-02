public class a_59 {
    public static void main(String[] args) {

        String original = "abcde FGHIJ ABC abc DEFG  ";
        String s1 = original.toLowerCase();
        String s2 = original.toUpperCase();
        String s3 = original.trim();
        String s4 = original.substring(2);
        String s5 = original.substring(2, 9);
        String s6 = original.replace("a", "x");
        String s7 = original.replace("abc", "xy");
        int i = original.lastIndexOf("bc");
        int ii = original.indexOf("bc");
        System.out.println("Original: "+ original);
        System.out.println(s1);
        System.out.println(s2);
        System.out.println(s3);
        System.out.println(s4);
        System.out.println(s5);
        System.out.println(s6);
        System.out.println(s7);
        System.out.println(i);
        System.out.println(ii);

        String s = "Potato apple lemon";
        String[] vect = s.split(" ");
        System.out.println(vect[0]);
        System.out.println(vect[1]);
        System.out.println(vect[2]);

    }
}
