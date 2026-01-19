package Secao_8.Exercicio_3.application;

public class Student {
    public double firstGrade;
    public double secondGrade;
    public double thirdGrade;
    public double finalGrade() {
        return firstGrade+secondGrade+thirdGrade;
    };
    public String result (double FinalGrade) {
        if (FinalGrade>=60) {
            return System.out.printf("FINAL GRADE = %.2f%nPASS", FinalGrade).toString();
        } else {
            return System.out.printf("FINAL GRADE = %.2f%nFAILED%nMISSING %.2f", FinalGrade, Math.abs(FinalGrade-60)).toString();
        }
    };
}
