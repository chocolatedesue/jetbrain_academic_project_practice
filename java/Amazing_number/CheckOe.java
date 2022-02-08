package numbers;

import java.math.BigInteger;

public class CheckOe {
    public static String check (BigInteger tar){
        if (tar.and(BigInteger.ONE).equals(BigInteger.ONE))return "odd";
        else return "even";
    }
}
