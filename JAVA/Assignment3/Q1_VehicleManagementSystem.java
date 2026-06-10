// Q1. Vehicle Management System - Multilevel Inheritance
// Assignment III - Inheritance, Interface, Package & Exception Handling
// Subject: Object Oriented Programming with JAVA (MCAN-293)

class Vehicle {
    protected String brand;
    protected String model;
    protected int year;

    public Vehicle(String brand, String model, int year) {
        this.brand = brand;
        this.model = model;
        this.year = year;
    }

    public void displayDetails() {
        System.out.println("Brand: " + brand);
        System.out.println("Model: " + model);
        System.out.println("Year: " + year);
    }
}

class Car extends Vehicle {
    protected String fuelType;

    public Car(String brand, String model, int year, String fuelType) {
        super(brand, model, year);
        this.fuelType = fuelType;
    }

    @Override
    public void displayDetails() {
        super.displayDetails();
        System.out.println("Fuel Type: " + fuelType);
    }
}

class LuxuryCar extends Car {
    private String feature;

    public LuxuryCar(String brand, String model, int year, String fuelType, String feature) {
        super(brand, model, year, fuelType);
        this.feature = feature;
    }

    @Override
    public void displayDetails() {
        super.displayDetails();
        System.out.println("Feature: " + feature);
    }
}

public class Q1_VehicleManagementSystem {
    public static void main(String[] args) {
        LuxuryCar luxuryCar = new LuxuryCar("Tesla", "Model S", 2023, "Electric", "Autopilot");
        System.out.println("=== Luxury Car Details ===");
        luxuryCar.displayDetails();
        // Expected Output:
        // Brand: Tesla
        // Model: Model S
        // Year: 2023
        // Fuel Type: Electric
        // Feature: Autopilot
    }
}
