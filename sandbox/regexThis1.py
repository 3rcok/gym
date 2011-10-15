#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:      used to test if file names ended with 'bat or ext'
#
# Author:      wanglei2
#
# Created:     27/05/2011
# Copyright:   (c) wanglei2 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
# group () backreferences \2 \1
#


##s/([A-Z])([0-9]{2,4}) /\2:\1 /g
##
##< A37 B4 C107 D54112 E1103 XXX
##> 37:A B4 107:C D54112 1103:E XXX

#????
##>>> p = re.compile('x*')
##>>> p.sub('-', 'abxd')
##'-a-b-d-'
#????

#label
#if using?P no lablel, then there is no group number for that group

##import re
##txt = "A-xyz-37 # B:abcd:142 # C-wxy-66 # D-qrs-93"
##print re.sub("(?P<prefix>[A-Z])(-[a-z]{3}-)(?P<id>[0-9]*)",
##             "\g<prefix>\g<id>", txt)
##
##A37 # B:abcd:42 # C66 # D93

#replace ROAD with RD.

##>>> re.sub(r'\bROAD\b', 'RD.', s)  [4]
##'100 BROAD RD. APT 3'


#advance lookahead assertion
#?= or ?!

##A negative lookahead cuts through all this confusion:
##
##.*[.](?!bat$).*$ The negative lookahead means: if the expression bat doesnâ€™t match at this point, try the rest of the pattern; if bat$ does match, the whole pattern will fail. The trailing $ is required to ensure that something like sample.batch, where the extension only starts with bat, will be allowed.
##
##Excluding another filename extension is now easy; simply add it as an alternative inside the assertion. The following pattern excludes filenames that end in either bat or exe:
##
##.*[.](?!bat$|exe$).*$


import re
def main():
    txt = "A-xyz-37 # B:abcd:142 # C-wxy-66 # D-qrs-93"
    o = re.sub("(?P<prefix>[A-Z])(-[a-z]{3}-)(?P<id>[0-9]*)","\g<prefix>\g<id>", txt)
##    o = re.sub("(?P<prefix>[A-Z])(-[a-z]{3}-)(?P<id>[0-9]*)",r"(?P=prefix)(?P=id)", txt)
    if o:
        print(o)
    else :
        print('not match')

if __name__ == '__main__':
    main()