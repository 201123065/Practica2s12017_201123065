package practica2edd;


import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;
import java.awt.Dimension;
import java.awt.Toolkit;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.logging.Level;

public class Practica2Edd {

    public static OkHttpClient webClient = new OkHttpClient();
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Panel panel = new Panel();
        panel.setVisible(true);
        panel.setLocationRelativeTo(null);
        String nombre = "Marcod";
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato", nombre)
                .add("dato2", "4")
                .build();
        String r = getString("metodoWeb", formBody); 
        System.out.println(r + "---");
    }
 
     public static String getString(String metodo, RequestBody formBody) {

        try {
            URL url = new URL("http://0.0.0.0:5000/" + metodo);
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(practica2edd.Practica2Edd.class.getName()).log(Level.SEVERE, null, ex);
        } catch (Exception ex) {
            java.util.logging.Logger.getLogger(practica2edd.Practica2Edd.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }
    
}

