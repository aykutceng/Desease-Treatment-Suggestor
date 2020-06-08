import string
import re
import nltk
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem.snowball import SnowballStemmer


idenditify = ['\033[92m'+'Ad   : Aykut'+'\033[0m','\033[92m'+'Soyad: Cengiz'+'\033[0m','\033[92m'+'No   : 503020190030'+'\033[0m','\033[92m'+'<Information Retrieval Final Project>'+'\033[0m']


lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
porter = PorterStemmer()
snowy = SnowballStemmer("english")
translator = str.maketrans('','', string.punctuation)

Tk().withdraw()

baslıklar = ['doga','bilim','hukuk','din','ekonomi','is','moda','siyaset','spor']

diseaseAllergie = dict()
diseaseAnxiety = dict()
diseaseBipolar = dict()
diseaseBrainTumour = dict()
diseaseBreastCancer = dict()
diseaseCommonCold = dict()
diseaseDiabet = dict()
diseaseDepression = dict()
diseaseDownsSyndrome = dict()
diseaseFlu = dict()
diseaseHighCholesterol = dict()
diseaseHIV = dict()
diseaseInsominia = dict()
diseaseLungCancer = dict()
diseaseMigrain = dict()
diseaseSunburn = dict()
diseasePercentage = dict()
disease = ["allergie","anxiety","bipolar","braintumor","breastcancer","commoncold","diabet","depression","downssyndrome",
           "flue","highcholesterol","hiv","insominia","lungcancer","migrain","sunburn"]
diseaseAllergie = {"sneezing":"Allergie","runny nose":"Allergie","blocked nose":"Allergie","red eyes":"Allergie",
                   "itchy eyes":"Allergie","watery eyes":"Allergie","wheezing":"Allergie","coughing":"Allergie",
                   "itchy rash":"Allergie"}
diseaseAnxiety = {"restlessness":"Anxiety","sense of dread":"Anxiety","feeling constantly on edge":"Anxiety",
                  "difficulty concentrating":"Anxiety","irritability":"Anxiety","dizziness":"Anxiety","tiredness":"Anxiety",
                  "muscle aches and tension":"Anxiety","irregular heartbeat":"Anxiety","trembling or shaking":"Anxiety",
                  "dry mouth":"Anxiety","excessive sweating":"Anxiety","shortness of breath":"Anxiety","stomach ache":"Anxiety",
                  "feeling sick":"Anxiety","headache":"Anxiety","pins and needles":"Anxiety",
                  "difficulty falling or staying asleep":"Anxiety"}
diseaseBipolar = {"feeling sad,hopeless or irritable":"Bipolar","lacking energy":"Bipolar",
                  "loss of interest in activities":"Bipolar","feelings of emptiness or worthlessness":"Bipolar",
                  "feelings of guilt and despair":"Bipolar","feeling pessimistic about everything":"Bipolar",
                  "self-doubt":"Bipolar","lack of appetite":"Bipolar","difficulty sleeping":"Bipolar",
                  "waking up early":"Bipolar","suicidal thoughts":"Bipolar","talking very quickly":"Bipolar",
                  "feeling very happy":"Bipolar","feeling full of energy":"Bipolar","not eating":"Bipolar",
                  "being easily distracted":"Bipolar"}
diseaseBrainTumour = {"persistent headaches":"Brain Tumour","seizures":"Brain Tumour","persistent nausea":"Brain Tumour",
                      "vomiting":"Brain Tumour", "drowsiness":"Brain Tumour","mental or behavioural changes":"Brain Tumour",
                      "progressive weakness":"Brain Tumour", "vision problem":"Brain Tumour","speech problem":"Brain Tumour"}
diseaseBreastCancer = {"bone pain":"Breast Cancer","swelling of the lymph nodes":"Breast Cancer",
                       "shortness of breath":"Breast Cancer","nipple retraction":"Breast Cancer","nipple ulceration":"Breast Cancer",
                       "nipple discharge":"Breast Cancer","feeling unusally tired":"Breast Cancer","itchy skin":"Breast Cancer"}
