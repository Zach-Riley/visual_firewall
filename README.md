# Raytheon-Visual-Firewall
Senior Design Project

This project graphically displays traffic that goes through a network by querying IPtables.

It's current capabilities include:
  -representing various connections made to a host behind the firewall
  -bandwidth usage of those connections
  -http packet inspection
    -this feature is enabled by the use of pcap2har by andrewf. The pcap2har repository can be found here: https://github.com/andrewf/pcap2har.git
    
Other features to be implemented in the future:
  -recording traffic for playback at a later time
  -implementing anomaly detection algorithms to automate anomaly detection
  -being able to speed up or slow down the real time playback of traffic for better manual analysis
  -modify IPTables rules remotely through the application
  -addition of other packet information upon deep inspection
  
Installation and Run Instructions:
  -first, download the code to your webserver on your router.
  -start capture.sh to allow the web app to display the http packets when needed.
    -the first pcap won't be available until 5 minutes have elapsed since the start
  -in a browser, go to the IP address of your webserver and the web app should be at an intro screen
  -enter your desired query speed and a whitelist if you wish and click 'save and continue' when done
