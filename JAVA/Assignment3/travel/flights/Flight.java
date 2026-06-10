// Q7. Travel Booking System - Package: travel.flights
// Assignment III - Inheritance, Interface, Package & Exception Handling
// Subject: Object Oriented Programming with JAVA (MCAN-293)

package travel.flights;

public class Flight {
    private String flightNumber;
    private String destination;
    private double price;

    public Flight(String flightNumber, String destination, double price) {
        this.flightNumber = flightNumber;
        this.destination = destination;
        this.price = price;
    }

    public String getFlightNumber() { return flightNumber; }
    public String getDestination() { return destination; }
    public double getPrice() { return price; }

    public String getDetails() {
        return "Flight Number: " + flightNumber +
               "\nDestination: " + destination +
               "\nPrice: $" + price;
    }
}
