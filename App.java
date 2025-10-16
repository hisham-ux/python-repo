import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpExchange;
import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.util.Random;

public class App {
    public static void main(String[] args) throws IOException {
       HttpServer server = HttpServer.create(new InetSocketAddress(9090), 0);

        server.createContext("/", new QuoteHandler());

        server.setExecutor(null); // default executor
        System.out.println("🚀 Server running on http://localhost:9090/");
        server.start();
    }

    static class QuoteHandler implements HttpHandler {
        private final String[] quotes = {
            "The best way to predict the future is to invent it.",
            "Simplicity is the soul of efficiency.",
            "Code is like humor. When you have to explain it, it’s bad.",
            "First, solve the problem. Then, write the code.",
            "Experience is the name everyone gives to their mistakes."
        };

        @Override
        public void handle(HttpExchange exchange) throws IOException {
            Random rand = new Random();
            String response = "💡 Random Quote: " + quotes[rand.nextInt(quotes.length)];
            exchange.sendResponseHeaders(200, response.getBytes().length);
            OutputStream os = exchange.getResponseBody();
            os.write(response.getBytes());
            os.close();
        }
    }
}
