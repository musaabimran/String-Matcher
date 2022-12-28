import tkinter
import tkinter.font as tkf
from tkinter import OptionMenu
from tkinter import  filedialog
from tkinter import  StringVar
import itertools
from tkinter import  Toplevel
# Initializing the Library
app = tkinter.Tk()
#THESE ARE VARIABLES FOR POP UP WINDOW


#---------------------- KMP Algorithm from Internet ---------------------#
def KMPSearch(pat, txt,length_match,indexes):
    M = len(pat)
    N = len(txt)

    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    lps = [0] * M
    j = 0  # index for pat[]

    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)

    i = 0  # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            #print("Found pattern at index", str(i - j))
            if(length_match == 1):
                #print(txt[i-j+len(pat)])
                if((txt[i-j+len(pat)] == " " or txt[i-j+len(pat)] == "") and txt[i-j-1] == " "):
                    indexes.append(i-j)
            else:
                indexes.append(i - j)
            j = lps[j - 1]

        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


def computeLPSArray(pat, M, lps):
    len = 0  # length of the previous longest prefix suffix

    lps[0]  # lps[0] is always 0
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len - 1]

                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1
#---------------------------------End of KMP Algorithm---------------------------#

# This function reaches the files list descriptor
def KMPImplementation(files,string_to_search,match_whole_word,match_case):
    indexes=[]
    # Reading the Files Data
    for i in range(len(files)):
        # Create an instance of Tkinter frame
        win = tkinter.Tk()
        win.geometry("1000x1000")
        win.title("KMP Result")
        text=[]
        T = tkinter.Text(win, height=500, width=500)
        T.insert(str(i) + ".0", str(files[i].name + "\n"))
        #Readlines returns a list of text
        text = (files[i].readlines())
        #print(text)
        if(text != None):
            text[-1] = text[-1]+"\n"
        #print(text)
        index = 1
        #Applying Algo on each Line
        for j in range(len(text)):
            indexes=[]
            # Conditions to Consider
            if (match_whole_word.get() == 1) & (match_case.get() == 0):
                #print("Match whole word only [Checked] and Match case [Unchecked]")
                # Getting the possiblites of lower and Upper Cases
                lists = (map(''.join, itertools.product(*zip(string_to_search.upper(), string_to_search.lower()))))
                lists = (list(lists))
                for l in range(len((lists))):
                    KMPSearch((lists[l]), text[j],1,indexes)
            elif (match_whole_word.get() == 0) & (match_case.get() == 1):
                #print("Match whole word only [Unchecked] and Match case [Checked]")
                KMPSearch(string_to_search, text[j],0, indexes)
            elif (match_whole_word.get() == 0) & (match_case.get() == 0):
                #print("Match whole word only [Unchecked] and Match case [Unchecked]")
                # Getting the possiblites of lower and Upper Cases
                lists = (map(''.join, itertools.product(*zip(string_to_search.upper(), string_to_search.lower()))))
                lists = (list(lists))
                for l in range(len((lists))):
                    KMPSearch((lists[l]), text[j],0, indexes)
            else:
                #print("Match whole word only [Checked] and Match case [checked]")
                KMPSearch(string_to_search, text[j],1, indexes)

            #Making the Box
            if(indexes):
                #T.insert((str(j)+".0"),"Line -> " + str(j+1)  + " Index No -> " + str(indexes)[1:-1] + " Text ->" + text[j] )
                col = ','.join(str(v) for v in indexes)
                T.insert((str(j) + ".0"), "Line -> " + str(j + 1) + " Col -> " + str(col) + " Text ->" + text[j])
                #print("highlight", str(index)+"."+str(indexes[0]+32), str(index)+"."+str(len(string_to_search)+indexes[0]+32))
                for k in range(len(indexes)):
                    T.tag_add("highlight", str(index)+"."+str(indexes[k]+len("Line -> " + str(j + 1) + " Col -> " + str(col) + " Text ->")), str(index)+"."+str(len(string_to_search)+indexes[k]+len("Line -> " + str(j + 1) + " Col -> " + str(col) + " Text ->")))
                    T.tag_config("highlight", background="green", foreground="yellow")
                T.grid(row=500)
                index=index+1
       

