package secao_10.aula103;

public class Aula103 {
    static void main() {
        String[] vect = new String[] {"Maria", "Bob", "Alex"};
        for (int i=0; i< vect.length; i++) {
            System.out.println(vect[i]);
        }
        for (String obj : vect) {
            System.out.println(obj);
        }
    }
}
