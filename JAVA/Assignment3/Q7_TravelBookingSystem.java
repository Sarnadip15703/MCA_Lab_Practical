// Q7. Travel Booking System - Main Class
// Assignment III - Inheritance, Interface, Package & Exception Handling
// Subject: Object Oriented Programming with JAVA (MCAN-293)
//
// To compile and run:
//   javac travel/flights/Flight.java travel/hotels/Hotel.java travel/bookings/Booking.java Q7_TravelBookingSystem.java
//   java Q7_TravelBookingSystem

import travel.flights.Flight;
import travel.hotels.Hotel;
import travel.bookings.Booking;

public class Q7_TravelBookingSystem {
    public static void main(String[] args) {
        // Create flight and hotel objects
        Flight flight = new Flight("AI-202", "New York", 450.00);
        Hotel hotel = new Hotel("Grand Hyatt", "New York, USA", 200.00);
        Booking booking = new Booking();

        // Book flight and hotel
        booking.bookFlight(flight);
        booking.bookHotel(hotel);

        System.out.println("Total Cost: $" + (flight.getPrice() + hotel.getPrice()));
    }
}
