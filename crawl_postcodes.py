import dryscrape
import time


def wait_until_enable(node):
    while(node.is_disabled()):
        time.sleep(0.2)
    return

# set up a web scraping session
sess = dryscrape.Session(base_url = 'http://www.ems.com.cn/')

print "Connecting..."

# visit homepage and search for a term
sess.visit('/serviceguide/you_bian_cha_xun.html')

print "Start crawling postcodes..."
# Get the selection elements of province, city and result via xpath

province = sess.at_xpath('//*[@id="province"]')
city = sess.at_xpath('//*[@id="city"]')
result = sess.at_xpath('//*[@id="result"]')



# select options under province one by one: 
for pro_option in province.children()[1:]: # skip the first option

    print "######### %s #########" % pro_option.text()
    pro_option.select_option()
    wait_until_enable(province) # wait until ajax data loaded

    # select options under city one by one 
    for city_option in city.children()[1:]: # skip the first option
        print city_option.text()
        city_option.select_option()

        wait_until_enable(city) # wait until ajax data loaded 

        for res_option in result.children():
            print res_option.text()

        print ""

    print ""

print "Crawled postcodes successfully.."            









