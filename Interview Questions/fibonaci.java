import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class fibonaci {
    public static List<Integer> fibonacci(int n) {
        int num1 = 0;
        int num2 = 1;

        List<Integer> series = new ArrayList<>();

        for (int i = 0; i<n; i++){
            series.add(num1);
            int temp = num1;
            num1 = num2;
            num2 = temp + num2;
        }
        return series;
        
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        List<Integer> series = fibonacci(n);
        System.out.println(series);
        sc.close();
    }
}
    

