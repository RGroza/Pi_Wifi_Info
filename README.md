# Pi_Wifi_Info

This GitHub repository contains code for accessing your Raspberry Pi's IP Address, Gateway Address, and your Hostname, and it is able to send an email with those credentials to your inbox. This saves time when wanting to establish a headless connection with your Raspberry Pi using your IP Address, which is prone to changing on your network. Please follow the guide below to setup the emailing service for your Raspberry Pi.

Create a SendGrid Account
-------------------------

This program requires the SendGrid API to function. SendGrid is an email marketing service that is used by many businesses to automatically send emails to their recipients. This allows the program to send an email using your email account without needing to store your credentials in your Raspberry Pi.

Create a SendGrid account `https://signup.sendgrid.com` and login to your SendGrid dashboard.

Create an API Key
-----------------

Click on the "Settings" dropdown menu on the left hand side and then on "API Keys". Click on "Create API Key" and copy the string generated. I would highly suggest saving the API key in a text file on your computer.

SSH Headless Configuration
--------------------------

If you don't have access to a monitor and a keyboard, it is advised to use a network that you can easily access your Pi's IP Address (possibly your home network). Insert the Pi's SD Card into your computer and copy the two files from the "ssh_setup" folder of this repository. Change the ssid of the wpa_supplicant.conf file to the Wifi name and add a password if necessary after the ssid: `psk="<password>"`

Install Packages
----------------

These are the necessary packages that need to be installed before being able to run the program.

    sudo pip install python_http_client
    
    sudo pip install sendgrid

Clone the Repository
--------------------

Navigate to the desired directory on the Pi and enter the command:

    clone https://github.com/RGroza/Pi_Wifi_Info.git

Once the cloning process has finish, check for the folder by using:

    ls
    
And navigate into the folder using:

    cd Pi_Wifi_Info

Manual Setup (not needed if cloning is successful)
--------------------------------------------------

Navigte to your desired directory and create a file on your Raspberry Pi's current directory called "send_info.py" using:

    touch send_info.py

And then edit the file you just created:

    sudo nano send_info.py

Copy the code from "send_info.py" in this repository and paste it into nano using:

Windows:
    Ctrl + Shift + V  OR  Shift + Insert  OR  Right Click in nano editor

Mac:
    Command + Shift + V  OR  Right Click and paste in nano editor

Setup and Run
-------------

Insert your email in the `from_email='<your email address>'` and `to_emails='<your email address>'` parameters, and insert your API Key into `sg = SendGridAPIClient('<API Key>')`

Run the program to see if it is able to send an email to your inbox:

    python send_info.py

The first few emails that are sent to your inbox might be flagged as spam, so it is advised to check your spam folder and mark them as being genuine.

Run Program on Raspberry Pi's Boot
----------------------------------

To execute the script on every reboot, you need to add the python app to the `rc.local` file.

    sudo nano /etc/rc.local

Add the following command before `end 0` in the file and insert your file path where indicated:

    (sleep 15; python <INSERT FILE PATH>/send_info.py)&

To test your configuration change, simply reboot the pi:

    sudo reboot

Remember that the first few emails that are sent to your inbox might be flagged as spam, so it is advised to check your spam folder and mark them as being genuine.
