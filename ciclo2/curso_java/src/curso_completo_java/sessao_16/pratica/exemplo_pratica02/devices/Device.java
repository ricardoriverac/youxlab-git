package curso_completo_java.sessao_16.pratica.exemplo_pratica02.devices;

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

    public abstract void processDoc(String doc);
}
