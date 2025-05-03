public class Guitarra {
    private String modelo;
    private String fabricante;
    private double preco;

    // Construtor
    public Guitarra(String modelo, String fabricante, double preco) {
        this.modelo = modelo;
        this.fabricante = fabricante;
        this.preco = preco;
    }

    // Métodos getters e setters
    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public String getFabricante() {
        return fabricante;
    }

    public void setFabricante(String fabricante) {
        this.fabricante = fabricante;
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }

    // Método para exibir detalhes da guitarra
    public void mostrarDetalhes() {
        System.out.println("Modelo: " + modelo);
        System.out.println("Fabricante: " + fabricante);
        System.out.println("Preço: R$" + preco);
    }

    // Método principal para testar a classe
    public static void main(String[] args) {
        Guitarra minhaGuitarra = new Guitarra("Stratocaster", "Fender", 8500.00);
        minhaGuitarra.mostrarDetalhes();
    }
}
