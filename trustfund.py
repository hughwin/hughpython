# Works out how much money is left in the trust fund... 
print """
                                                                                                                                                
 _________________      _____    ____   ____          ______   _________________             _____   ____   ____  _____   ______        _____   
/                 \ ___|\    \  |    | |    |     ___|\     \ /                 \       ____|\    \ |    | |    ||\    \ |\     \   ___|\    \  
\______     ______/|    |\    \ |    | |    |    |    |\     \\______     ______/      |    | \    \|    | |    | \\    \| \     \ |    |\    \ 
   \( /    /  )/   |    | |    ||    | |    |    |    |/____/|   \( /    /  )/         |    |______/|    | |    |  \|    \  \     ||    | |    |
    ' |   |   '    |    |/____/ |    | |    | ___|    \|   | |    ' |   |   '          |    |----'\ |    | |    |   |     \  |    ||    | |    |
      |   |        |    |\    \ |    | |    ||    \    \___|/       |   |              |    |_____/ |    | |    |   |      \ |    ||    | |    |
     /   //        |    | |    ||    | |    ||    |\     \         /   //              |    |       |    | |    |   |    |\ \|    ||    | |    |
    /___//         |____| |____||\___\_|____||\ ___\|_____|       /___//               |____|       |\___\_|____|   |____||\_____/||____|/____/|
   |`   |          |    | |    || |    |    || |    |     |      |`   |                |    |       | |    |    |   |    |/ \|   |||    /    | |
   |____|          |____| |____| \|____|____| \|____|_____|      |____|                |____|        \|____|____|   |____|   |___|/|____|____|/ 
     \(              \(     )/      \(   )/      \(    )/          \(                    )/             \(   )/       \(       )/    \(    )/   
      '               '     '        '   '        '    '            '                    '               '   '         '       '      '    '    
"""                                                                                                                                           
header = "\t\t\t Ensures your money doesn't run out!" 
print "\n" 

print header.title()
print "How much do you take home after tax?" 
pay = int(raw_input("Pay:"))
print "How much do you spend on bills per month?"
bills = int(raw_input("Bills:"))
print "How much do you spend on food?" 
food = int(raw_input("Food:"))
disinc = pay - (bills + food)
print "\n\n Your monthly disposable income is: %s" % disinc 
 

