package app;

import app.view.LoginFrame;

public class Main {
    public static void main(String[] args) {
        // Launch the Login Window on the Event Dispatch Thread
        javax.swing.SwingUtilities.invokeLater(() -> {
            new LoginFrame().setVisible(true);
        });
    }
}
