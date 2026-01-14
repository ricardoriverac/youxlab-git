package application.entities;

public class ImpostoBrasilServico {
    public Double tax(Double quantidade){
        if(quantidade <= 100.0){
            return quantidade * 0.2;
        }
        else {
            return quantidade * 0.15;
        }
    }
}
