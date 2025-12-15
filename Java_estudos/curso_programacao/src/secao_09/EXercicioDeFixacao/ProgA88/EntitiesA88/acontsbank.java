package secao_09.EXercicioDeFixacao.ProgA88.EntitiesA88;

public class acontsbank {

    private String holder;
    private int number;
    private double balence;

    public acontsbank(String holder, int number) {
        this.holder = holder;
        this.number = number;
    }

    public  acontsbank (String holder, int number, double initialDeposit){
        this.holder = holder;
        this.number = number;
        this.balence = initialDeposit;
    }


    public double getBalence() {
        return balence;
    }
    public  void deposit(double amount){
        this.balence += amount;
    }

    public void setBalence(double balence) {
        this.balence = balence;
    }

    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public String getHolder() {
        return holder;
    }

    public void setHolder(String holder) {
        this.holder = holder;
    }

    public void withDraw(double amount){
        this.balence -= 5.00 + amount;
    }

}
