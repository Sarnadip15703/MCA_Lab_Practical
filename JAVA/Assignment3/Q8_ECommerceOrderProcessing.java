// Q8. E-Commerce Order Processing - Custom Exception Handling
// Assignment III - Inheritance, Interface, Package & Exception Handling
// Subject: Object Oriented Programming with JAVA (MCAN-293)

// Custom Exception
class OutOfStockException extends Exception {
    public OutOfStockException(String message) {
        super(message);
    }
}

class Product {
    private String name;
    private int stock;

    public Product(String name, int stock) {
        this.name = name;
        this.stock = stock;
    }

    public String getName() { return name; }
    public int getStock() { return stock; }

    public void purchase(int quantity) throws OutOfStockException {
        if (quantity > stock) {
            throw new OutOfStockException(
                "OutOfStockException: Cannot purchase " + quantity +
                " unit(s) of \"" + name + "\". Only " + stock + " unit(s) available in stock."
            );
        }
        stock -= quantity;
        System.out.println("Purchase Successful! " + quantity + " unit(s) of \"" + name + "\" purchased.");
        System.out.println("Remaining Stock: " + stock);
    }
}

public class Q8_ECommerceOrderProcessing {
    public static void main(String[] args) {
        Product laptop = new Product("Laptop", 3);

        System.out.println("=== E-Commerce Order Processing ===");
        System.out.println("Product: " + laptop.getName());
        System.out.println("Available Stock: " + laptop.getStock());
        System.out.println();

        // Successful purchase
        try {
            System.out.println("Attempting to purchase 2 unit(s)...");
            laptop.purchase(2);
        } catch (OutOfStockException e) {
            System.out.println(e.getMessage());
        }

        System.out.println();

        // Out of stock scenario
        try {
            System.out.println("Attempting to purchase 5 unit(s)...");
            laptop.purchase(5);
        } catch (OutOfStockException e) {
            System.out.println(e.getMessage());
            System.out.println("Order Failed! Please try again later.");
        } finally {
            System.out.println("Order processing complete.");
        }
    }
}
