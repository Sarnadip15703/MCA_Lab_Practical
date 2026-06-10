// Q2. Online Shopping System - Multilevel Inheritance
// Assignment III - Inheritance, Interface, Package & Exception Handling
// Subject: Object Oriented Programming with JAVA (MCAN-293)

class Product {
    protected String productName;
    protected double price;

    public Product(String productName, double price) {
        this.productName = productName;
        this.price = price;
    }

    public void displayDetails() {
        System.out.println("Product Name: " + productName);
        System.out.println("Price: $" + price);
    }
}

class Electronics extends Product {
    protected String warrantyPeriod;

    public Electronics(String productName, double price, String warrantyPeriod) {
        super(productName, price);
        this.warrantyPeriod = warrantyPeriod;
    }

    @Override
    public void displayDetails() {
        super.displayDetails();
        System.out.println("Warranty: " + warrantyPeriod);
    }
}

class Smartphone extends Electronics {
    private String batteryLife;

    public Smartphone(String productName, double price, String warrantyPeriod, String batteryLife) {
        super(productName, price, warrantyPeriod);
        this.batteryLife = batteryLife;
    }

    @Override
    public void displayDetails() {
        super.displayDetails();
        System.out.println("Battery Life: " + batteryLife);
    }
}

public class Q2_OnlineShoppingSystem {
    public static void main(String[] args) {
        Smartphone smartphone = new Smartphone("iPhone 14", 999, "1 year", "20 hours");
        System.out.println("=== Smartphone Details ===");
        smartphone.displayDetails();
        // Expected Output:
        // Product Name: iPhone 14
        // Price: $999.0
        // Warranty: 1 year
        // Battery Life: 20 hours
    }
}
