package curso_completo_java.sessao_16.pratica.exemplo_pratica01.model.entities;


import curso_completo_java.sessao_16.pratica.exemplo_pratica01.model.enums.Color;

public abstract class AbstractShape implements Shape {

        private Color color;

        public AbstractShape(Color color) {
            this.color = color;
        }

        public Color getColor() {
            return color;
        }

        public void setColor(Color color) {
            this.color = color;
        }
    }

