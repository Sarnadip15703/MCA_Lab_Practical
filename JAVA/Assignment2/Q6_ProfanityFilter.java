// Q6. Replace Profanity in Text
// Assignment II - Array & String
// Subject: Object Oriented Programming with JAVA (MCAN-293)

public class Q6_ProfanityFilter {

    static class TextFilter {
        private String[] badWords;

        public TextFilter(String[] badWords) {
            this.badWords = badWords;
        }

        public String filterText(String text) {
            for (String badWord : badWords) {
                // Case-insensitive replacement
                text = text.replaceAll("(?i)" + badWord, "***");
            }
            return text;
        }
    }

    public static void main(String[] args) {
        String[] badWords = {"bad", "ugly", "stupid"};
        TextFilter filter = new TextFilter(badWords);

        String inputText = "This is a bad and ugly comment.";
        System.out.println("Bad Words List: \"bad\", \"ugly\", \"stupid\"");
        System.out.println("Input: " + inputText);
        System.out.println("Output: " + filter.filterText(inputText));
        // Expected: This is a *** and *** comment.
    }
}
