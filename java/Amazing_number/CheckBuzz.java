package numbers;

import java.math.BigInteger;

public class CheckBuzz {
    public static boolean check(BigInteger tar){
        return tar.remainder(BigInteger.valueOf((long) 7)).equals(BigInteger.ZERO) || tar.remainder(BigInteger.TEN).equals(BigInteger.valueOf(7L));
   }
}

