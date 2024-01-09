necessity_envelop = 0
freedom_envelop = 0
education_envelop = 0
long_term_envelop = 0
play_envelop = 0
give_envelop = 0

nec_rate = 0.55
ffa_rate = 0.1
edu_rate = 0.1
ltss_rate = 0.1
play_rate = 0.1
give_rate = 0.05

expected_income = 1000

print("""Hello.\n
    We gonna fill your envelops by the money you input here!\n
    Please input your amounts of money income and see the results.\n
    Press Ctrl+c to exit script.\n\n""")

sum = 0

while (sum < expected_income):
    print("\n Enter the amount please:")
    line = int(input())
    sum += line

    necessity_envelop += line * nec_rate
    freedom_envelop += line * ffa_rate
    education_envelop += line * edu_rate
    long_term_envelop += line * ltss_rate
    play_envelop += line * play_rate
    give_envelop += line * give_rate

else:
    massage = ("\nAt the end we we have:\n\n"
    f"Summary Income: {int(sum)}\n"           #show total sum of income we have
    f"Necessity Envelop has: {int(necessity_envelop)}\n"
    f"Financial Freedom Envelop has: {int(freedom_envelop)}\n"
    f"Education Envelop:{int(education_envelop)}\n"
    f"Long Term Saving for Spending Envelop has:{int(long_term_envelop)}\n" 
    f"Play Envelop has:{int(play_envelop)}\n"
    f"Give Envelop has:{int(give_envelop)}\n")
    
    print(massage)      #immediately shows the result if the entered amount is sufficient
