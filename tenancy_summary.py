def extract_date(a):
    b= a.split()
    for i in range(len(b)):
        if b[i] == ( "at" or "place") :
            break
    #print("THE NAME OF THE PLACE IS :" + b[i+1])
    from word2number import w2n
    for i in range (len(a)) :
        if a[i] == "." :
            b= a[:i] + " "
    #print(b)
    #c = w2n.word_to_num(b)
    for i in range( len(a)):
        if (a[i])== ",":
            d= a[:i+1] + a[i+2 : ]
    import datefinder
    #string_with_dates = "THIS AGREEMENT made at Kolkata on this 1st day of September, "
    matches = datefinder.find_dates(a)
    #print(matches)
    for match in matches:
        continue
        #print (match)
    v= str(match)
    m= v.split()
    #print(m[0])
    #print(m[1])
    p = str(m[0])
    r = p.split("-")
    import inflect
    q = inflect.engine()
    return (p)
    
    
def extract_landlord(a):
    from nltk.tag import pos_tag
    for i in a.split():
        #print(i)
        tagged_sent = pos_tag(a.split(","))
        #print(tagged_sent)
        propernouns = [word for word,pos in tagged_sent if pos == 'NNP' or pos == 'JJ' or pos == 'VBZ']
    result = " ".join(propernouns)
    return (result)
    
    
def extract_tenant(a):
    from nltk.tag import pos_tag
    for i in a.split():
        tagged_sent = pos_tag(a.split(","))
        #print(tagged_sent)
        propernouns = [word for word,pos in tagged_sent if pos == 'NNP' or pos == 'JJ' or pos == 'VBZ']
    result = " ".join(propernouns)
    return (result)
    
    
def actual_house_landlord(a):
    tagged_sent = pos_tag(a.split(" "))
    #print(tagged_sent)
    propernouns = [word for word,pos in tagged_sent if pos == 'NNP' or pos == 'JJ' or pos == 'VBZ' or pos == 'CD']
    result = " ".join(propernouns)
    return (result)
    
    
def details(a):
    stopwords = ['what','who','is','a','at','is','he','whereas','tenant','landlord','card','schedule','aadhaar','No','herein','hereunder','rupees']
    from nltk.tag import pos_tag
    tagged_sent = pos_tag(a.split())
    #print(tagged_sent)
    propernouns = [word for word,pos in tagged_sent if pos == 'NNP' or pos == 'CD' or pos =='NNS']
    for i in propernouns:
        resultwords  = [word for word in propernouns if word.lower() not in stopwords]
        #print(resultwords)
        result = ' '.join(resultwords)
    return (result)
    
    
def notice(a):
    stopwords = ['what','who','is','a','at','is','he','whereas','tenant','landlord','card','schedule','aadhaar','No','herein','hereunder']
    from nltk.tag import pos_tag
    tagged_sent = pos_tag(a.split())
    #print(tagged_sent)
    propernouns = [word for word,pos in tagged_sent if pos == 'CD' or pos == 'NNS' or pos == 'RB']
    for i in propernouns:
        resultwords  = [word for word in propernouns if word.lower() not in stopwords]
    for i in range (len(resultwords)):
        if(resultwords[i]=="notice"):
            z = resultwords[:i+1]
    result = ' '.join(z)
    return (result)
    
    
def prior(a):
    stopwords = ['what','who','is','a','at','is','he','whereas','tenant','landlord','card','schedule','aadhaar','No','herein','hereunder','parties']
    from nltk.tag import pos_tag
    tagged_sent = pos_tag(a.split())
    #print(tagged_sent)
    propernouns = [word for word,pos in tagged_sent if pos == 'CD' or pos =='NNS'  ]
    for i in propernouns:
        resultwords  = [word for word in propernouns if word.lower() not in stopwords]
        #print(resultwords)
        result = ' '.join(resultwords)
    return (result)
    
    
def wife(a):
    stopwords = ['what','who','is','a','at','is','he','whereas','tenant','landlord','card','schedule','aadhaar','No','herein','hereunder','ground','top','bed','rooms','floor','first']
    from nltk.tag import pos_tag
    tagged_sent = pos_tag(a.split())

    #print(tagged_sent)

    propernouns = [word for word,pos in tagged_sent if pos == 'NNP']
    for i in propernouns:
        resultwords  = [word for word in propernouns if word.lower() not in stopwords]
        #print(resultwords)
        result = ' '.join(resultwords)
    return (result)
    
    
def automatic(a):
    stopwords = ['what','who','is','at','is','he','the','that','event','this','payment','agreement','default','payment''whereas','tenant','landlord','card','schedule','aadhaar','No','herein','hereunder','rupees']
    from nltk.tag import pos_tag
    tagged_sent = pos_tag(a.split())
    #print(tagged_sent)
    propernouns = [word for word,pos in tagged_sent if pos == 'NN' or pos == 'DT']
    for i in propernouns:
        resultwords  = [word for word in propernouns if word.lower() not in stopwords]
        #print(resultwords)
        result = ' '.join(resultwords)
    return result


