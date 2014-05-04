import imaplib
import webbrowser

class Py3status:
    
    """
    A py3status module which checks for unread mail in a gmail inbox 
    and displays the number of unread messages on the bar.



    """

    
    def kill(self, i3status_output_json, i3status_config):
                
        
        pass

    def on_click(self, i3status_output_json, i3status_config, event):
                
        webbrowser.open("http://mail.google.com") #open gmail on click (Not working on my system)
        
        pass

    def empty(self, i3status_output_json, i3status_config):
        
        response = {'full_text': '', 'name': 'empty'}
        
        f = open('py3mail.conf', 'r') #Open file containing username and password
        username = f.readline() #read first line
        password = f.readline()  # read second line
        f.close()
        usr = username.strip() #strip trailing spaces
        passw = password.strip()

        obj = imaplib.IMAP4_SSL('imap.gmail.com','993') #login to gmail
        obj.login( usr, passw) 
        obj.select()
        obj.search(None,'UnSeen') ##look for unread mail
        num = len(obj.search(None, 'Unseen')[1][0].split()) #get number of unread messages/
        
        if num >0 :
            response['color'] =i3status_config['color_good'] #if we have an unread message, change colour.
         
             
        response['full_text'] = "Unread mail: {0}".format(num)  
        return (0, response)
