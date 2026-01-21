package GenericsSetMap.Set.ProblemaExemplo.entities;

import java.util.Date;
import java.util.Objects;

public class LogEntry {

    private String userName;
    private Date dateMoment;

    public LogEntry(String userName, Date dateMoment) {
        this.userName = userName;
        this.dateMoment = dateMoment;
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public Date getDateMoment() {
        return dateMoment;
    }

    public void setDateMoment(Date dateMoment) {
        this.dateMoment = dateMoment;
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        LogEntry logEntry = (LogEntry) o;
        return Objects.equals(userName, logEntry.userName);
    }

    @Override
    public int hashCode() {
        return Objects.hashCode(userName);
    }
}
