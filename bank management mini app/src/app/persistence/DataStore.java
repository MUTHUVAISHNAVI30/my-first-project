package app.persistence;

import app.model.Customer;
import app.model.Account;
import java.util.ArrayList;
import java.util.List;

public class DataStore {
    public static List<Customer> customers = new ArrayList<>();
    public static List<Account> accounts = new ArrayList<>();

    static {
    Customer c1 = new Customer("Muthu Vaishnavi", "0030");
    Account a1 = new Account("0030");
    a1.deposit(100000);
    customers.add(c1);
    accounts.add(a1);

    // Admin 2
    Customer c2 = new Customer("Jenifer Beula", "0010");
    Account a2 = new Account("0010");
    a2.deposit(100000);
    customers.add(c2);
    accounts.add(a2);

    // Admin 3
    Customer c3 = new Customer("Tamilvani", "0090");
    Account a3 = new Account("0090");
    a3.deposit(100000);
    customers.add(c3);
    accounts.add(a3);
      
    }
}
