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
    public void Imagen(){
        try {
            //raiz donde se encuentra el grafo
            String fileInputPath = System.getProperty("user.dir")+"/grafo.dot";
            //ejecutable dot, -T, formato, ejecucion, entrada
            String [] cmd = {"/usr/local/bin/dot","-T","png", "-O",fileInputPath}; //Comando de apagado en windows
            Runtime.getRuntime().exec(cmd);
        } catch (Exception ex) {
            System.out.println("resulta que no es mac o linux");
        }
        try{
            String ruta="c:\\Archivos de programa\\Graphviz 2.28\\bin\\dot.exe";
            String fileInputPath = System.getProperty("user.dir")+"\\grafo.dot";
            String fileOutputPath = System.getProperty("user.dir")+"\\grafo1.jpg";
            //ejecutable dot, -T, formato, ejecucion, entrada
            String [] cmd = {ruta,"-Tpng",fileInputPath,"-o",fileOutputPath}; //Comando de apagado en windows
            Runtime.getRuntime().exec(cmd);
            
        }
        catch(Exception ex){
            System.out.println("resulta que tampoco es windows");
        }   
    }
}
