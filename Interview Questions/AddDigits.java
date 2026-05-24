import java.util.Scanner;

public class AddDigits {
    private static int sumOfDigits(int n){
        int sum = 0;
        while(n > 0) {
            sum += n %  10;
            n /= 10;
        }
        return sum;
    }

    public static int findDigitalRoot(int n) {
        while (n >= 10) {
            n = sumOfDigits(n);
        }
        return n;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        sc.close();

        int results = findDigitalRoot(n);
        System.out.println(results);

            
    }

}