# This is the Implementation of the Rabin Carp
def Rabin_CarpImplementation(files,string_to_search,match_whole_word,match_case):
    # Driver program to test the above function
    for i in range(len(files)):
        # Create an instance of Tkinter frame

        win = tkinter.Tk()
        win.geometry("1000x1000")
        win.title("KMP Result")
        text = []
        T = tkinter.Text(win, height=105, width=80)
        T.insert(str(i) + ".0", str(files[i].name + "\n"))
        #Readlines returns a list of text
        text = (files[i].readlines())
        #print(text)
        if(text != None):
            text[-1] = text[-1]+"\n"
        #print(text)
        index = 1
        #Applying Algo on each Line
        for j in range(len(text)):
            indexes = []
            # Conditions to Consider
            if (match_whole_word.get() == 1) & (match_case.get() == 0):
                #print("Match whole word only [Checked] and Match case [Unchecked]")
                # Getting the possiblites of lower and Upper Cases
                lists = (map(''.join, itertools.product(*zip(string_to_search.upper(), string_to_search.lower()))))
                lists = (list(lists))
                for l in range(len((lists))):
                    Rabin_Carp(text[j],lists[l],1,indexes)
            elif (match_whole_word.get() == 0) & (match_case.get() == 1):
                #print("Match whole word only [Unchecked] and Match case [Checked]")
                Rabin_Carp(text[j],string_to_search,0,indexes)
            elif (match_whole_word.get() == 0) & (match_case.get() == 0):
                #print("Match whole word only [Unchecked] and Match case [Unchecked]")
                # Getting the possiblites of lower and Upper Cases
                lists = (map(''.join, itertools.product(*zip(string_to_search.upper(), string_to_search.lower()))))
                lists = (list(lists))
                print(lists)
                for l in range(len((lists))):
                    Rabin_Carp(text[j],lists[l],0,indexes)
            else:
                #print("Match whole word only [Checked] and Match case [checked]")
                Rabin_Carp(text[j],string_to_search,1,indexes)
            #print(indexes)
            # Making the Box
            if (indexes):
                # T.insert((str(j)+".0"),"Line -> " + str(j+1)  + " Index No -> " + str(indexes)[1:-1] + " Text ->" + text[j] )
                col = ','.join(str(v) for v in indexes)
                T.insert((str(j) + ".0"), "Line -> " + str(j + 1) + " Col -> " + str(col) + " Text ->" + text[j])
                # print("highlight", str(index)+"."+str(indexes[0]+32), str(index)+"."+str(len(string_to_search)+indexes[0]+32))
                for k in range(len(indexes)):
                    T.tag_add("highlight",
                              str(index) + "." + str(indexes[k] + len("Line -> " + str(j + 1) + " Col -> " + str(col) + " Text ->")),
                              str(index) + "." + str(
                                  len(string_to_search) + indexes[k] + len("Line -> " + str(j + 1) + " Col -> " + str(col) + " Text ->")))
                    T.tag_config("highlight", background="green", foreground="yellow")
                T.grid(row=500)
                index = index + 1
       


#---------------------------- RABIN CARP ALGO FROM INTERNET START HERE ----------------------------#
def rehash(prev_hash, first, last, d):
    """Returns new hash if first char removed and last char is added."""
    return ((prev_hash - ord(first) * d) << 1) + ord(last)

def Rabin_Carp(txt, pat,length_match,matches):
    """Returns list of indices in text string which matches given pattern."""
    hy = 0  # Hash of running text frame
    hx = 0  # Hash of pattern
    n = len(txt)
    m = len(pat)

    if m > n:
        return []

    d = 1 << m - 1

    for i in range(m):
        hx = (hx << 1) + ord(pat[i])
        hy = (hy << 1) + ord(txt[i])

    # Search
    j = 0
    while j <= n - m:
        if hx == hy and pat == txt[j:j + m]:
            if (length_match == 1):
                if ((txt[j + len(pat)] == " " or txt[j + len(pat)] == "") and txt[j - 1] == " "):
                    matches.append(j)
            else:
                matches.append(j)
        if j < n - m:
            hy = rehash(hy, txt[j], txt[j + m], d)
        j += 1
