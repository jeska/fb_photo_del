from urllib import urlopen
import logging
from os import system
from datetime import datetime, timedelta
logging.basicConfig(filename='checkpic.log',level=logging.INFO)

def run():
   pic_address = "" # YOUR PHOTO HERE
   try:
      get_pic = urlopen(pic_address)
      deleted_date = datetime(YYYY, MM, DD, HH, MM) # YOUR DELETION DATE/TIME HERE
      diff = datetime.today() - deleted_date
      msg = ""

      if get_pic.getcode() == 200:
         if diff.days % 7 == 0:
            msg = "It has been %d weeks since you tried to delete that photo, but Facebook just won\\'t quit! Check it out: %s" % (diff.days / 7, pic_address)
            sub = "Facebook does not know how to quit you."
      else:
         msg = "It was %d days since you deleted that photo. Congrats, Facbeook! Click the URL to see: %s" % (diff.days, pic_address)
         sub = "Facebook did it!"


      if len(msg) > 0:
         # This should work on Mac/Linux OSes. Feel free to play around with this line if you'd prefer something else
         command = 'echo %s | mail -s "%s" YOUR_EMAIL_HERE' % (msg, sub)
         system(command)
         
   except IOError, ioex:
      logging.info('IOError, but all is well!')

if __name__ == '__main__':
   run()
