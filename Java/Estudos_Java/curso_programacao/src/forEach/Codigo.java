package forEach;

public class Codigo {
    static void main() {

        String[] vect = new String[] {"Maria", "Bob", "Alex"};
        for (int i=0; i< vect.length; i++) {
            System.out.println(vect[i]);
        }
        // for each
        for (String obj : vect) {
            System.out.println(obj);
        }
    }
}
