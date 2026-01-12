package application;

import entities.*;

import java.util.Formattable;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

import static entities.StatusPedido.*;

public class ProgramaPrincipal {
    static void main() {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        Cliente cliente = new Cliente();
        Produto produto = new Produto();
        Pedido pedido = new Pedido();



        List<Cliente> clientes = List.of(
                new Cliente(0, "Ágatha Silva", "agathasilva123@gmail.com"),
                new Cliente(1, "Henrique Soares", "henriquesoares356@gmail.com"),
                new Cliente(2, "Emily Alves", "emilyalves234@gmail.com"),
                new Cliente(3, "Maria Oliveira", "mariaoliveira658@gmail.com"),
                new Cliente(4, "Luis Paiva", "luispaiva776@gmail.com"));


        List<Produto> produtos = List.of(
                new Produto(0, "Computador", 4500.00),
                new Produto(1, "Mouse", 79.00),
                new Produto(2, "Teclado", 200.00),
                new Produto(3, "Celular", 2300.00),
                new Produto(4, "Microfone", 269.00),
                new Produto(5, "Munitor", 900.00)
                );

        List<Endereco> enderecoEntrega = List.of(
                new Endereco(0, "Avenida Paulista", "170A", "Sâo Paulo", "Sâo Paulo"),
                new Endereco(1, "Rua Carvalho", "1976", "Belo Horizonte", "Minas Gerais"),
                new Endereco(2, "Rua Fernando de Sousa", "1230", "Capelinha", "Minas Gerais"),
                new Endereco(3, "Avenida Cacau show", "19", "Florianópolis", "Tocatins"),
                new Endereco(4, "Rua Costa Rica", "100", "Bom Sucesso", "Rio de Janeiro")
        );

        List<Pedido> pedidos = List.of(
                new Pedido(1, clientes.get(0), 1, enderecoEntrega.get(1), AGUARDANDO_PEDIDO),
                new Pedido(2, clientes.get(1), 2, enderecoEntrega.get(3), EM_ANDAMENTO),
                new Pedido(3, clientes.get(2), 1, enderecoEntrega.get(2), ATRASADO),
                new Pedido(4, clientes.get(3), 1, enderecoEntrega.get(4), ENTREGUE),
                new Pedido(5, clientes.get(4), 2, enderecoEntrega.get(0), EM_ANDAMENTO),
                new Pedido(6, clientes.get(1), 1, enderecoEntrega.get(1), ATRASADO)
        );
        int buscar = 0;
        while (buscar != 4) {
            System.out.println("""
                    
                    1 - BUSCAR PEDIDO POR ID
                    2 - VER O VALOR DO PRODUTO POR ID
                    3 - BUSCAR PEDIDOS POR STATUS
                    4 - SAIR""");
            System.out.print("-> ");
            buscar = sc.nextInt();
            System.out.println();

            if (buscar == 4){
                System.out.print("Saindo...");
                break;
            }
            else if (buscar == 1){
                System.out.print("Digite o ID (1 - 6): ");
                int idProcura = sc.nextInt();
                if (idProcura >= 7 || idProcura <= 0){
                    System.out.println("NÃO EXISTE ESSE PEDIDO!");
                }
                else {
                    System.out.println(pedidos.get(idProcura - 1));
                }
            }
            else if (buscar == 2) {
                System.out.println("""
                        1 - Computador
                        2 - Mouse
                        3 - Teclado
                        4 - Celular
                        5 - Microfone
                        6 - Munitor
                        """);
                System.out.print("Digite o ID: ");
                int idProcura = sc.nextInt();
                double valorProduto = 0.0;
                String nomeProduto = "";
                for (Produto p : produtos){
                    if (idProcura >= 7 || idProcura <= 0){
                        System.out.println("NÃO EXISTE ESSE PRODUTO!");
                    }
                    if (p.getId() == idProcura - 1){
                        valorProduto = p.getPreco();
                        nomeProduto = p.getNome();
                    }
                }
                System.out.printf("NOME: %s \nVALOR: %.2f%n", nomeProduto, valorProduto);
            }
            else if (buscar == 3) {
                System.out.println("""
                        AGUARDANDO_PEDIDO
                        EM_ANDAMENTO
                        ATRASADO
                        ENTREGUE""");
                System.out.print("Digite o STATUS: ");
                String status = sc.next().toUpperCase();

                for (Pedido p : pedidos) {
                    if (p.getStatus() == StatusPedido.valueOf(status)) {
                        System.out.println(p);
                    }
                }
            }
            else {
                System.out.println("NÚMERO INVÁLIDO!");
            }
        }

        sc.close();
    }
}
