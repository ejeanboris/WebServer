from django.db import models
from django.db.models import Model
from django.db.models import permalink
import email, imaplib
from email import parser, message
from email.parser import BytesParser
from email.message import EmailMessage
import quopri
# Create your models here.


class MailBox(models.Model):

    myEmails=[]
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    connected = False
    name=models.CharField(max_length=100, unique=True,default='Rem')

    @classmethod
    def connect(self,*args, **kwargs):
        self.mail = imaplib.IMAP4_SSL('imap.gmail.com')
        self.mail.login('ejeanboris@gmail.com', 'Incorrect47G')
        self.mail.list()
        # Out: list of "folders" aka labels in gmail.
        self.mail.select("inbox",readonly=True) # connect to inbox.
        self.connected=True


    @classmethod
    def supply(self,*args, **kwargs):

        #if self.connected==False:
        self.connect()

        result, data = self.mail.uid('search', None, "ALL") # search and return uids instead
        id_list = data[0].split()

        for latest_email_uid in id_list[:-200:1]:
            result, data = self.mail.uid('fetch', latest_email_uid, '(RFC822)')
            raw_email = data[0][1]
            # here's the body, which is raw text of the whole email
            # including headers and alternate payloads

            #Parsing
            manager=BytesParser()
            email_message = manager.parsebytes(raw_email)

            message_juice= email_message.get_payload(decode=True)
            try:
                newBlog= Blog(title=email_message['Subject'],body= message_juice.decode('windows-1251'))
                newBlog.save()
                self.myEmails.append(newBlog)
                pass
            except Exception as e:
                pass


class Blog(models.Model):
    title = models.TextField()
    body = models.TextField()
    id = models.AutoField(primary_key=True)
    posted = models.DateField(db_index=True, auto_now_add=True)
#    def __unicode__(self):
#        return '%s' % self.title

#    @permalink
#    def get_absolute_url(self):
#        return ('view_blog_post', None, { 'slug': self.slug })

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    #@permalink
    #def get_absolute_url(self):
        #return ('view_blog_category', None, { 'slug': self.slug })
