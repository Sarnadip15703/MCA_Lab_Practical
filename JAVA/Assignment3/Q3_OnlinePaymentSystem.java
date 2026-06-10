// Q3. Online Payment System - Abstract Class
// Assignment III - Inheritance, Interface, Package & Exception Handling
// Subject: Object Oriented Programming with JAVA (MCAN-293)

abstract class Payment {
    protected String transactionId;
    protected double amount;

    public Payment(String transactionId, double amount) {
        this.transactionId = transactionId;
        this.amount = amount;
    }

    public abstract void processPayment();

    public void displayTransaction() {
        System.out.println("Transaction ID: " + transactionId);
        System.out.println("Amount: $" + amount);
    }
}

class CreditCardPayment extends Payment {
    private static final double TRANSACTION_FEE = 0.02; // 2%

    public CreditCardPayment(String transactionId, double amount) {
        super(transactionId, amount);
    }

    @Override
    public void processPayment() {
        double fee = amount * TRANSACTION_FEE;
        double total = amount + fee;
        System.out.println("=== Credit Card Payment ===");
        displayTransaction();
        System.out.printf("Transaction Fee (2%%): $%.2f%n", fee);
        System.out.printf("Total Charged: $%.2f%n", total);
        System.out.println("Payment Processed Successfully via Credit Card!");
    }
}

class PayPalPayment extends Payment {
    private static final double TRANSACTION_FEE = 0.03; // 3%

    public PayPalPayment(String transactionId, double amount) {
        super(transactionId, amount);
    }

    @Override
    public void processPayment() {
        double fee = amount * TRANSACTION_FEE;
        double total = amount + fee;
        System.out.println("=== PayPal Payment ===");
        displayTransaction();
        System.out.printf("Transaction Fee (3%%): $%.2f%n", fee);
        System.out.printf("Total Charged: $%.2f%n", total);
        System.out.println("Payment Processed Successfully via PayPal!");
    }
}

public class Q3_OnlinePaymentSystem {
    public static void main(String[] args) {
        Payment creditCard = new CreditCardPayment("TXN001", 500.00);
        creditCard.processPayment();

        System.out.println();

        Payment paypal = new PayPalPayment("TXN002", 300.00);
        paypal.processPayment();
    }
}
