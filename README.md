# Pi_Wifi_Info

Create a SendGrid Account
-------------------------

Create a SendGrid account `https://signup.sendgrid.com` and login to your SendGrid dashboard.

Create an API Key
-----------------

Click on the "Settings" dropdown menu on the left hand side and then on "API Keys". Click on "Create API Key" and copy the string generated. I would highly suggest saving the API key in a text file on your computer.

SSH Headless Configuration
--------------------------

If you don't have access to a monitor, it is advised to use a network that you can easily access your Pi's IP Address (either on the class's TP-Link router or your home network). Insert the Pi's SD Card into your computer and copy the two files from the "ssh setup" folder of this repository. Change the ssid of the wpa_supplicant.conf file to the Wifi name and add a password if necessary after the ssid: `psk="<password>"`

Install Packages
---------------

    sudo pip install python_http_client
    
    sudo pip install sendgrid
    
Quickstart
----------

Navigte to your desired directory and create a file on your Raspberry Pi's current directory called "send_info.py" using:

    touch send_info.py

And then edit the file you just created:

    sudo nano send_info.py

Copy the code from "send_info.py" in this repository and paste it into nano using:

Windows:
    Ctrl + Shift + V  OR  Shift + Insert  OR  Right Click in nano editor

MAC:
    Command + Shift + V  OR  Right Click and paste in nano editor

Insert your email in the "from_email" and "to_emails" parameters, and insert your API Key into `sg = SendGridAPIClient('<API Key>')`

Run the program to see if it is able to send an email to your inbox:

    python send_info.py

The first few emails that are sent to your inbox might be flagged as spam, so it is advised to check your spam folder and mark them as being genuine.

Run Program on Raspberry Pi's Boot
----------------------------------

To execute the script on every reboot, you need to add the python app to the `rc.local` file.

    sudo nano /etc/rc.local

Add the following command before `end 0` in the file and insert your file path where indicated:

    (sleep 30; python <INSERT FILE PATH>/send_info.py)&

To test your configuration change, simply reboot the pi:

    sudo reboot

Remember that the first few emails that are sent to your inbox might be flagged as spam, so it is advised to check your spam folder and mark them as being genuine.

Change your Pi's network connection to MIT GUEST if you haven't already and boot the Pi to test if the email service is working correctly.
