import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

 public class CharacterCount {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.next();
        scanner.close();

        // converting input to lowercase its optional
        input = input.toLowerCase();

        // Create a HashMap to store the character counts
        Map<Character, Integer> charCountMap = new HashMap<>();

    
        // Convert the string to character array
        char[] charArray = input.toCharArray();

        // Iterate through the character array
        for (char c : charArray) {
            if (charCountMap.containsKey(c)) {
                // if the character is already in the map, increament its count
                charCountMap.put(c, charCountMap.get(c) + 1);
            } else {
                // If the character is not in the map, add it with a count of 1
                charCountMap.put(c, 1);
            }
        } 
            
        // Print the character counts
        for (Map.Entry<Character, Integer> entry : charCountMap.entrySet()) {
            System.out.println((entry.getKey() + ": " + entry.getValue()));
        }
        
    }
 }