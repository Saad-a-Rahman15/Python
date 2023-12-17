print("Hi welcome to this quiz that asks you your opinions about some things in football!")
name = input("What's your name? \n")
print("Hi, are you ready for this football game " + name)

print("Man City Arsenal Man Utd Liverpool Chelsea Fulham Nott'm Forest Brighton Aston Villa West Ham Tottenham Newcastle Brentford Crystal Palace Wolves Everton Luton Burnley Sheffield Utd Bournemouth")
pl_team = input("Choose a Premier League football club that you like from above:  \n")
print("Hi " + name)
print("You like the football club, " + pl_team)

print("Man City  Bayern Munich  Real Madrid  Barcelona  Juventus  Dortmund  Sporting CP  AC Milan  Man Utd  Napoli  PSG")
cp_teams = input("Now, choose a Champions League club from above to show who you will win the Champions League this year:  \n")
print(name + ", you think that " + cp_teams + " will win the Champions League.\n")

print("Do you want to to a country-football opinion game?")
print("If yes, type down 'yes.'")
print("If no, type down 'no.'")
print("WARNING. Please write your answer as shown")
question1 = input("Type your answer down here.\n")

reply1 = "yes"
reply2 = "no"

if question1 == reply1:
    print("England  Germany  France  Italy\n")
    print("WARNING. Please write your answer as shown")
    command1 = input("Choose a country from above.\n")

    country1 = "England"
    country2 = "Germany"
    country3 = "France"
    country4 = "Italy"

    if command1 == country1:
        print("Man City  Liverpool  Man Utd  Newcastle Utd  Arsenal  Chelsea  Spurs.\n")
        england1 = input("Choose a football club.\n")
        print(name + " you like " + england1)
        print("This is the end of the quiz. Thank you :)")

    if command1 == country2:
        print("Bayern Munich  Borussia Dortmunt  Bayer Leverkusen  Union Berlin  RB Leipzing")
        germany1 = input("Choose a foot    if :ball club.\n")
        print(name + " you like " + germany1)
        print("This is the end of the quiz. Thank you :)")

    if command1 == country3:
        print("PSG  Lyon  Monaco  Nice  Marsielle  LOSC_Lille")
        france1 = input("Choose a football club.\n")
        print(name + " you like " + france1)
        print("This is the end of the quiz. Thank you :)")

    if command1 == country4:
        print("Napoli  AC Milan  Inter  Juventus  Roma")
        italy1 = input("Choose a football club.\n")
        print(name + " you like " + italy1)
        print("This is the end of the quiz. Thank you :)")

elif question1 == reply2:
    print("OK, this is the end of the quiz. Thank you :)")

else:
    print("That is not the reply 'yes' or 'no.' :(")