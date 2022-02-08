package numbers;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
//        write your code here
        welcome();
        Scanner sc = new Scanner(System.in);
        while (true){
            System.out.println("Enter a request:");
            String[] temp = sc.nextLine().split(" ");
            BigInteger tar = new BigInteger(temp[0]);
            if (temp.length==1){

                if (tar.compareTo(BigInteger.ZERO)==-1) {
                    System.out.print("The first parameter should be a natural number or zero.\n");
                } else if (tar.equals(BigInteger.ZERO)) {
                    System.out.print("\nGoodbye!");
                    break;
                } else {
                    NumProperty n = getNumProperty(tar);
                    n.showInf();
                }
            }
            else {
                long cnt = Integer.valueOf(temp[1]).longValue();
                if (cnt<=0){
                    System.out.println("second parameter should be a natural number");
                    continue;
                }
                for (long i=0;i<cnt;++i){
                    NumProperty n = getNumProperty(tar.add(BigInteger.valueOf(i)));
                    n.showMulInf();
                }
            }
        }
//
//        while (true) {
//
//
////            int tar = sc.nextInt();
//            BigInteger tar = sc.nextBigInteger();
//            BigInteger cmp = new BigInteger("0");

//        }
    }

    private static void welcome() {
        System.out.printf("Welcome to Amazing Numbers!\n\n");
        System.out.println("Supported requests:");
        System.out.println("- enter a natural number to know its properties;");
        System.out.println("- enter two natural numbers to obtain the properties of the list:");
        System.out.println("  * the first parameter represents a starting number;");
        System.out.println("  * the second parameter shows how many consecutive numbers are to be processed;");
        System.out.println("- separate the parameters with one space;");
        System.out.printf("- enter 0 to exit.\n\n");
    }

    private static NumProperty getNumProperty(BigInteger tar) {
        NumProperty n = new NumProperty(tar);
        n.setBuzz(CheckBuzz.check(n.getNum()));
        n.setDuck(CheckDuck.check(n.getNum()));
        n.setOe(CheckOe.check(n.getNum()));
        n.setPalindromic(CheckPalindromic.check(n.getNum()));
        n.setGapful(CheckGapful.check(n.getNum()));
        return n;
    }

}
