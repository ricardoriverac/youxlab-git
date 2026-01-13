package application.POO;

import application.entities.OrderStatus;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

import static application.POO.Status.EM_ANDAMENTO;

public class desafioPOO2 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        int menu = 0;
        List<Produto> produtos = new ArrayList<>();
        List<Pedido> pedidos = new ArrayList<>();
        produtos.add(new Produto(1, "TV", 1000.0));
        produtos.add(new Produto(2, "Mouse", 40.0));
        produtos.add(new Produto(3, "Computador", 3000.0));
        produtos.add(new Produto(4, "Alexa", 800.0));
        produtos.add(new Produto(5, "Celular", 3000.0));
        produtos.add(new Produto(6, "Fone", 70.0));
        pedidos.add(new Pedido(1, new Cliente(1, "Ruan", "Ruan@gmail.com"), produtos, new Endereco("Rua Joaquim Olímpio de Carvalho", "1200 A", "Lavras", "Minas Gerais"), Status.EM_ANDAMENTO));
        pedidos.add(new Pedido(2, new Cliente(2, "Davi", "Davi@gmail.com"), produtos, new Endereco("Rua José Giarola", "200 A", "Lavras", "Minas Gerais"), Status.ATRASADO));
        pedidos.add(new Pedido(3, new Cliente(3, "Renan", "Renan@gmail.com"), produtos, new Endereco("Rua raimunda Marques Guimaraẽs", "40 B", "Lavras", "Minas Gerais"), Status.ENTREGUE));
        pedidos.add(new Pedido(4, new Cliente(4, "Ravi", "Ravi@gmail.com"), produtos, new Endereco("Rua 2", "140", "Ijaci", "Minas Gerais"), EM_ANDAMENTO));
        pedidos.add(new Pedido(5, new Cliente(5, "João", "João@gmail.com"), produtos, new Endereco("Rua Primeiro de maio", "275", "Belo Horizonte", "Minas Gerais"), Status.AGUARDANDO_ENVIO));

        while (menu != 3) {
            System.out.print("\nCaro usuário, escolha uma das opções abaixo: ");
            System.out.println("1- Buscar pedido por ID\n"
                    + "2- Buscar pedido por Status\n"
                    + "3- Sair");

            menu = sc.nextInt();

            switch (menu) {
                case 1:
                    System.out.print("Caro usuário, por favor informe o id de seu pedido: ");
                    Integer idVerificacao = sc.nextInt();
                    System.out.print("\nCaro usuário, seu pedido de id" + idVerificacao + ", é composto por:" + pedidos.stream().filter(p -> p.getId().equals(idVerificacao)).findFirst().orElse(null));
                    break;
                case 2:
                    System.out.print("Caro usuário, por favor informe o status de seu pedido: ");
                    String statusVerificado = sc.next();
                    System.out.print("\nCaro usuário, seu pedido de status" + statusVerificado + ", é composto por:" + pedidos.stream().filter(p -> p.getStatus().equals(Status.valueOf(statusVerificado))).findFirst().orElse(null));
                    break;
                case 3:
                    break;
            }
        }
        System.out.print("Programa encerrado!");
    }
}