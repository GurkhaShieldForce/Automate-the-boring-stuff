#This is the python version of the scraping application where we use playwright and json module 
from playwright.sync_api import sync_playwright
import time
import json

def run():
    with sync_playwright() as p:
        browser = None
        try:
            # Replace 'USERNAME:PASSWORD' with your actual credentials
            auth = 'USERNAME:PASSWORD'
            
            browser = p.chromium.connect_over_cdp(f"wss://{auth}@authstring") #replace with auth string
            
            page = browser.new_page()
            page.set_default_timeout(2 * 60 * 1000)
            
            page.goto('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
            
            selector = '.a-carousel-card'

            page.wait_for_selector(selector)

            products = page.evaluate("""
                () => {
                    const productElements = document.querySelectorAll('.a-carousel-card');
                    
                    return Array.from(productElements).map(element => {
                        const nameElement = element.querySelector('.p13n-sc-truncate-desktop-type2');
                        const priceElement = element.querySelector('._cDEzb_p13n-sc-price_3mJ9Z');
                        const linkElement = element.querySelector('a.a-link-normal');
                        
                        return {
                            name: nameElement ? nameElement.textContent.trim() : 'N/A',
                            price: priceElement ? priceElement.textContent.trim() : 'N/A',
                            url: linkElement ? linkElement.href : 'N/A'
                        };
                    });
                }
            """)

            delay = 5  # 5 seconds delay

            for product in products[:5]:  # Limit to first 5 products for testing
                if product['url'] != 'N/A':
                    print(f"Navigating to: {product['url']}")
                    
                    try:
                        new_page = browser.new_page()
                        new_page.goto(product['url'], wait_until='networkidle')
                        
                        # Here you can add more scraping logic for the individual product page if needed
                        print(f"Scraped: {product['name']}")
                        
                        new_page.close()
                        
                        # Constant delay of 5 seconds
                        time.sleep(delay)
                    except Exception as error:
                        print(f"Failed to scrape {product['url']}: {str(error)}")

            print(json.dumps(products, indent=2))
            
        except Exception as e:
            print('Scrape failed', str(e))
        finally:
            if browser:
                browser.close()

if __name__ == "__main__":
    run()
