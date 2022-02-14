# In this file, we will create a GUI based Website Blocker for Windows and Linux with an option to unblock

# Importing all the modules
from tkinter import *
from tkinter.messagebox import *

# Setting the file location and the localhost IP address for the GUI
host_files = {
    'Windows': r"C:\Windows\System32\drivers\etc\hosts",
    'Linux': '/etc/host'
}
localhost = '127.0.0.1'

def block(win):
    def block_websites(websites):
        host_file = host_files['Windows']
        sites_to_block = list(websites.split(' , '))

        # First we will make a copy of the websites you want blocked to a text file called 'blocked_websites.txt'
        with open('blocked_websites.txt', 'r+') as blocked_websites_txt:
            blocked_websites_txt.seek(0, 2)
            for site in sites_to_block:
                blocked_websites_txt.write(site)

        with open(host_file, 'r+') as hostfile:
            content_in_file = hostfile.read()

            for site in sites_to_block:
                if site not in content_in_file:
                    hostfile.write(localhost + '\t' + site + '\n')
                    showinfo('Websites blocked!', message='We have blocked the websites you wanted blocked!')
                else:
                    showinfo('Website Already blocked!', 'A website you entered is already blocked')


    blck_wn = Toplevel(win, background='grey')
    blck_wn.title("Block a website")
    photo = PhotoImage(file = "logo.png")
    blck_wn.iconphoto(False,photo)
    blck_wn.geometry('300x200')
    blck_wn.resizable(False, False)

    Label(blck_wn, text='Block websites', background='LightBlue', font=("Georgia", 16)).place(x=80, y=0)
    Label(blck_wn, text='(Enter the websites separated *only* by \' , \')', background='LightBlue',
          font=("Times", 13)).place(x=0, y=35)
    Label(blck_wn, text='Enter the URLs (www.<sitename>.com):', background='LightBlue', font=('Times', 13)).place(
        x=0, y=70)

    sites = Text(blck_wn, width=35, height=3)
    sites.place(x=0, y=100)

    submit_btn = Button(blck_wn, text='Submit', bg='black',fg="yellow", command=lambda: block_websites(sites.get('1.0',END)))
    submit_btn.place(x=100, y=160)


def unblock(win):
    def unblock_websites(websites_to_unblock):
        host_file = host_files['Windows']

        with open(host_file, 'r+') as hostfile:
            content_in_file = hostfile.readlines()
            hostfile.seek(0)

            for line in content_in_file:
                if not any(site in line for site in websites_to_unblock):
                    hostfile.write(line)

                hostfile.truncate()

        with open('blocked_websites.txt', 'r+') as blocked_websites_txt:
            file_content = blocked_websites_txt.readlines()
            blocked_websites_txt.seek(0)

            for line in file_content:
                if not any(site in line for site in websites_to_unblock):
                    blocked_websites_txt.write(line)

                blocked_websites_txt.truncate()


        Label(unblck_wn, text='Website Blocked!', font=("Times", 13), bg='Aquamarine').place()


    # We are now going to get a list of all the blocked websites from the blocked_websites.txt file from its 3rd line
    with open('blocked_websites.txt', 'r+') as blocked_websites:
        blck_sites = blocked_websites.read().splitlines()[2:]

    unblck_wn = Toplevel(win, background='Aquamarine')
    unblck_wn.title("Block a website")
    unblck_wn.geometry('285x200')
    photo1 = PhotoImage(file = "logo.png")
    unblck_wn.iconphoto(False,photo1)
    unblck_wn.resizable(False, False)

    Label(unblck_wn, text='Unblock websites', background='Aquamarine', font=("Georgia", 16)).place(x=80, y=0)
    Label(unblck_wn, text='Select the URLs that you want to unblock:', background='Aquamarine', font=('Times', 13)).place(x=0, y=70)

    # Creating a dropdown menu from the textfile to get the sites that are blocked
    blck_sites_strvar = StringVar(unblck_wn)
    blck_sites_strvar.set(blck_sites[0])
    dropdown = OptionMenu(unblck_wn, blck_sites_strvar, *blck_sites)
    dropdown.config(width=20)
    dropdown.place(x=60, y=100)

    submit_btn = Button(unblck_wn, text='Submit', bg='black',fg="yellow",
                        command=lambda: unblock_websites(blck_sites_strvar.get()))
    submit_btn.place(x=100, y=160)


# Creating a GUI master window
root = Tk()
root.title("Website Blocker")
photo = PhotoImage(file = "logo.png")
root.iconphoto(False,photo)
root.geometry('400x300')
root.wm_resizable(False, False)

# Creating and setting the locations of all the components of the GUI
Label(root, text='ProjectGurukul Website Blocker', font=("Comic Sans MS", 16)).place(x=45, y=0)
Label(root, text='What do you want to do?', font=("Helvetica", 14)).place(x=90, y=40)

Button(root, text='Block a Website', font=('Times', 16), bg='black', fg="yellow" ,command=lambda: block(root)).place(x=110, y=100)

Button(root, text='Unblock a Website', font=('Times', 16), bg='black',fg="yellow" ,command=lambda: unblock(root)).place(x=100, y=150)

root.update()
root.mainloop()
