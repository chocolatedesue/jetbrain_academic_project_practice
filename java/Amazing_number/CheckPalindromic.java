package numbers;

import java.math.BigInteger;

public class CheckPalindromic {
    public static boolean check(BigInteger tar){
        String temp = String.valueOf(tar);
        if (temp.equals(new StringBuffer(temp).reverse().toString())){
            return true;
        }
        else return  false;
    }
}
