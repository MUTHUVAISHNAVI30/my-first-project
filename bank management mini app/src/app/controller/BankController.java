package app.controller;

import app.model.Account;
import app.persistence.DataStore;

public class BankController 
{
    public boolean validateLogin(String username, String password) {
        // Admin 1
        if(username.equals("Muthu Vaishnavi") && password.equals("0030")) return true;
        // Admin 2
        if(username.equals("Jenifer Beula") && password.equals("0010")) return true;
        // Admin 3
        if(username.equals("Tamilvani") && password.equals("0090")) return true;

        return false; // invalid login
    }
   
    

    public boolean deposit(String accountNumber, double amount) {
        for(Account a : DataStore.accounts) {
            if(a.getAccountNumber().equals(accountNumber)) {
                return a.withdraw(amount);
            }
        }
        return false;
    }

    public boolean withdraw(String accountNumber, double amount) {
        for(Account a : DataStore.accounts) {
            if(a.getAccountNumber().equals(accountNumber)) {
                return a.withdraw(amount);
            }
        }
        return false;
    }

    public double getBalance(String accountNumber) {
        for(Account a : DataStore.accounts) {
            if(a.getAccountNumber().equals(accountNumber)) {
                return a.getBalance();
            }
        }
        return -1; // account not found
    }
}
