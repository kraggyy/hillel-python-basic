public class Main {

    public static void main(String[] args) {
        int[] arr = {1, 3, 3, 5, 6, 7, 11, 20};
        boolean result1 = isIncreasing(arr);
        System.out.println(result1);
        System.out.println("-".repeat(50));
        boolean result3 = canSplitArray(arr);
        System.out.println(result3);
        System.out.println("-".repeat(50));
        fizzBuzz();
    }

    public static boolean isIncreasing(int[] arr) {
        if (arr.length < 2) {
            return false; 
        }

        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < arr[i - 1]) {
                return false;
            }
        }

        return true; 
    }

    public static void fizzBuzz() {
        for (int i = 1; i <= 100; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println("FizzBuzz");
            } else if (i % 3 == 0) {
                System.out.println("Fizz");
            } else if (i % 5 == 0) {
                System.out.println("Buzz");
            } else {
                System.out.println(i);
            }
        }
    }

    public static boolean canSplitArray(int[] arr) {
        if (arr.length < 2) {
            return false;
        }

        int totalSum = 0;
        for (int num : arr) {
            totalSum += num;
        }

        int leftSum = 0;
        for (int i = 0; i < arr.length - 1; i++) {
            leftSum += arr[i];
            if (leftSum == totalSum - leftSum) {
                return true; 
            }
        }

        return false;
    }
}