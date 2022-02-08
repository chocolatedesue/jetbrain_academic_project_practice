package numbers;

import java.math.BigInteger;

public class CheckDuck {
    public static boolean check(BigInteger tar){
        String temp = String.valueOf(tar);
        if (temp.startsWith("0")){
            for (int i=1;i<temp.length();++i){
                if (temp.charAt(i)=='0'){
                    return true;
                }
            }
            return false;
        }
        else {
            return temp.contains("0");
        }
    }

}

