package com.example.desafioJoao.enums;

public enum BetStatus {
    IN_PROGRESS("in_progress"),
    LOST("lost"),
    WON("won");
    private String status;

    BetStatus(String status){
        this.status = status;
    }

    public String getStatus() {
        return status;
    }
}