#def tenancy_summary(lines):
    #import docx2txt
    #MY_TEXT = docx2txt.process("Draft format of a TENANCY_AGREEMENT.docx")
    #with open("draft.txt", "w") as text_file:
        #print(MY_TEXT, file=text_file)
    #f = open("draft.txt")
    #lines = fetched_data.readlines()
    #count=0
    #b=0
    #l=0
    #t=0
    #string = ''
    #for line in lines:
        #a = line.split()
        #if (len(line)>20):
            #for i in range (len(a)):
                #if a[i]=="WITNESS" or a[i]=="SCHEDULE" or a[i]=="PROPERTY" or a[i] == "REFERRED" :
                    #b=1
                #if a[i] == "AGREEMENT"  :
                    #print("THE DATE OF AGREEMENT: ")
                    #string += "\n" + extract_date(line)
                    #break;
                #elif a[i] == "ONE" and a[i+1] == "PART":
                    #print("LANDLORD: ")
                    #string += "\n" + extract_landlord(line)
                    #break;
                #elif a[i] == "OTHER" and a[i+1] == "PART":
                   # print("TENANT: ")
                    #string += "\n" + extract_tenant(line)
                   # break
                #elif a[i]== "seized": 
                    #print("THE ACTUAL PLACE OF LANDLORD:")
                    #actual_house_landlord(line)
                    #break
                #elif a[i]=="Monthly" and a[i+1] == "Rent":
                    #print("TOTAL DETAILS FOR THE ROOM AND RENT: ")
                    #string += "\n" + details(line)
                   # break
                #elif a[i] == "notice":
                    #print("THE MINIMUM TIME TO GIVE BEFORE LEAVING: ")
                    #string += "\n" + notice(line)
                    #break
               # elif a[i]== "mutual":
                    #print("THE TIME TO CONTINUE: ")
                    #string += "\n" + prior(line)
                   # break
               # elif a[i] == "surrender":
                    #print("THE TEREMINATION TIME: ")
                    #string += "\n" + extract_date(line)
                    #break
                #elif a[i] == "wife":
                    #print("THE NAME OF THE TENANT'S WIFE IS: ")
                    #string += "\n" + wife(line)
                    #break
                #elif a[i]== 'automatic':
                    #print("THE TIME FOR AUTOMATIC TERMISSION IS: ")
                    #string += "\n" + automatic(line)
            #if b==1:
                #break
    #print(len(line))
    #if len(line)>20:
        #count+=1
        #print (line)    
#print(count)
    #return string
def tenancy_summary(lines):
    import docx2txt
    #MY_TEXT = docx2txt.process("Draft format of a TENANCY_AGREEMENT.docx")
    #with open("draft.txt", "w") as text_file:
        #print(MY_TEXT, file=text_file)
    #f = open("draft.txt")
    #lines = fetched_data.readlines()
    count=0
    b=0
    l=0
    t=0
    string = ''
    for line in lines:
        a = line.split()
        if (len(line)>30):
            for i in range (len(a)):
                if a[i]=="WITNESS" or a[i]=="SCHEDULE" or a[i]=="PROPERTY" or a[i] == "REFERRED" :
                    b=1
                if a[i] == "AGREEMENT" and a[i+1] == "made"  :
                    print("THE DATE OF AGREEMENT: ")
                    string += "\n" + extract_date(line)
                    break;
                elif a[i] == "ONE" and a[i+1] == "PART":
                    print("LANDLORD: ")
                    string += "\n" + extract_landlord(line)
                    break;
                elif a[i] == "OTHER" and a[i+1] == "PART":
                    print("TENANT: ")
                    string += "\n" + extract_tenant(line)
                    break
                #elif a[i]== "seized": 
                    #print("THE ACTUAL PLACE OF LANDLORD:")
                    #actual_house_landlord(line)
                    #break
                elif a[i]=="Monthly" and a[i+1] == "Rent":
                    print("TOTAL DETAILS FOR THE ROOM AND RENT: ")
                    string += "\n" + details(line)
                    break
                elif a[i] == "months" and a[i+1] == "notice" :
                    print("THE MINIMUM TIME TO GIVE BEFORE LEAVING: ")
                    string += "\n" + notice(line)
                    break
                elif a[i]== "mutual" and a[i+1] == "understanding" :
                    print("THE TIME TO CONTINUE: ")
                    string += "\n" + prior(line)
                    break
                elif a[i] == "surrender" and a[i+1] == "to" :
                    print("THE TEREMINATION TIME: ")
                    string += "\n" + extract_date(line)
                    break
                elif a[i] == "wife":
                    print("THE NAME OF THE TENANT'S WIFE IS: ")
                    string += "\n" + wife(line)
                    break
                elif a[i]== 'automatic':
                    print("THE TIME FOR AUTOMATIC TERMISSION IS: ")
                    string += "\n" + automatic(line)
                elif a[i]!="WITHNESS"  :
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
            if b==1:
                break
    #print(len(line))
    #if len(line)>20:
        #count+=1
        #print (line)    
#print(count)
    return string
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
