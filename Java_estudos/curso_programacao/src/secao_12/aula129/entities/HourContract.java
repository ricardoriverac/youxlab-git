package secao_12.aula129.entities;

import javax.xml.crypto.Data;
import java.util.Date;

public class HourContract {
    private Date date;
    private Double valuePerhour;
    private Integer hours;

    public HourContract(){

    }

    public HourContract(Date date, int hours, double valuePerhour) {
        this.date = (Date) date;
        this.hours = hours;
        this.valuePerhour = valuePerhour;
    }


    public Date getDate() {
        return date;
    }


    public void setDate(Date date) {
        this.date = date;
    }


    public Double getValuePerhour() {
        return valuePerhour;
    }


    public void setValuePerhour(Double valuePerhour) {
        this.valuePerhour = valuePerhour;
    }


    public Integer getHours() {
        return hours;
    }


    public void setHours(Integer hours) {
        this.hours = hours;
    }


    public void add(HourContract contract) {

    }


    public double totalValue(){
        return valuePerhour * hours;


    }
}
