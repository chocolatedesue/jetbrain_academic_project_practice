package numbers;

import java.math.BigInteger;
import java.util.Scanner;

public class CheckGapful {
    public static boolean check(BigInteger s){
        if (s.compareTo(BigInteger.valueOf(100L))==-1)
            return false;
        else {
            int reminder = (s.toString().charAt(0)-'0')*10+(s.toString().charAt(s.toString().length()-1)-'0');
            return s.remainder(BigInteger.valueOf(reminder)).equals(BigInteger.ZERO);
        }

    }


}
