import java.util.*;
import java.util.LinkedList;
public class Customer
{
public static void main(String[] args)
   {
      Queue q1 = new LinkedList();
      
      q1.add("Peter");
      q1.add("Sam");
      q1.add("John");
      q1.add("Caleb");
      q1.remove();
      q1.remove();
      
      System.out.println("Queue: " + q1);
   }
}