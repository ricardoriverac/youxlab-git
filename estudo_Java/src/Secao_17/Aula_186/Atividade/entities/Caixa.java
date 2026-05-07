package Secao_17.Aula_186.Atividade.entities;

public class Caixa<T> {

    private T type;

    public void guardar(T type) {
        this.type = type;
    }

    public T pegar() {
        return this.type;
    }
}
