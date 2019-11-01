#Pull All AWS SES Identities in given region and list txt and dkim keys
#Use this script to grab the txt verification and dkim keys for each SES domain found in a given region.

import os
import json

#AWS Variables: enter yours here (should match your aws cli profile set up)
AWSregion = "eu-west-1"
AWSprofile = "newcds"

#Grab all SES domains in specified region and return the results as the variable "identities"
listSESIdentites = "aws ses list-identities --profile {0} --region {1}".format(str(AWSprofile), str(AWSregion))
identities = os.popen(listSESIdentites).read()
#Convert "identities" to a JSON dictionary SESIDs_dict
SESIDs_dict = json.loads(identities)
#Import the Identities domain name list to a python array named "Domain_list"
Domain_list = (SESIDs_dict['Identities'])
#Rearrange the list in alphabetical order
Domain_list.sort()

#Loop through the array
for domain_number in range(len(Domain_list)):
    #Set DOMAIN to the domain name current on the looping list
    DOMAIN = (Domain_list[domain_number])
    #Build the command to verify-domain-idenity by domain and produce copyable txt verification output.
    verifyID = "aws ses verify-domain-identity --domain {0} --region {1} --profile {2}".format(str(DOMAIN), str(AWSregion), str(AWSprofile))
    #Run command and read back output to variable "txtOutput"
    txtOutput = os.popen(verifyID).read()
    #parse as JSON
    txt_dict = json.loads(txtOutput)

    #BUILD OUT output in desired format
    print(DOMAIN.upper())
    print("TXT Verification:")
    print("Txt Name: \n_amazonses." + DOMAIN)
    print("TXT Value:")
    print(txt_dict["VerificationToken"])
    print("\n")

    #Run get-identity-dkim-attributes by domain and produce copyable dkim key text output
    dkimVerify = "aws ses get-identity-dkim-attributes --identities {0} --region eu-west-1 --profile newcds".format(str(DOMAIN))
    #Run command and read back output to variable "dkimOutput"
    dkimOutput = os.popen(dkimVerify).read()
    #parse as JSON
    DKIM_dict = json.loads(dkimOutput)
    #Set each of the three resulting keys in the JSON list as variables DKIM1-3
    DKIM1 = (DKIM_dict["DkimAttributes"][DOMAIN]["DkimTokens"][0])
    DKIM2 = (DKIM_dict["DkimAttributes"][DOMAIN]["DkimTokens"][1])
    DKIM3 = (DKIM_dict["DkimAttributes"][DOMAIN]["DkimTokens"][2])

    #BUILD OUT output in desired format
    print("DKIM Verification:")
    print("Name: \n" + DKIM1 + "._domainkey." + DOMAIN)
    print("Type: CNAME")
    print("Value: \n" + DKIM1 + ".dkim.amazonses.com")
    print("\n")
    print("Name: \n" + DKIM2 + "._domainkey." + DOMAIN)
    print("Type: CNAME")
    print("Value: \n" + DKIM2 + ".dkim.amazonses.com")
    print("\n")
    print("Name: \n" + DKIM3 + "._domainkey." + DOMAIN)
    print("Type: CNAME")
    print("Value: \n" + DKIM3 + ".dkim.amazonses.com")
    print("\n")

# run with python [ScriptName].py > output.txt