#---------------------------- RABIN CARP ALGO FROM INTERNET END HERE----------------------------#

def Brute_ForceImplementation(files,string_to_search,match_whole_word,match_case):
    for i in range(len(files)):
        # Create an instance of Tkinter frame
        win = tkinter.Tk()
        win.geometry("1000x1000")
        win.title("KMP Result")
        text = []
        T = tkinter.Text(win, height=500, width=500)
        T.insert(str(i) + ".0", str(files[i].name + "\n"))
        #Readlines returns a list of text
        text = (files[i].readlines())
        #print(text)
        if(text != None):
            text[-1] = text[-1]+"\n"
        #print(text)
        index = 1
        #Applying Algo on each Line
        for j in range(len(text)):
            indexes = []
            # Conditions to Consider
            if (match_whole_word.get() == 1) & (match_case.get() == 0):
                #print("Match whole word only [Checked] and Match case [Unchecked]")
                # Getting the possiblites of lower and Upper Cases
                lists = (map(''.join, itertools.product(*zip(string_to_search.upper(), string_to_search.lower()))))
                lists = (list(lists))
                for l in range(len((lists))):
                    Brute_Force(lists[l], text[j],1,indexes)
            elif (match_whole_word.get() == 0) & (match_case.get() == 1):
                #print("Match whole word only [Unchecked] and Match case [Checked]")
                Brute_Force(string_to_search,text[j],0,indexes)
            elif (match_whole_word.get() == 0) & (match_case.get() == 0):
                #print("Match whole word only [Unchecked] and Match case [Unchecked]")
                # Getting the possiblites of lower and Upper Cases
                lists = (map(''.join, itertools.product(*zip(string_to_search.upper(), string_to_search.lower()))))
                lists = (list(lists))
                print(lists)
                for l in range(len((lists))):
                    Brute_Force(lists[l], text[j],0,indexes)
            else:
               # print("Match whole word only [Checked] and Match case [checked]")
                Brute_Force(string_to_search, text[j],1,indexes)
            #print(indexes)
            # Making the Box
            if (indexes):
                # T.insert((str(j)+".0"),"Line -> " + str(j+1)  + " Index No -> " + str(indexes)[1:-1] + " Text ->" + text[j] )
                col = ','.join(str(v) for v in indexes)
                T.insert((str(j) + ".0"), "Line -> " + str(j + 1) + " Col -> " + str(col) + " Text ->" + text[j])
                # print("highlight", str(index)+"."+str(indexes[0]+32), str(index)+"."+str(len(string_to_search)+indexes[0]+32))
                for k in range(len(indexes)):
                    T.tag_add("highlight",
                              str(index) + "." + str(indexes[k] + len("Line -> " + str(j + 1) + " Col -> "+ str(col) + " Text ->")),
                              str(index) + "." + str(
                                  len(string_to_search) + indexes[k] + len("Line -> " + str(j + 1) + " Col -> "+ str(col) + " Text ->")))
                    T.tag_config("highlight", background="green", foreground="yellow")
                T.grid(row=500)
                index = index + 1
       
 


#-----------------------------Brute Force from the internet ===================================#
def Brute_Force(pat, txt,length_match,indexes):
    M = len(pat)
    N = len(txt)
    # A loop to slide pat[] one by one */
    for i in range(N - M + 1):
        j = 0
        # For current index i, check
        # for pattern match */
        while (j < M):
            if (txt[i + j] != pat[j]):
                break
            j += 1
        if (j == M):
            #print("Pattern found at index ", i)
            if (length_match == 1):
                if ((txt[i + len(pat)] == " " or txt[i + len(pat)] == "") and txt[i - 1] == " "):
                    indexes.append(i)
            else:
                indexes.append(i)

