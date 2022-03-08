public class Luca {
/*
calcolare l 'area di una forma triangolare di dimensione n come quella riportata
sotto, nell' ipotesi che ciascun quadrato [] abbia area unitaria
[]
[][]
[][][]
[][][][]
[][][][][]
sono 15 vediamo come si torna a 15
*/

    public static void main(String[] args) {
        //base del triangolo
        int baseArea=5;
        int a=AreaTriangolo (baseArea);
        System.out.println("Area del triangolo "+ a + "unit� di area");

}//end main



public static int AreaTriangolo (int n) {
    int result;

    if(n<=0) {

        result=0;

    }

    else if(n==1) {

        result=1;

    }else {


        result=n + AreaTriangolo(n-1);



        }


        return result;
    }



}