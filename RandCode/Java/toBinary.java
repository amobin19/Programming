// amobin19 09/09/2020

import java.util.ArrayList;

public class toBinary {

    public static ArrayList<Integer> revArrayList(ArrayList<Integer> array_list)
    {
        ArrayList<Integer> revArrayList = new ArrayList<Integer>();
        for (int i = array_list.size() - 1; i >= 0; i--) {
            revArrayList.add(array_list.get(i));
        }
        return revArrayList;
    }

    static ArrayList<Integer> rev_list = new ArrayList<Integer>(16);

    public static ArrayList toBin(int decimal){
        if(decimal == 0){
            rev_list.add(0);
        }
        else {
            int var = decimal / 2;
            int rem = decimal % 2;
            rev_list.add(rem);
            toBin(var);
        }
        return revArrayList(rev_list);
    }

    public static void main(String args[])
    {
        System.out.println(toBin(7));
    }
}
