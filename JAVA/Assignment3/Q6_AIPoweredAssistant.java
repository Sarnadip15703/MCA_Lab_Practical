// Q6. AI-Powered Assistant - Multiple Interfaces
// Assignment III - Inheritance, Interface, Package & Exception Handling
// Subject: Object Oriented Programming with JAVA (MCAN-293)

interface Speaker {
    void speak(String text);
}

interface Translator {
    void translate(String text, String language);
}

class AIAssistant implements Speaker, Translator {
    private String assistantName;

    public AIAssistant(String assistantName) {
        this.assistantName = assistantName;
    }

    @Override
    public void speak(String text) {
        System.out.println("=== Speech Synthesis ===");
        System.out.println(assistantName + " is speaking: \"" + text + "\"");
        System.out.println("[Audio output generated for: \"" + text + "\"]");
    }

    @Override
    public void translate(String text, String language) {
        System.out.println("=== Language Translation ===");
        System.out.println("Original Text: \"" + text + "\"");
        System.out.println("Target Language: " + language);
        // Simulated translation
        System.out.println(assistantName + " translated text to " + language + ": \"[Translated: " + text + "]\"");
    }
}

public class Q6_AIPoweredAssistant {
    public static void main(String[] args) {
        AIAssistant assistant = new AIAssistant("Aria");

        // Demonstrate speaking
        assistant.speak("Hello! How can I assist you today?");

        System.out.println();

        // Demonstrate translation
        assistant.translate("Good morning, have a great day!", "Hindi");

        System.out.println();

        // Demonstrate both together
        String textToTranslateAndSpeak = "Welcome to the future of AI!";
        assistant.translate(textToTranslateAndSpeak, "French");
        assistant.speak(textToTranslateAndSpeak);
    }
}
