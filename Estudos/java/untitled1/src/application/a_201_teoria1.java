package application;

import java.util.Arrays;

public class a_201_teoria1 {
    public static int globalValue = 3;
    public static void main(String[] args) {
        int[] vect = new int[] {3, 4, 5};
        selecioneValoresAntigos(vect);
        System.out.println(Arrays.toString(vect));
    }

    public static void selecioneValoresAntigos(int[] numbers){
        for (int i = 0; i < numbers.length; i++) {
            if(numbers[i] % 2 != 0){
                numbers[i] += globalValue;
            }
            
        }
    }
}
