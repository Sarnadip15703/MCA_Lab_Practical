import java.util.*;


class RunwayController {
    public synchronized void requestTakeoff(String flightName) {
        System.out.println(flightName + " taking off...");
        try {
            Thread.sleep(1000); 
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        System.out.println(flightName + " took off. Runway free.\n");
    }
}

class Flight extends Thread {
    RunwayController controller;
    String name;
    int priority; 
    Flight(String name, int priority, RunwayController controller) {
        this.name = name;
        this.priority = priority;
        this.controller = controller;
    }

    public void run() {
        controller.requestTakeoff(name);
    }
}

public class Runway1 {
    public static void main(String[] args) throws InterruptedException {
        RunwayController controller = new RunwayController();

        List<Flight> flights = new ArrayList<>();
        flights.add(new Flight("AI 211", 3, controller));
        flights.add(new Flight("UK 2344", 2, controller));
        flights.add(new Flight("AI 2333", 1, controller));
        flights.add(new Flight("IG 294", 2, controller));

        
        flights.sort((a, b) -> a.priority - b.priority);

        
        for (Flight f : flights) {
            f.start();
            f.join();
        }
    }
}
