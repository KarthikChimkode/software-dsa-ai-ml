import java.util.*;
import java.text.*;

public class Solution {
    
   public static void main(String[] args) {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
    Scanner scan = new Scanner(System.in);
    double n = scan.nextDouble();
    String us = NumberFormat.getCurrencyInstance(Locale.US).format(n);

    String china = NumberFormat.getCurrencyInstance(Locale.CHINA).format(n);
    String france = NumberFormat.getCurrencyInstance(Locale.FRANCE).format(n);
    @SuppressWarnings("deprecation")
    String india = NumberFormat.getCurrencyInstance(new Locale("en","IN")).format(n);
    System.out.println("US: "+us);
    System.out.println("India: "+india);
    System.out.println("China: "+china);
    System.out.println("France: "+ france);
    scan.close();
}
}