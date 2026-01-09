package application;

import application.entities.Circulo;
import application.entities.Color;
import application.entities.Forma;
import application.entities.Retangulo2;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class a_144 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        List<Forma> formas = new ArrayList<>();

        System.out.print("Caro usuário, por favor insira quantas formas geométricas serão analisadas: ");
        int quantidadeFormas = sc.nextInt();

        for (int i = 0; i < quantidadeFormas; i++) {
            System.out.print("Caro usuário, sua forma é um retângulo ou um círculo? ");
            char formaGeometrica = sc.next().charAt(0);
            System.out.print("Caro usuário, qual a cor da sua forma? [BLACK/RED/BLUE]");
            String corForma = sc.next();
            Color cor = Color.valueOf(corForma);
            if(formaGeometrica == 'r' || formaGeometrica == 'R'){
                System.out.print("Caro usuário, qual a altura de seu retângulo? ");
                Double altura = sc.nextDouble();
                System.out.print("Caro usuário, qual a largura de seu retângulo? ");
                Double largura = sc.nextDouble();
                formas.add(new Retangulo2(altura, largura, cor));
            }
            else{
                System.out.print("Caro usuário, qual o raio do seu círculo?");
                Double raio = sc.nextDouble();
                formas.add(new Circulo(cor, raio));
            }
        }
        System.out.print("Areas: ");
        for(Forma f : formas){
            System.out.print(f.area() + "\n");
        }
    }
}
