from django.contrib import admin
from blog.models import Blog, Category, MailBox
import email, imaplib
from email import parser, message
from email.parser import BytesParser
from email.message import EmailMessage
import quopri
# Register your models here.

#Actions
def fillUp(modeladmin, request, queryset):

    for obj in queryset:
        #if self.connected==False:
        obj.connect()

        result, data = obj.mail.uid('search', None, "ALL") # search and return uids instead
        id_list = data[0].split()

        for latest_email_uid in id_list[:-100:-1]:
            result, data = obj.mail.uid('fetch', latest_email_uid, '(RFC822)')
            raw_email = data[0][1]

            # here's the body, which is raw text of the whole email
            # including headers and alternate payloads

            #Parsing
            manager=BytesParser()
            email_message = manager.parsebytes(raw_email)

            try:
                message_juice= email_message.get_payload(decode=False)
                while type(message_juice)==type([1,2]) and type(message_juice[0].get_payload(decode=False))==type([1,2]):
                    message_juice= message_juice[0].get_payload(decode=False)

                if type(message_juice)==type([1,2]):
                    if message_juice[-1].get_filename() == None:
                        html_message_juice= message_juice[-1].get_payload(decode=True)
                    else:
                        html_message_juice= message_juice[0].get_payload(decode=True)
                else:
                    html_message_juice= email_message.get_payload(decode=True)

                try:
                    newBlog= Blog(title=email_message['Subject'], body= html_message_juice.decode())
                    newBlog.save()
                except:
                    newBlog= Blog(title=email_message['Subject'], body= html_message_juice.decode('windows-1251'))
                    newBlog.save()

            except:
                newBlog= Blog(title=email_message['Subject'], body= "This email could not be processed see what happened \n\nSubject: "+email_message['Subject'])
                newBlog.save()
                pass
            obj.myEmails.append(latest_email_uid)


fillUp.short_description = "Download all emails from inbox; do this only once"

def refresh(modeladmin, request, queryset):
    for obj in queryset:
        #if self.connected==False:
        obj.connect()

        result, data = obj.mail.uid('search', None, "ALL") # search and return uids instead
        id_list = data[0].split()

        for latest_email_uid in id_list[:-100:-1]:
            if latest_email_uid in obj.myEmails:
                pass

            else:
                result, data = obj.mail.uid('fetch', latest_email_uid, '(RFC822)')
                raw_email = data[0][1]
                # here's the body, which is raw text of the whole email
                # including headers and alternate payloads

                #Parsing
                manager=BytesParser()
                email_message = manager.parsebytes(raw_email)

                try:
                    message_juice= email_message.get_payload(decode=False)
                    while type(message_juice)==type([1,2]) and type(message_juice[0].get_payload(decode=False))==type([1,2]):
                        message_juice= message_juice[0].get_payload(decode=False)

                    if type(message_juice)==type([1,2]):
                        if message_juice[-1].get_filename() == None:
                            html_message_juice= message_juice[-1].get_payload(decode=True)
                        else:
                            html_message_juice= message_juice[0].get_payload(decode=True)
                    else:
                        html_message_juice= email_message.get_payload(decode=True)

                    try:
                        newBlog= Blog(title=email_message['Subject'], body= html_message_juice.decode())
                        newBlog.save()
                    except:
                        newBlog= Blog(title=email_message['Subject'], body= html_message_juice.decode('windows-1251'))
                        newBlog.save()

                except:
                    newBlog= Blog(title=email_message['Subject'], body= "This email could not be processed see what happened \n\nSubject: "+email_message['Subject'])
                    newBlog.save()
                    pass
            obj.myEmails.append(latest_email_uid)
refresh.short_description = "Download new emails from inbox"

#Models
class BlogAdmin(admin.ModelAdmin):
    exclude = ['']

class MailBoxAdmin(admin.ModelAdmin):
    exclude= ['myEmails','connected']
    actions = [fillUp,refresh]

admin.site.register(Blog, BlogAdmin)
admin.site.register(MailBox, MailBoxAdmin)
