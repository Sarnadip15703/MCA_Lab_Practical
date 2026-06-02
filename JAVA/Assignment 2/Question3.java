// import java.util.Scanner;

interface FitnessTracker {
    int stepsCount = 15;
    default void countSteps(){
        System.out.println("Fitness Tracker");
    }
   // void test();
    void calculateCalories();
}

interface NotificationReceiver {
    String notificationMessage="Fitness..";
    void receiveNotification();
    void displayNotification();
}

class SmartWatch implements FitnessTracker, NotificationReceiver{
    String watchBrand, model;
    SmartWatch(String w, String m){
        watchBrand = w;
        model = m;
    }

    void showTime(){
        System.out.println("Show time");
    }

    @Override
    public void receiveNotification() {
        System.out.println("Received notification: " + notificationMessage);
    }

    @Override
    public void displayNotification() {
        System.out.println("Displaying notification: " + notificationMessage);
    }

    @Override
    public void countSteps() {
        //System.out.println("Counting steps: " + stepsCount);
    }

    @Override
    public void calculateCalories() {
        System.out.println("Calculating calories...");
    }
}

class A implements FitnessTracker{
    @Override
    public void calculateCalories() {
        System.out.println("Calculating calories in class A...");
    }

    // void test(){
        //System.out.println("Test method in class A");
   // }

}

public class Question3{
    public static void main(String[] args) {
        SmartWatch watch = new SmartWatch("Apple", "Watch");
        watch.showTime();
        watch.countSteps();
        watch.calculateCalories();
        watch.receiveNotification();
        watch.displayNotification();
    }
}