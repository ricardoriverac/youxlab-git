package Secao14.aula154;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class Program {
    private int roomNumber;
    private LocalDate checkIn;
    private LocalDate checkOut;
    private static final DateTimeFormatter FORMATTER = DateTimeFormatter.ofPattern("dd/MM/yyyy");

    public Program(int roomNumber, LocalDate checkIn, LocalDate checkOut) {
        if (checkOut.isBefore(checkIn) || checkOut.isEqual(checkIn)) {
            throw new IllegalArgumentException("Check-out date must be after check-in date");
        }
        this.roomNumber = roomNumber;
        this.checkIn = checkIn;
        this.checkOut = checkOut;
    }
    public void updateDates(LocalDate newCheckIn, LocalDate newCheckOut) {
        LocalDate today = LocalDate.now();

        if (newCheckIn.isBefore(today) || newCheckOut.isBefore(today)) {
            throw new IllegalArgumentException("Reservation dates for update must be future dates");
        }
        if (newCheckOut.isBefore(newCheckIn) || newCheckOut.isEqual(newCheckIn)) {
            throw new IllegalArgumentException("Check-out date must be after check-in date");
        }
        this.checkIn = newCheckIn;
        this.checkOut = newCheckOut;
    }
    @Override
    public String toString() {
        long nights = checkOut.until(checkIn).getDays() * -1;
        return String.format("Room %d, check-in: %s, check-out: %s, %d nights",
                roomNumber, checkIn.format(FORMATTER), checkOut.format(FORMATTER), nights);
    }

    public static void main(String[] args) {
        try {
            LocalDate initialCheckIn = LocalDate.parse("23/09/2019", FORMATTER);
            LocalDate initialCheckOut = LocalDate.parse("26/09/2019", FORMATTER);
            Program res = new Program(8021, initialCheckIn, initialCheckOut);
            System.out.println(res);

            LocalDate newCheckIn1 = LocalDate.parse("24/09/2015", FORMATTER);
            LocalDate newCheckOut1 = LocalDate.parse("29/09/2015", FORMATTER);
            res.updateDates(newCheckIn1, newCheckOut1);

        } catch (IllegalArgumentException e) {
            System.out.println("Error in reservation: " + e.getMessage());
        }

        try {
            LocalDate initialCheckIn = LocalDate.parse("23/09/2019", FORMATTER);
            LocalDate initialCheckOut = LocalDate.parse("26/09/2019", FORMATTER);
            Program res = new Program(8021, initialCheckIn, initialCheckOut);
            System.out.println(res);

            LocalDate newCheckIn2 = LocalDate.parse("24/09/2020", FORMATTER);
            LocalDate newCheckOut2 = LocalDate.parse("22/09/2020", FORMATTER);
            res.updateDates(newCheckIn2, newCheckOut2);

        } catch (IllegalArgumentException e) {
            System.out.println("Error in reservation: " + e.getMessage());
        }
    }
}