diseaseCommonCold = {"sore throat":"Common Cold","blocked nose":"Common Cold","runny nose":"Common Cold",
                     "sneezing":"Common Cold","hoarse voice":"Common Cold","feeling unwell":"Common Cold","headache":"Common Cold",
                     "high temperature":"Common Cold","fever":"Common Cold","earache":"Common Cold","muscle pain":"Common Cold",
                     "loss of taste":"Common Cold","loss of smell":"Common Cold"}
diseaseDiabet = {"feeling very thirsty":"Diabete","feeling very tired":"Diabete","weight loss":"Diabete","loss of muscle bulk":"Diabete",
                 "urinating more frequently":"Diabete","blurred vision":"Diabete","cuts that heal slowly":"Diabete"}
diseaseHIV = {"fever":"HIV","sore throat":"HIV","body rash":"HIV","tiredness":"HIV","joint pain":"HIV","muscle pain":"HIV",
              "swollen glands":"HIV","weight loss":"HIV","chronic diarrhoea":"HIV","night sweats":"HIV","skin problems":"HIV",
              "recurrent infections":"HIV","serious life illnesses":"HIV"}
diseaseInsominia = {"difficult to fall asleep":"Insominia","lie awake for long periods at night":"Insominia",
                    "waking up several time during the night":"Insominia","not feel refreshed when you get up":"Insominia",
                    "feel tired":"Insominia","irritable":"Insominia"}
diseaseMigrain = {"headache":"Migrain","nausea":"Migrain","vomiting":"Migrain","vomiting":"Migrain","increased sensitivity":"Migrain"
                  ,"sweating":"Migrain","poor concentration":"Migrain","diarrhoea":"Migrain","abdominal pain":"Migrain"
                  ,"visual problems":"Migrain","feeling dizzy":"Migrain","difficulty speaking":"Migrain"}

sympList = []

for a in diseaseAllergie:
    sympList.append(a)
for a in diseaseAnxiety:
    sympList.append(a)
for a in diseaseBipolar:
    sympList.append(a)
for a in diseaseBrainTumour:
    sympList.append(a)
for a in diseaseBreastCancer:
    sympList.append(a)
for a in diseaseCommonCold:
    sympList.append(a)
for a in diseaseDiabet:
    sympList.append(a)
for a in diseaseHIV:
    sympList.append(a)
for a in diseaseInsominia:
    sympList.append(a)
for a in diseaseMigrain:
    sympList.append(a)
sympList = list(dict.fromkeys(sympList))
sympList = sorted(sympList)
    
print(*sympList,sep='\n')

sympName = []
val = None
def sympNo():
    numberofSymptomps = input("\nPlease enter how many symptoms you have: ")
    try:
        val = int(numberofSymptomps)
        print("\nCORRECT! Input is integer.\n")
        return val
    except ValueError:
        print("Please enter only integer!")
        return sympNo()
val = sympNo() 

def fixWrongInput():
    nameofSymptomps = input("Please enter your symptomps:  ")
    nameofSymptomps = nameofSymptomps.lower()
    if nameofSymptomps in sympList:
        sympName.append(nameofSymptomps)
    else:
        print("Please enter a valid symptom from list")
        return fixWrongInput()

for sNo in range(0,val):
    fixWrongInput()

allergie = 0
anxiety = 0
bipolar = 0
braintumor = 0
breastcancer = 0
commoncold = 0
diabet = 0
hiv = 0
insomnia = 0
migraine = 0

for x in sympName:
    if x in diseaseAllergie:
        allergie += 1
    if x in diseaseAnxiety:
        anxiety += 1
    if x in diseaseBipolar:
        bipolar += 1
    if x in diseaseBrainTumour:
        braintumor += 1
    if x in diseaseBreastCancer:
        breastcancer += 1
    if x in diseaseDiabet:
        diabet += 1
    if x in diseaseHIV:
        hiv += 1
    if x in diseaseInsominia:
        insomnia += 1
    if x in diseaseMigrain:
        migraine += 1
