// Java 8
    /**
    *    Method Name: printArray
    *    Print each element of the generic array on a new line. Do not return anything.
    *    @param A generic array
    **/
    
    // Write your code here
    public static <E> void printArray(E[] array){

       for(E element : array){
           System.out.println(element);
       }
   }