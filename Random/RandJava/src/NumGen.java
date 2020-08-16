// amobin19
import java.util.Random;

public class NumGen{

    public static int two_digit_number_generator(){
        // create instance of Random class
        Random rand = new Random();

        // generate random integers in range 0 to 99
        int num = rand.nextInt(100);

        // ensure number is 2 digit value
        if(num < 10){
            num = num + 10;
        }
        if(num > 99){
            num = num - 10;
        }

        return num;
    }

    public static void main(String args[])
    {
        // print values
        System.out.println(two_digit_number_generator());
        System.out.println(two_digit_number_generator());
    }
}