#-----------------------------Brute Force from the internet  END here===================================#
# This function will Run when the User will Upload File
def UploadAction(algo_to_run,match_whole_word,match_case,string_to_search):
    # Selecting the Files
    filez = filedialog.askopenfilenames(parent=app, title='Choose a file')
    # Printing the Files Selected
    print('Selected:', filez)
    # Making a list to hold the Files Descriptor
    # Files list/array contains the Files Selected
    files=[]
    for i in range(len(filez)):
        files.append(open(filez[i]))


    #String to Search
    #string_to_search = "test"
    print("String to Search -> " + str(string_to_search.get()))
    #NOTE THESE VARIABLES
    print(match_whole_word.get())
    print(match_case.get())
    if (match_whole_word.get() == 1) & (match_case.get() == 0):
       print("Match whole word only [Checked] and Match case [Unchecked]")
    elif (match_whole_word.get() == 0) & (match_case.get() == 1):
        print("Match whole word only [Unchecked] and Match case [Checked]")
    elif (match_whole_word.get() == 0) & (match_case.get() == 0):
        print("Match whole word only [Unchecked] and Match case [Unchecked]")
    else:
        print("Match whole word only [Checked] and Match case [checked]")
    # You can use Above Variables to pass onto Your Function


    if(algo_to_run.get() == "Brute Force"):
        Brute_ForceImplementation(files,string_to_search.get(),match_whole_word,match_case)

    elif(algo_to_run.get() == "Rabin-Carp"):
        Rabin_CarpImplementation(files,string_to_search.get(),match_whole_word,match_case)

    elif(algo_to_run.get() == "KMP"):
        KMPImplementation(files,string_to_search.get(),match_whole_word,match_case)


#Start Function For Implementing the GUI
def gui():

    # Naming the title

    app.title("String Matching")
    app.geometry('700x300')
    app.config(bg="DarkOliveGreen1")
    #app.wm_attributes('-transparentcolor','black')

    # Making dummy Label to maange GUI a bit
    dummy_label = tkinter.Label(app, text="                 ")
    #Some required Labels
    algo_label = tkinter.Label(app, text="Algorithm:  ",font=('Helvatical bold',14,'bold'),relief="sunken" , bg = 'DarkOliveGreen3')
    case_label = tkinter.Label(app, text="Select Option:  ", font=('Helvatical bold', 14,'bold'),relief="sunken" ,bg = 'DarkOliveGreen3')
   
    #dummy_label.grid(row=1,column=1)
    algo_label.grid(row=4,column=2)
    #dummy_label.grid(row=3,column=1)
    
    hell = tkf.Font(family='Helvetica', size =10, weight= 'bold')
    # Options to Select the Algorithm From
    choices_algo = ['Brute Force' , 'Rabin-Karp', 'KMP']
    algo_to_run = StringVar(app)
    algo_to_run.set(choices_algo[0])
    w = OptionMenu(app, algo_to_run,*choices_algo, )
    w.config(font = hell,bg = 'DarkOliveGreen4')
    w["menu"].config(font = hell,bg = 'DarkOliveGreen1')
    w.grid(row=6, column=3)
    #w.pack()
    # Options to Select the Case From Algorithm
    match_whole_word = tkinter.IntVar()
    match_case = tkinter.IntVar()

    c2 = tkinter.Checkbutton(app, text='Match Case',font=('Helvatical bold', 10,'bold'), bg = 'DarkOliveGreen1',variable=match_case, onvalue=1, offvalue=0)
    c1 = tkinter.Checkbutton(app, text='Match whole word only',font=('Helvatical bold', 10,'bold'), bg = 'DarkOliveGreen1',variable=match_whole_word, onvalue=1, offvalue=0)
    case_label.grid(row=25,column=2)
    c2.grid(row=26,column=3)
    c1.grid(row=27,column=3)
    
    #dummy_label.grid(row=30)
    enter_string_label = tkinter.Label(app, text="Enter String", font=('Helvatical bold', 14,'bold'),relief="sunken" ,bg = 'DarkOliveGreen3')
    enter_string_label.grid(row=32,column=2)
    #Textbox to take the User INput
    string_to_search = tkinter.Entry(app)
    string_to_search.insert(0,'Text')
    string_to_search.grid(row=34,column=3)
    #A button that decides which Algorithm to Run
    button2 = tkinter.Button(app, text='Start Searching',font=('Helvatical bold', 10,'bold'),bg = 'DarkOliveGreen4',command=lambda: UploadAction(algo_to_run,match_whole_word,match_case,string_to_search))
    button2.grid(row=38,column=6)
    #button2.pack()


    # A main loop to Run
    app.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gui()

