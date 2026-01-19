package curso_completo_java.sessao_16.pratica.exemplo_pratica01.model.entities;


import curso_completo_java.sessao_16.pratica.exemplo_pratica01.model.enums.Color;

public class Circle extends AbstractShape {

        private Double radius;

        public Circle(Color color, Double radius) {
            super(color);
            this.radius = radius;
        }

        public Double getRadius() {
            return radius;
        }

        public void setRadius(Double radius) {
            this.radius = radius;
        }

        @Override
        public double area() {
            return Math.PI * radius * radius;
        }
}
