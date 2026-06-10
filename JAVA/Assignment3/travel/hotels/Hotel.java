// Q7. Travel Booking System - Package: travel.hotels
// Assignment III - Inheritance, Interface, Package & Exception Handling
// Subject: Object Oriented Programming with JAVA (MCAN-293)

package travel.hotels;

public class Hotel {
    private String hotelName;
    private String location;
    private double price;

    public Hotel(String hotelName, String location, double price) {
        this.hotelName = hotelName;
        this.location = location;
        this.price = price;
    }

    public String getHotelName() { return hotelName; }
    public String getLocation() { return location; }
    public double getPrice() { return price; }

    public String getDetails() {
        return "Hotel Name: " + hotelName +
               "\nLocation: " + location +
               "\nPrice per Night: $" + price;
    }
}