y = len(sympName)
total = allergie + anxiety + bipolar + braintumor + breastcancer + commoncold + diabet + hiv + insomnia + migraine
allergie /= y
allergie *= 100

anxiety /= y
anxiety *= 100

bipolar /= y
bipolar *= 100

braintumor /= y
braintumor *= 100

breastcancer /= y
breastcancer *= 100

commoncold /= y
commoncold *= 100

diabet /= y
diabet *= 100

hiv /= y
hiv *= 100

insomnia /= y
insomnia *= 100

migraine /= y
migraine *= 100
diseaseCount = [allergie,anxiety,bipolar,braintumor,breastcancer,commoncold,diabet,hiv,insomnia,migraine]
diseasePercentage = {"Allergies":round(allergie,2),"Anxiety":round(anxiety,2),"Bipolar":round(bipolar,2),
                     "Brain Tumour":round(braintumor,2),"Breast Cancer":round(breastcancer,2),"Common Cold":round(commoncold,2)
                     ,"Diabete":round(diabet,2),"HIV":round(hiv,2),"Insomnia":round(insomnia,2),"Migraine":round(migraine,2)}



z = 0
for w in diseaseCount:
    if w > 0:
        z += 1
if z >= 4:
    print("\nThere are too many disease determined in according to your symptoms. Please get a professional help determining your desease and treatment\n")
