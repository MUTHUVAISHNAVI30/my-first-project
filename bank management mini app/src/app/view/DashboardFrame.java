package app.view;

import javax.swing.*;
import java.awt.*;
import app.controller.BankController;

public class DashboardFrame extends JFrame {
    private BankController controller;

    public DashboardFrame() {
        controller = new BankController();

        setTitle("Bank Dashboard");
        setSize(500, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new GridLayout(5, 1, 10, 10));

        JLabel welcomeLabel = new JLabel("Welcome to Bank Management System", SwingConstants.CENTER);
        add(welcomeLabel);

        JButton depositButton = new JButton("Deposit");
        JButton withdrawButton = new JButton("Withdraw");
        JButton viewBalanceButton = new JButton("View Balance");
        JButton exitButton = new JButton("Exit");

        add(depositButton);
        add(withdrawButton);
        add(viewBalanceButton);
        add(exitButton);

        depositButton.addActionListener(e -> deposit());
        withdrawButton.addActionListener(e -> withdraw());
        viewBalanceButton.addActionListener(e -> viewBalance());
        exitButton.addActionListener(e -> System.exit(0));
    }

    private void deposit() {
        String acc = JOptionPane.showInputDialog(this, "Enter Account Number:");
        String amtStr = JOptionPane.showInputDialog(this, "Enter Amount to Deposit:");
        double amount = Double.parseDouble(amtStr);

        if(controller.deposit(acc, amount)) {
            JOptionPane.showMessageDialog(this, "Amount deposited successfully!");
        } else {
            JOptionPane.showMessageDialog(this, "Account not found!");
        }
    }

    private void withdraw() {
        String acc = JOptionPane.showInputDialog(this, "Enter Account Number:");
        String amtStr = JOptionPane.showInputDialog(this, "Enter Amount to Withdraw:");
        double amount = Double.parseDouble(amtStr);

        if(controller.withdraw(acc, amount)) {
            JOptionPane.showMessageDialog(this, "Withdrawal successful!");
        } else {
            JOptionPane.showMessageDialog(this, "Insufficient balance or account not found!");
        }
    }

    private void viewBalance() {
        String acc = JOptionPane.showInputDialog(this, "Enter Account Number:");
        double balance = controller.getBalance(acc);
        if(balance >= 0) {
            JOptionPane.showMessageDialog(this, "Balance: " + balance);
        } else {
            JOptionPane.showMessageDialog(this, "Account not found!");
        }
    }
}
