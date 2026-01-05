package secao6_estruturasRepetitivas;

public class teste3 {
    public static void main(String[] args){
        int y = 0;
        int x = 5;

        while(x > 2) {
            System.out.print(x + "; ");
            y += x;
            x -= 1;
        }
    }
}
