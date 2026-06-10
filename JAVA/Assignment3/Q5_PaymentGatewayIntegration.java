// Q5. Payment Gateway Integration - Multiple Interfaces
// Assignment III - Inheritance, Interface, Package & Exception Handling
// Subject: Object Oriented Programming with JAVA (MCAN-293)

interface UPIPayment {
    void payViaUPI(String upiId, double amount);
}

interface CardPayment {
    void payViaCard(String cardNumber, double amount);
}

class OnlinePayment implements UPIPayment, CardPayment {

    @Override
    public void payViaUPI(String upiId, double amount) {
        System.out.println("=== UPI Payment ===");
        System.out.println("UPI ID: " + upiId);
        System.out.printf("Amount: ₹%.2f%n", amount);
        System.out.println("Payment of ₹" + amount + " processed successfully via UPI!");
    }

    @Override
    public void payViaCard(String cardNumber, double amount) {
        System.out.println("=== Card Payment ===");
        // Mask card number for security
        String maskedCard = "**** **** **** " + cardNumber.substring(cardNumber.length() - 4);
        System.out.println("Card Number: " + maskedCard);
        System.out.printf("Amount: ₹%.2f%n", amount);
        System.out.println("Payment of ₹" + amount + " processed successfully via Card!");
    }
}

public class Q5_PaymentGatewayIntegration {
    public static void main(String[] args) {
        OnlinePayment payment = new OnlinePayment();

        // UPI Payment
        payment.payViaUPI("user@upi", 1500.00);

        System.out.println();

        // Card Payment
        payment.payViaCard("1234567812345678", 2500.00);
    }
}
