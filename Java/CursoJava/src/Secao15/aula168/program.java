package Secao15.aula166;

public class program {
    public static void main(String[] args) {

            System.out.println("--- RESUMO DOS VALORES ---");
            System.out.println("Nome do Item             | Valor Total");
            calcularEExibir("TV LED", 1290.99, 1);
            calcularEExibir("Video Game Chair", 350.50, 3);
            calcularEExibir("Iphone X", 900.00, 2);
            calcularEExibir("Samsung Galaxy 9", 850.00, 2);
        }

        private static void calcularEExibir(String nome, double preco, int quantidade) {
            double total = preco * quantidade;
            System.out.printf("%-25s | R$ %.2f%n", nome, total);
        }
    }
