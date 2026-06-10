// Q7. Travel Booking System - Package: travel.bookings
// Assignment III - Inheritance, Interface, Package & Exception Handling
// Subject: Object Oriented Programming with JAVA (MCAN-293)

package travel.bookings;

import travel.flights.Flight;
import travel.hotels.Hotel;

public class Booking {
    public void bookFlight(Flight f) {
        System.out.println("=== Flight Booking Confirmed ===");
        System.out.println(f.getDetails());
        System.out.println("Status: BOOKED");
        System.out.println();
    }

    public void bookHotel(Hotel h) {
        System.out.println("=== Hotel Booking Confirmed ===");
        System.out.println(h.getDetails());
        System.out.println("Status: BOOKED");
        System.out.println();
    }
}
