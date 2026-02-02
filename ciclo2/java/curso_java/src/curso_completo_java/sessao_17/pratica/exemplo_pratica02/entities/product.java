package curso_completo_java.sessao_17.pratica.exemplo_pratica02.entities;

public class product implements Comparable<product> {

        private String name;
        private Double price;

        public product(String name, Double price) {
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

        @Override
        public String toString() {
            return name + ", " + String.format("%.2f", price);
        }

        @Override
        public int compareTo(product other) {
            return price.compareTo(other.getPrice());
        }
    }

