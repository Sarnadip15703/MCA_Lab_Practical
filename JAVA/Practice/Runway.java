import java.util.concurrent.PriorityBlockingQueue;
import java.util.concurrent.TimeUnit;
 

class RunwayController {
    
    public synchronized void requestTakeoff(String flightName) {
        System.out.println(flightName + " is lined up on the runway...");
        try {
            Thread.sleep(1000); 
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        System.out.println(flightName + " has taken off. Runway clear.\n");
    }
}
 
class Flight extends Thread {
    private final RunwayController controller;
    private final String flightName;
 
    public Flight(String flightName, RunwayController controller) {
        super(flightName);
        this.flightName = flightName;
        this.controller = controller;
    }
 
    @Override
    public void run() {
        System.out.println(flightName + " requesting takeoff clearance...");
        controller.requestTakeoff(flightName);
    }
}
 

class PriorityFlightRequest implements Comparable<PriorityFlightRequest> {
    final String name;
    final int priority;
 
    PriorityFlightRequest(String name, int priority) {
        this.name = name;
        this.priority = priority;
    }
 
    @Override
    public int compareTo(PriorityFlightRequest other) {
        return Integer.compare(this.priority, other.priority);
    }
}
 
class ControlTower {
    private final RunwayController runway = new RunwayController();
    private final PriorityBlockingQueue<PriorityFlightRequest> queue = new PriorityBlockingQueue<>();
    private volatile boolean acceptingRequests = true;
 
    public void submitRequest(String flightName, int priority) {
        PriorityFlightRequest req = new PriorityFlightRequest(flightName, priority);
        queue.put(req);
        System.out.println(flightName + " queued with priority " + priority);
    }
 
    public Thread startDispatcher() {
        Thread dispatcher = new Thread(() -> {
            while (acceptingRequests || !queue.isEmpty()) {
                try {
                    PriorityFlightRequest next = queue.poll(500, TimeUnit.MILLISECONDS);
                    if (next != null) {
                        runway.requestTakeoff(next.name);
                    }
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            }
        }, "Tower-Dispatcher");
        dispatcher.start();
        return dispatcher;
    }
 
    public void stopAcceptingRequests() {
        acceptingRequests = false;
    }
}
 

public class Runway {
    public static void main(String[] args) throws InterruptedException {
 
        System.out.println("===== FCFS / Queue-based takeoff =====\n");
        RunwayController controller = new RunwayController();
        Flight f1 = new Flight("IndiGo-101", controller);
        Flight f2 = new Flight("AirIndia-202", controller);
        Flight f3 = new Flight("SpiceJet-303", controller);
 
        f1.start();
        f2.start();
        f3.start();
        f1.join();
        f2.join();
        f3.join();
 
        System.out.println("===== Priority-based takeoff =====\n");
        ControlTower tower = new ControlTower();
        Thread dispatcher = tower.startDispatcher();
 
       
        tower.submitRequest("Cargo-501", 3);
        tower.submitRequest("Commercial-202", 2);
        tower.submitRequest("Emergency-911", 1); 
        tower.submitRequest("Commercial-303", 2);
 
        Thread.sleep(500);
        tower.stopAcceptingRequests();
        dispatcher.join();
    }
}
 