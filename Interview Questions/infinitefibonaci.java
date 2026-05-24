import java.util.Iterator;

public class infinitefibonaci implements Iterator<Integer>{
    private int a = 0;
    private int b = 1;

   @Override
    public boolean hasNext(){
        return true;
    }

    @Override
    public Integer next() {
        int current = a;
        int temp = a;
        a = b;
        b = temp + b;
        return current;
    }

    public static void main(String[] args) {
        infinitefibonaci f1 = new infinitefibonaci();

       while (true) {
            System.out.println(f1.next());
        }
    }
}
