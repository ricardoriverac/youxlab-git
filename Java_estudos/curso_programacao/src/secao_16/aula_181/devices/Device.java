package secao_16.aula_181.devices;

public abstract class Device {

    public String serialNumber;

    public Device(String serialNumber) {
        this.serialNumber = serialNumber;
    }

    public String getSerialNumber() {
        return serialNumber;
    }

    public void setSerialNumber(String serialNumber) {
        this.serialNumber = serialNumber;
    }

    public abstract void print(String doc);

    public abstract void processDoc(String doc);
}