import javax.swing.*;
import java.awt.*;  // Adicionando importação para o layout manual
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class IMCCalculator {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Calculadora de IMC");
        frame.setSize(300, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(null);

        JLabel labelPeso = new JLabel("Peso (Kg):");
        labelPeso.setBounds(10, 10, 80, 25);
        frame.add(labelPeso);

        JTextField campoPeso = new JTextField();
        campoPeso.setBounds(100, 10, 150, 25);
        frame.add(campoPeso);

        JLabel labelAltura = new JLabel("Altura (Cm):");
        labelAltura.setBounds(10, 40, 80, 25);
        frame.add(labelAltura);

        JTextField campoAltura = new JTextField();
        campoAltura.setBounds(100, 40, 150, 25);
        frame.add(campoAltura);

        JButton botaoCalcular = new JButton("Calcular IMC");
        botaoCalcular.setBounds(80, 70, 120, 30);
        frame.add(botaoCalcular);

        JLabel resultadoLabel = new JLabel("Resultado: ");
        resultadoLabel.setBounds(10, 110, 250, 25);
        frame.add(resultadoLabel);

        botaoCalcular.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    double peso = Double.parseDouble(campoPeso.getText().replace(",", "."));
                    double altura = Double.parseDouble(campoAltura.getText().replace(",", ".")) / 100;
                    double imc = peso / (altura * altura);

                    String classificacao;
                    if (imc < 18.5) {
                        classificacao = "Abaixo do peso";
                    } else if (imc < 24.9) {
                        classificacao = "Peso normal";
                    } else if (imc < 29.9) {
                        classificacao = "Sobrepeso";
                    } else {
                        classificacao = "Obesidade";
                    }

                    resultadoLabel.setText(String.format("IMC: %.2f (%s)", imc, classificacao));
                } catch (NumberFormatException ex) {
                    resultadoLabel.setText("Valores inválidos!");
                }
            }
        });

        frame.setLocationRelativeTo(null); // Centralizar na tela
        frame.setVisible(true);
    }
}
