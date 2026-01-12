package entities;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Endereco {

    private int id;
    private String logradouro;
    private  String numero;
    private String cidade;
    private String estado;

    public Endereco(int id,String logradouro, String numero, String cidade, String estado) {
        this.logradouro = logradouro;
        this.numero = numero;
        this.cidade = cidade;
        this.estado =  estado;
    }

    public String toString(){
        return "\nLogradouro: "
                + logradouro
                + "\nNúmero: "
                + numero
                + "\nCidade: "
                + cidade
                + "\nEstado: "
                + estado;
    }
}
