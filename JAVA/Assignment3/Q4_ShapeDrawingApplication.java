// Q4. Shape Drawing Application - Abstract Class
// Assignment III - Inheritance, Interface, Package & Exception Handling
// Subject: Object Oriented Programming with JAVA (MCAN-293)

abstract class Shape {
    protected String color;

    public Shape(String color) {
        this.color = color;
    }

    public abstract double calculateArea();
    public abstract void draw();
}

class Circle extends Shape {
    private double radius;

    public Circle(String color, double radius) {
        super(color);
        this.radius = radius;
    }

    @Override
    public double calculateArea() {
        return Math.PI * radius * radius;
    }

    @Override
    public void draw() {
        System.out.println("Drawing a " + color + " Circle with radius: " + radius);
        System.out.printf("Area = π * r² = π * %.1f² = %.2f%n", radius, calculateArea());
    }
}

class Rectangle extends Shape {
    private double length;
    private double breadth;

    public Rectangle(String color, double length, double breadth) {
        super(color);
        this.length = length;
        this.breadth = breadth;
    }

    @Override
    public double calculateArea() {
        return length * breadth;
    }

    @Override
    public void draw() {
        System.out.println("Drawing a " + color + " Rectangle with length: " + length + " and breadth: " + breadth);
        System.out.printf("Area = length * breadth = %.1f * %.1f = %.2f%n", length, breadth, calculateArea());
    }
}

public class Q4_ShapeDrawingApplication {
    public static void main(String[] args) {
        Shape circle = new Circle("Red", 5.0);
        System.out.println("=== Circle ===");
        circle.draw();

        System.out.println();

        Shape rectangle = new Rectangle("Blue", 8.0, 4.0);
        System.out.println("=== Rectangle ===");
        rectangle.draw();
    }
}
