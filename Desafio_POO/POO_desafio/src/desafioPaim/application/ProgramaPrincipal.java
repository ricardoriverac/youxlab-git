package desafioPaim.application;

import desafioPaim.entities.Cliente;
import desafioPaim.entities.Endereco;
import desafioPaim.entities.Pedido;
import desafioPaim.entities.Produto;
import desafioPaim.entities.entitiesEnums.StatusPedido;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ProgramaPrincipal {

    static void main() {

        Scanner sc = new Scanner(System.in);


        List<Cliente> clientes = List.of(
                new Cliente(1, "Ágatha Emanuelle", "@agathaayouxlab"),
                new Cliente(2, "Luis Paiva", "@luissyoux9879"),
                new Cliente(3, "Emily", "@emilyycristina"),
                new Cliente(4, "Ana Andrade", "@andradeana"),
                new Cliente(5, "Maria Vitoria", "@mariaavitoria")
        );


        List<Produto> produtos = List.of(
                new Produto(1, "Lápis", 11),
                new Produto(2, "Garrafa", 300),
                new Produto(3, "Carregador", 59),
                new Produto(4, "Celular", 5000),
                new Produto(5, "Caneta", 32),
                new Produto(6, "Caneca", 89)
        );


        List<Pedido> pedidos = new ArrayList<>();

        pedidos.add(new Pedido(
                1,
                clientes.get(3),
                produtos.get(0),
                new Endereco("Rua Azul", "A123", "Lavras", "MG"),
                StatusPedido.ATRASO
        ));

        pedidos.add(new Pedido(
                2,
                clientes.get(1),
                produtos.get(3),
                new Endereco("Rua Rosa", "B444", "Lavras", "MG"),
                StatusPedido.ENTREGUE
        ));

        pedidos.add(new Pedido(
                3,
                clientes.get(2),
                produtos.get(5),
                new Endereco("Rua Verde", "C434", "Lavras", "MG"),
                StatusPedido.AGUARDANDO_ENVIO
        ));


        int opcao = -1;

        while (opcao != 0) {

            System.out.println("\n=== MENU ===");
            System.out.println("1 - Mostrar todos os pedidos");
            System.out.println("2 - Buscar pedido por ID");
            System.out.println("3 - Buscar pedidos por status");
            System.out.println("4 - Ver valor total do pedido");
            System.out.println("0 - Sair");
            System.out.print("Escolha uma opção: ");
            opcao = sc.nextInt();

            if (opcao == 1) {
                for (Pedido p : pedidos) {
                    System.out.println(p);
                }

            } else if (opcao == 2) {
                System.out.print("Digite o ID do pedido: ");
                int id = sc.nextInt();

                boolean encontrado = false;
                for (Pedido p : pedidos) {
                    if (p.getId() == id) {
                        System.out.println(p);
                        encontrado = true;
                    }
                }

                if (!encontrado) {
                    System.out.println("Pedido não encontrado.");
                }

            } else if (opcao == 3) {
                System.out.println("1 - AGUARDANDO_ENVIO");
                System.out.println("2 - EM_ANDAMENTO");
                System.out.println("3 - ATRASADO");
                System.out.println("4 - ENTREGUE");
                System.out.print("Escolha o status: ");
                int escolha = sc.nextInt();

                StatusPedido status = StatusPedido.values()[escolha - 1];

                for (Pedido p : pedidos) {
                    if (p.getStatus() == status) {
                        System.out.println(p);
                    }
                }

            } else if (opcao == 4) {
                System.out.print("Digite o ID do pedido: ");
                int id = sc.nextInt();

                for (Pedido p : pedidos) {
                    if (p.getId() == id) {
                        System.out.println("Valor total: R$ " + p.getProduto().getPreco());
                    }
                }

            } else if (opcao == 0) {
                System.out.println("Sistema encerrado.");

            } else {
                System.out.println("Opção inválida.");
            }
        }

        sc.close();
    }
}