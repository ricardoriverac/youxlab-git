package secao_08.produto.exercicio_1;

public class entities {

    public static double widht;
    public static double height;

    public static double area(){
        return widht * height;
    }

    public static double perimeter(){
        return (widht + height) * 2;
    }
    public static double diagonal() {
        return Math.sqrt((widht * widht) + (height * height));
    }


}
