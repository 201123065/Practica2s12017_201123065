/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package practica2edd;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

/**
 *
 * @author marcosmayen
 */
public class Graphviz {
    public void Imagen(String cadena){
        try {
            //raiz donde se encuentra el grafo
            String fileInputPath = System.getProperty("user.dir")+"/src/grafo.dot";
            crearArchivo("digraph G {"+cadena+"}",fileInputPath);
            //ejecutable dot, -T, formato, ejecucion, entrada
            String [] cmd = {"/usr/local/bin/dot","-T","png", "-O",fileInputPath}; //Comando de apagado en windows
            Runtime.getRuntime().exec(cmd);
        } catch (Exception ex) {
            System.out.println("resulta que no es mac o linux");
        }
         
    }
    private void crearArchivo(String cadena, String ruta){
        File f;
        FileWriter fw;
        try{
        System.out.println("SI ENRTA QUE PS");
            f = new File("src/grafo.dot");
            fw = new FileWriter(f);
            BufferedWriter bw = new BufferedWriter(fw);
            PrintWriter salida = new PrintWriter(bw);
            salida.write(cadena);
            System.out.println(cadena);
            salida.close();
            bw.close();
        }catch (IOException e){
            System.out.println("algo paso ._.");
        }
    }
}
