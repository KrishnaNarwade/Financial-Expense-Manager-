package krishna.kr;


import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.Test;
//comment the above line and uncomment below line to use Chrome
//import org.openqa.selenium.chrome.ChromeDriver;
public class AppTest {

	@Test
    public static void test()throws InterruptedException {
        // declaration and instantiation of objects/variables
    	System.setProperty("webdriver.chrome.driver",".\\driver\\chromedriver.exe");
		WebDriver driver = new ChromeDriver();
    	
		//comment the above 2 lines and uncomment below 2 lines to use Chrome
		//System.setProperty("webdriver.chrome.driver","G:\\chromedriver.exe");
		//WebDriver driver = new ChromeDriver();
    	
		driver.get("http://www.google.com");
        System.out.println("Title of the page is: " + driver.getTitle());
        driver.close();
    }

}