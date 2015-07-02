#Quick script by Luke Turvey to find what CDN is being used

from selenium import webdriver #Import
import sys, os, time


def CDNGET(CDNURL):

	browser = webdriver.Firefox()
	read = browser.get("http://www.cdnplanet.com/tools/cdnfinder/#site:http://"+CDNURL)
	html = browser.page_source #get URL and open firefox to load page
	
	with open("html.txt", "a") as file:
		file.write(html.encode('utf8')) #Have to encode to write to file
		file.close()
	time.sleep(1)
	browser.quit() #Writes HTML to file and closes browser
	os.system('clear')
	
	searchfile = open("html.txt","r") #opens text file and searches for CDN used in the HTML
	for line in searchfile:
		if "is using <strong>Google" in line:
			print "Google is the CDN, Can you bypass it?" 
			break
		elif "is using <strong>Akamai" in line:
			print "Akamai is the CDN, Can you bypass it?"
			break
		elif "is using <strong>Cloudflare" in line:
			print "Cloudflare is the CDN, Can you bypass it?"
			break
		elif "is using <strong>Amazon" in line:
			print "Amazon Cloudfront is the CDN, Can you bypass it?"
			break
		elif "is using <strong>Incapsula" in line:
			print "Incapsula is the CDN, Can you bypass it?"
			break
		elif "is using <strong>Fastly" in line:
			print "Fastly is the CDN, Can you bypass it?"
			break
		elif "is using <strong>Level" in line:
			print "Level 3 is the CDN, Can you bypass it?"
			break
		elif "is using <strong>Bitgravity" in line:
			print "Bitgravity is the CDN, Can you bypass it?"
			break
		elif "is using <strong>Cache" in line:
			print "Cache is the CDN, Can you bypass it?"
			break
		elif "is using <strong>CDN77" in line:
			print "CDN77 is the CDN, Can you bypass it?"
			break
		elif "is using <strong>CDNetworks" in line:
			print "CDNetworks is the CDN, Can you bypass it?"
			break
		elif "is using <strong>CDNIFY" in line:
			print "CDNIFY is the CDN, Can you bypass it?"
			break
		elif "is using <strong>ChinaCache" in line:
			print "ChinaCache is the CDN, Can you bypass it?"
			break
		elif "is using <strong>ChinaNetCenter" in line:
			print "ChinaNetCenter is the CDN, Can you bypass it?"
			break
		elif "is using <strong>EdgeCast" in line:
			print "Edgecast is the CDN, Can you bypass it?"
			break
		elif "is using <strong>Highwinds" in line:
			print "Highwinds is the CDN, Can you bypass it?"
			break
		elif "is using <strong>Internap" in line:
			print "Internap is the CDN, Can you bypass it?"
			break
		elif "is using <strong>Keycdn" in line:
			print "KeyCDN is the CDN, Can you bypass it?"
			break
		elif "is using <strong>Leaseweb" in line:
			print "Leaseweb is the CDN, Can you bypass it?"
			break
		elif "is using <strong>Limelight" in line:
			print "Limelight is the CDN, Can you bypass it?"
			break
		elif "is using <strong>MaxCDN" in line:
			print "MaxCDN is the CDN, Can you bypass it?"
			break
		elif "is using <strong>Ngenix" in line:
			print "NGENIX is the CDN, Can you bypass it?"
			break
		elif "is using <strong>Skypark" in line:
			print "Skypark is the CDN, Can you bypass it?"
			break
		elif "is using <strong>Xcdn" in line:
			print "XCDN is the CDN, Can you bypass it?"
			break
		else: "Looks like no CDN is used"
	searchfile.close()
	
if __name__ == "__main__":
	print "Please enter domain in which to check CDN. I.E google.com \n"
	CDNURL = raw_input('')
	CDNGET(CDNURL)
	
	#CDNURL Example - google.com

