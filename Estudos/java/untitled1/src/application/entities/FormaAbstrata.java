package application.entities;

public abstract class FormaAbstrata implements FormaInterface {
    private Color color;

    public FormaAbstrata(Color color) {
        this.color = color;
    }

    public Color getColor() {
        return color;
    }

    public void setColor(Color color) {
        this.color = color;
    }
}
