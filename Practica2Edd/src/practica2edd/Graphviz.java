/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package practica2edd;

/**
 *
 * @author marcosmayen
 */
public class Graphviz {
    public void Imagen(String cadena){
        try {
            //raiz donde se encuentra el grafo
            System.out.println(System.getProperty("user.dir")+"/grafo.dot");
            String fileInputPath = System.getProperty("user.dir")+"/grafo.dot";
            //ejecutable dot, -T, formato, ejecucion, entrada
            String [] cmd = {"/usr/local/bin/dot","-T","png", "-O",fileInputPath}; //Comando de apagado en windows
            Runtime.getRuntime().exec(cmd);
        } catch (Exception ex) {
            System.out.println("resulta que no es mac o linux");
        }
         
    }
}
