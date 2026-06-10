// Q4. All Permutations of a String using Recursion
// Assignment II - Array & String
// Subject: Object Oriented Programming with JAVA (MCAN-293)

public class Q4_StringPermutations {

    static class PermutationGenerator {
        public void generatePermutations(String str, int left, int right) {
            if (left == right) {
                System.out.println(str);
                return;
            }
            for (int i = left; i <= right; i++) {
                str = swap(str, left, i);
                generatePermutations(str, left + 1, right);
                str = swap(str, left, i); // backtrack
            }
        }

        private String swap(String str, int i, int j) {
            char[] arr = str.toCharArray();
            char temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            return new String(arr);
        }
    }

    public static void main(String[] args) {
        PermutationGenerator generator = new PermutationGenerator();

        String input = "XYZ";
        System.out.println("Input: \"" + input + "\"");
        System.out.println("All Permutations:");
        generator.generatePermutations(input, 0, input.length() - 1);
        // Expected: XYZ, XZY, YXZ, YZX, ZXY, ZYX
    }
}
