# SES_txt_and_DKIM_listing_by_domain
Python scripts for working with AWS SES
These assume aws cli has been intalled on your machine and that aws configure has been run on them.

If no custom profiles have been created, use: default for the profile variable.
========
Use case: List all SES domains with their txt verification and their dkim records

Create all DKIM IDs
aws ses verify-domain-dkim --domain --eu-west-1 --profile newcds

==========

Input domain list as csv:
For each domain $DOMAIN 
aws ses get-identity-verification-attributes --identities "domain1"
>$verification (strip out and append this)
“Verification Token”: “____”

Txt Name: _amazonses.$DOMAIN
TXT Value: $VERIFICATION
aws ses get-identity-dkim-attributes --identities $DOMAIN --profile newcds --region eu-west-1
 

Grab , separated JSON DKIM tokens:
$DKIM1
$DKIM2
$DKIM3
Name: $DKIM1._domainkey.$DOMAIN
Type: CNAME
Value: $DKIM1.dkim.amazonses.com

Name: $DKIM2._domainkey.$DOMAIN
Type: CNAME
Value: $DKIM2.dkim.amazonses.com

Name: $DKIM3._domainkey.$DOMAIN
Type: CNAME
Value: $DKIM3.dkim.amazonses.com


