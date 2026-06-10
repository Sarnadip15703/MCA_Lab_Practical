// Q10. Extract Domain from URL
// Assignment II - Array & String
// Subject: Object Oriented Programming with JAVA (MCAN-293)

import java.util.Scanner;

public class Q10_ExtractDomain {

    static class DomainExtractor {
        public String extractDomain(String url) {
            // Remove protocol (http://, https://)
            String domain = url.replaceAll("https?://", "");
            // Remove www.
            domain = domain.replaceAll("^www\\.", "");
            // Remove path after domain
            int slashIndex = domain.indexOf('/');
            if (slashIndex != -1) {
                domain = domain.substring(0, slashIndex);
            }
            // Remove query params if any
            int queryIndex = domain.indexOf('?');
            if (queryIndex != -1) {
                domain = domain.substring(0, queryIndex);
            }
            return domain;
        }
    }

    public static void main(String[] args) {
        DomainExtractor extractor = new DomainExtractor();
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter URL: ");
        String url = scanner.nextLine();
        System.out.println("Domain: " + extractor.extractDomain(url));

        scanner.close();

        // Test case
        System.out.println("\n--- Test Case ---");
        String testUrl = "https://www.google.com/search?q=java";
        System.out.println("Input: " + testUrl);
        System.out.println("Domain: " + extractor.extractDomain(testUrl));
        // Expected: google.com
    }
}
