package curso_completo_java.sessao_18.pratica.exemplo_pratica06.entities;

public class Product {


    private String name;
    private Double price;

    public Product(String name, Double price) {
        this.name = name;
        this.price = price;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Double getPrice() {
        return price;
    }

    public void setPrice(Double price) {
        this.price = price;
    }

    public static String staticUpperCaseName (curso_completo_java.sessao_18.pratica.exemplo_pratica05.entities.Product p) {
        return p.getName().toUpperCase();
    }

    public String nonStaticUpperCaseName() {
        return name.toUpperCase();
    }

    @Override
    public String toString() {
        return "Product{" +
                "name='" + name + '\'' +
                ", price= " + price +
                '}';
    }
}
