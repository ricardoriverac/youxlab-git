package exception.entities;

import exception.exception.DomainException;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.concurrent.TimeUnit;

public class Reserva {
    private Integer numeroQuarto;
    private Date checkIn;
    private Date checkOut;

    private static SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");

    public Reserva(Integer numeroQuarto, Date checkIn, Date checkOut) {
        this.numeroQuarto = numeroQuarto;
        this.checkIn = checkIn;
        this.checkOut = checkOut;
    }

    public Integer getNumeroQuarto(){
        return numeroQuarto;
    }

    public void setNumeroQuarto(Integer numeroQuarto) {
        this.numeroQuarto = numeroQuarto;
    }

    public Date getCheckOut() {
        return checkOut;
    }

    public Date getCheckIn() {
        return checkIn;
    }

    public long duracao(){
        long diferenca = checkOut.getTime() - checkIn.getTime();
        return TimeUnit.DAYS.convert(diferenca, TimeUnit.MILLISECONDS);
    }

    public void atualizarData(Date checkIn, Date checkOut){
        Date now = new Date();
        if(checkIn.before(now) || checkOut.before(now)){
            throw new DomainException("As datas de reserva para atualização devem ser datas futuras");
        }
        if(!checkOut.after(checkIn)){
            throw new DomainException("A data de check-out deve ser posterior à data de check-in");
        }
        this.checkIn = checkIn;
        this.checkOut = checkOut;
    }

    @Override
    public String toString() {
        return "Quarto: " + numeroQuarto + ", " + "check-in: " + sdf.format(checkIn) + ", check-out: " + sdf.format(checkOut) + ", " + duracao() + " noites";
    }
}
