def extract_date_place_live(a):
    stopwords = ['what','who','is','at','is','he','the','that','event','this','payment','agreement','default','payment''whereas','tenant','landlord','card','schedule','aadhaar','No','herein','hereunder','rupees','january','february','march','april','may','June','july','august','september','october','november','december']
    from nltk.tag import pos_tag
    tagged_sent = pos_tag(a.split())
    #print(tagged_sent)
    propernouns = [word for word,pos in tagged_sent if pos == 'NNP' or pos == 'CD']
    for i in propernouns:
        resultwords  = [word for word in propernouns if word.lower() not in stopwords]
        #print(resultwords)
    result = ' '.join(resultwords)
    return (result)
def extract_landlord_live(a):
    from nltk.tag import pos_tag
    for i in a.split():
        #print(i)
        tagged_sent = pos_tag(a.split(","))
        
        propernouns = [word for word,pos in tagged_sent if pos == 'NNP' or pos == 'JJ' or pos == 'VBZ']
    result = " ".join(propernouns)
    #print(tagged_sent)
    return(result)
def extract_tenant_live(a):
    from nltk.tag import pos_tag
    for i in a.split():
        tagged_sent = pos_tag(a.split())
        
        propernouns = [word for word,pos in tagged_sent if pos == 'NNP' or pos == 'JJ' or pos == 'VBZ' or pos =='CD' ]
    #print(tagged_sent)
    result = " ".join(propernouns)
    return(result)
def actual_house_landlord(a):
    from nltk.tag import pos_tag
    tagged_sent = pos_tag(a.split(" "))
    #print(tagged_sent)
    stopwords = ['is','schedule','said']
    propernouns = [word for word,pos in tagged_sent if pos == 'NNP' or pos == 'JJ' or pos == 'VBZ' or pos == 'CD']
    for i in propernouns:
        resultwords  = [word for word in propernouns if word.lower() not in stopwords]
    result = " ".join(resultwords)
    return(result)
def details(a):
    stopwords = ['what','who','is','a','at','is','he','whereas','tenant','landlord','card','schedule','aadhaar','No','herein','hereunder','rupees','licensee','spaces','scheduled','premises','license','available','such','have','temporary','permissive','clear','fresh','own','leave','property','licensor','ground']
    from nltk.tag import pos_tag
    tagged_sent = pos_tag(a.split())
    #print(tagged_sent)
    propernouns = [word for word,pos in tagged_sent if pos == 'NNP' or pos == 'CD' or pos =='NNS' or pos =="JJ"]
    for i in propernouns:
        resultwords  = [word for word in propernouns if word.lower() not in stopwords]
        #print(resultwords)
        result = ' '.join(resultwords)
    return (result)
def extract_tds(a):
    import re
    regex = re.compile('@')
    b=a.split()
    for i in range(len(b)):
        #print(b[i])
        #count= count+1
        #print(count)
        if b[i].lower() == 'advance':
            print(b[i] + " " + b[i+1] + " " + b[i+2] + " " + b[i+3] + " " + b[i+4])
        if(regex.search(b[i]) == None): 
            continue
        else:
            return("TDS IS " + b[i+1])
def live_and_license_summary(lines):
    import docx2txt
    #MY_TEXT = docx2txt.process("Chandan Dhar_RUEDA_Leave_&_License_Agreement_12-06-19_11-05-20_Legal.docx")
    #with open("draft1.txt", "w") as text_file:
        #print(MY_TEXT, file=text_file)
    #f = open("draft1.txt")
    #lines = f.readlines()
    count=0
    b=0
    l=0
    t=0
    string = ''
    for line in lines:
        #print(line)
        #print(len(line))
        if (len(line)>30):
            #x+=1
            a = line.split()
            for i in range (len(a)):
                if a[i]!="WITHNESS"  :
                    if a[i]=="LEAVE" and a[i+1]=="AND" and a[i+2]=="LICENSE":
                        #print("THE DATE AND PLACE OF AGREEMENT: ")
                        string += "\n" + extract_date_place_live(line)
                        break;
                    elif a[i] == "FIRST" and a[i+1] == "PART" and l==0:
                        #print("LICENSOR: ")
                        l=1
                        string += "\n" + extract_landlord_live(line)
                        break;
                    elif a[i] == "SECOND" and a[i+1] == "PART" and t==0:
                        #print("LICENSEE: ")
                        string += "\n" + extract_tenant_live(line)
                        t=1
                        break
                    elif a[i] == "seized" and a[i+1] == "and" and a[i+2] == "possessed":
                        #print("ACTUAL HOUSE LICENSOR: ")
                        string += "\n" + actual_house_landlord(line)
                        break
                    elif a[i] == "accommodation" and a[i+1] == "arrangement":
                        print("ACCOMODATION DETAILS: ")
                        details(line)
                        break
                    elif a[i] == "one" and a[i+1] == "time" and a[i+2] == "interest":# and a[i+3] == "free ":
                        #print("CHARGES DETAILS: ")
                        string += "\n" + details(line)
                        break
                    elif a[i] == "deduction" and a[i+1] == "of" and a[i+2] == "TDS":
                        #print("TDS CHARGES: ")
                        string += "\n" + extract_tds(line)
                        break
    return string
