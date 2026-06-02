import java.util.Scanner;

public class array {
    public static void main(String[] args) {
        System.out.println("Entered 3x3 matrix:");
        int[][] matrix = MatrixHelper.getInput();
        MatrixHelper.printMatrix(matrix);
        System.out.println();
        MatrixHelper.print2D(matrix);
    }
}

class MatrixHelper {
    public static int[][] getInput() {
        Scanner scanner = new Scanner(System.in);
        int[][] matrix = new int[3][3];
        System.out.println("Enter 9 integers for a 3x3 array:");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                matrix[i][j] = scanner.nextInt();
            }
        }
        return matrix;
    }

    public static void printMatrix(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static void print2D(int[][] matrix){
        for (int a = 0; a < matrix.length-1; a++) {
            for (int i = a; i < 2+a; i++) {
                for (int j = 0; j < 2; j++) {
                    System.out.print(matrix[i][j] + " ");
                }
                System.out.println();
            }
            System.out.println();
        }

        for (int a = 0; a < matrix.length-1; a++) {
            for (int i = a; i < 2+a; i++) {
                for (int j = 1; j < 2+a; j++) {
                    System.out.print(matrix[i][j] + " ");
                }
                System.out.println();
            }
            System.out.println();
        }
    }

}

