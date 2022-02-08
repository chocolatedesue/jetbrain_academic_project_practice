package numbers;

import java.math.BigInteger;

public class NumProperty {
    private BigInteger num;
    private String oe;
//    public enum oe {odd,even};
    private boolean buzz;
    private boolean duck;
    private boolean palindromic;
    private boolean gapful;
    NumProperty(BigInteger data){
        num = data;
    }

    public BigInteger getNum() {
        return num;
    }

    public boolean isGapful() {
        return gapful;
    }

    public void setGapful(boolean gapful) {
        this.gapful = gapful;
    }

    public void setNum(BigInteger num) {
        this.num = num;
    }

    public String getOe() {
        return oe;
    }

    public void setOe(String oe) {
        this.oe = oe;
    }

    public boolean isBuzz() {
        return buzz;
    }

    public void setBuzz(boolean buzz) {
        this.buzz = buzz;
    }

    public boolean isDuck() {
        return duck;
    }

    public void setDuck(boolean duck) {
        this.duck = duck;
    }

    public boolean isPalindromic() {
        return palindromic;
    }

    public void setPalindromic(boolean palindromic) {
        this.palindromic = palindromic;
    }

    public  void showInf(){
        System.out.printf("Properties of %s\n",this.getNum().toString());
//        System.out.printf("%13s","even:");

        System.out.printf("%13s %s\n","buzz:",isBuzz()?"true":"false");
        System.out.printf("%13s %s\n","duck:",isDuck()?"true":"false");
        System.out.printf("%13s %s\n","palindromic:",isPalindromic()?"true":"false");
        System.out.printf("%13s %s\n","gapful:",isGapful()?"true":"false");
        if (this.oe.equals("even")){
            System.out.printf("%13s true\n","even:");
//                System.out.println(" true");
            System.out.printf("%13s false\n","odd:");
//                System.out.println(" false");
        }
        else{
            System.out.printf("%13s false\n","even:");
            System.out.printf("%13s true\n","odd:");
        }
    }
    public void showMulInf(){
        System.out.printf("%s is",getNum());
        if (isBuzz()) System.out.printf(" buzz,");
        if (isDuck()) System.out.printf(" duck,");
        if (isPalindromic()) System.out.printf(" palindromic,");
        if (isGapful()) System.out.printf(" gapful,");
        if (getOe().equals("odd")) System.out.println(" odd");
        else System.out.println(" even");
    }


}
