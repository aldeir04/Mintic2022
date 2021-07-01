import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
        //int i = 1;
        
        Scanner sc = new Scanner(System.in);
        System.out.println("Por favor ingrese su nombre");
        String nombre_Entrada = sc.nextLine();
        System.out.println("Su nombre es: "+nombre_Entrada);
        

        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Por favor ingrese su nombre");
        String nombre_Entra = br.readLine();
        System.out.println("Su nombre es: "+nombre_Entra);

    }
}
    