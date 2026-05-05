package Secao_17.Aula_186.Generics.entities;

public class Repositorio<T> {

    private T type;

    public void salvar( T valor) {
        this.type = valor;
    }

    public T obter() {
        return this.type;
    }
}