else:
    print("\nYour possible matches has been listed below: \n")
    j = 1
    for w in diseasePercentage:
        if diseasePercentage[w] > 0:
            print("\033[1m"+str(j)+"\033[0m","\033[1m"+".)"+"\033[0m","\033[1m"+w+"\033[0m","\033[1m"+": "+"\033[0m",diseasePercentage[w],"% match")
            j += 1
            if w == "Allergies":
                print("\033[91m"+"#Recommendation:"+"\033[0m","The treatment for an allergy depends on what you're allergic to. In many cases, your GP will be able to offer advice and treatment. They will advise you about taking steps to avoid exposure to the substance you are allergic to, and can recommend medication to control your symptoms. For detail:","\033[94m"+"\n https://www.nhsinform.scot/illnesses-and-conditions/immune-system/allergies#treating-allergies \n"+"\033[0m")
            if w == "Anxiety":
                print("\033[91m"+"#Recommendation:"+"\033[0m","Generalised anxiety disorder (GAD) is a long-term condition, but a number of different treatments can help. Before you begin any form of treatment, your GP should discuss all your treatment options with you. They should outline the pros and cons of each and make sure you are aware of any possible risks or side effects. With your GP, you can make a decision on the treatment most suited to you, taking into account your personal preferences and circumstances. If you have other problems alongside GAD, such as depression and drug or alcohol misuse, these may need to be treated before having treatment specifically for GAD. For detail:","\033[94m"+"\n https://www.nhsinform.scot/illnesses-and-conditions/mental-health/anxiety \n"+"\033[0m")
            if w == "Bipolar":
                print("\033[91m"+"#Recommendation:"+"\033[0m","If a person isn't treated, episodes of bipolar-related mania can last for between three and six months. Episodes of depression tend to last longer, for between six and 12 months. However, with effective treatment, episodes usually improve within about three months. Most people with bipolar disorder can be treated using a combination of different treatments. For detail:","\033[94m"+"\n https://www.nhsinform.scot/illnesses-and-conditions/mental-health/bipolar-disorder \n"+"\033[0m")
            if w == "Brain Tumour":
                print("\033[91m"+"#Recommendation:"+"\033[0m","The main treatment for most brain tumours is surgery, which aims to remove as much of the abnormal tissue as possible. It's not always possible to remove the entire tumour, so further treatment with radiotherapy and/or chemotherapy may be necessary to kill any abnormal cells left behind. For detail:","\033[94m"+"\n https://www.nhsinform.scot/illnesses-and-conditions/cancer/cancer-types-in-adults/brain-tumours \n"+"\033[0m")
            if w == "Breast Cancer":
                print("\033[91m"+"#Recommendation:"+"\033[0m","Treatment for breast cancer in men largely depends on how far the cancer has spread. Most hospitals use multidisciplinary teams (MDTs) to treat men with breast cancer. These are teams of specialists who work together to make decisions about the best way to proceed with your treatment. Deciding which treatment is best for you can often be confusing. Your cancer team will recommend what they think is the ideal treatment option, but the final decision will be yours. Before visiting hospital to discuss your treatment options, you may find it useful to write a list of questions you'd like to ask the specialist. For example, you could ask about the advantages and disadvantages of particular treatments. For detail:","\033[94m"+"\n https://www.nhsinform.scot/illnesses-and-conditions/cancer/cancer-types-in-adults/breast-cancer-male \n"+"\033[0m")    
            if w == "Common Cold":
                print("\033[91m"+"#Recommendation:"+"\033[0m","Until you're feeling better, it may help to drink plenty of fluids to replace those lost from sweating and having a runny nose and to eat healthily – a low-fat, high-fibre diet is recommended, including plenty of fresh fruit and vegetables. For detail:","\033[94m"+"\n https://www.nhsinform.scot/illnesses-and-conditions/infections-and-poisoning/common-cold \n"+"\033[0m")
            if w == "Diabete":
                print("\033[91m"+"#Recommendation:"+"\033[0m","You should therefore visit your GP as soon as possible if you have symptoms, such as feeling thirsty, passing urine more often than usual, and feeling tired all the time. It's also advised to see your GP if you have risk factors of diabetes and are worried about developing diabetes in future. For detail:","\033[94m"+"\n https://www.nhsinform.scot/illnesses-and-conditions/diabetes \n"+"\033[0m")
            if w == "HIV":
                print("\033[91m"+"#Recommendation:"+"\033[0m","Although HIV cannot be cured, it's a very manageable long term condition and effective treatment is available to enable individuals to live a long and healthy life. If you're diagnosed with HIV, you'll be referred to a specialist HIV clinic for treatment, regular monitoring and care. It's recommended that everyone diagnosed with HIV starts treatment shortly after being diagnosed to keep in good health and free of symptoms. Treatment for HIV is generally very well tolerated. Medication, known as antiretrovirals, work by stopping the virus replicating in the body, allowing the immune system to repair itself and preventing further damage. These medicines come in the form of tablets which need to be taken every day. HIV can develop resistance to a single HIV drug very easily, but by taking a combination of different drugs or with support from your doctor in taking your treatment, resistance is less likely. Most people with HIV take a combination of three antiretrovirals (although some people take 1 or 2) and it's vital that the medications are taken every day as recommended by your doctor. For detail:","\033[94m"+"\n https://www.nhsinform.scot/illnesses-and-conditions/immune-system/hiv \n"+"\033[0m")
            if w == "Insomnia":
                print("\033[91m"+"#Recommendation:"+"\033[0m","Insomnia will often improve by making changes to your bedtime habits. If these don't help, your GP may be able to recommend other treatments. If you've had insomnia for more than four weeks, your GP may recommend cognitive and behavioural treatments or suggest a short course of prescription sleeping tablets as a temporary measure. If it's possible to identify an underlying cause of your sleeping difficulties, treating this may be enough to return your sleep to normal.For detail:","\033[94m"+"\n https://www.nhsinform.scot/illnesses-and-conditions/mental-health/insomnia \n"+"\033[0m")
            if w == "Migraine":
                print("\033[91m"+"#Recommendation:"+"\033[0m","There's currently no cure for migraines, although a number of treatments are available to help ease the symptoms. It may take time to work out the best treatment for you. You may need to try different types or combinations of medicines before you find the most effective ones. If you find you can't manage your migraines using over-the-counter medicines, your GP may prescribe something stronger.For detail:","\033[94m"+"\n https://www.nhsinform.scot/illnesses-and-conditions/brain-nerves-and-spinal-cord/migraine \n"+"\033[0m")
                
print(*idenditify,sep='\n')
print("\n")
