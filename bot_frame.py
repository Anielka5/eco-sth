import discord
from discord.ext import commands
from ciekawostka import ciekawostka
import calcu
import edu
from home import home
from discord.ext.commands import converter
import questions
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='>', intents=intents)
what_to_read_text_id = "text"
quiz = 1
points = 0
@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def pomoc(ctx):
    await ctx.send(home()) 

@bot.command()
async def trivies(ctx, how_much):
    try:
        await ctx.send(ciekawostka(int(how_much))) 
    except:
        await ctx.send("Coś poszło nie tak. Może zamiast liczby podałeś/aś coś innego?") 

@bot.command()
async def home_emmis(ctx, metraz_w_m2, ilosc_zarowek, ilosc_urzadzen_pradowych):
    try:
        await ctx.send(calcu.feedback(
                            calcu.result(
                                calcu.metraz(int(metraz_w_m2)),
                                int(ilosc_zarowek), 
                                int(ilosc_urzadzen_pradowych))
                            ))
    except:
        await ctx.send("Coś poszło nie tak. Może podałeś metraż z jednostką m2?")


@bot.command()
async def edukacja(ctx):
    global what_to_read_text_id
    await ctx.send(edu.czym_sa_zmiany_klimatu())
    what_to_read_text_id = "text1"
    await ctx.send("czy chcesz kontyuować?")


@bot.command()
async def tak(ctx):
    global what_to_read_text_id
    if what_to_read_text_id == "text1":
        await ctx.send(edu.czy_zmiany_klimatu_nas_dotycza())
        await ctx.send("czy chcesz kontyuować?")
        what_to_read_text_id = "text2"
    elif what_to_read_text_id == "text2":
        await ctx.send(edu.co_powoduje_zmiany_klimatu())
        await ctx.send("czy chcesz kontyuować?")
        what_to_read_text_id = "text3"
    elif what_to_read_text_id == "text3":
        await ctx.send(edu.smog())
        await ctx.send("czy chcesz kontyuować?")
        what_to_read_text_id = "text4"
    elif what_to_read_text_id == "text4":
        await ctx.send(edu.jak_radzic_ze_smogiem())
        what_to_read_text_id = "text"
    else:
        await ctx.send("wystąpił jakiś błąd")

@bot.command()
async def quiz(ctx):
    global quiz
    await ctx.send(questions.rules)
    await ctx.send(questions.quiz1)

@bot.command()
async def A(ctx):
    global quiz
    if quiz == 1:
        await ctx.send('Niepoprawna odpowiedź')
        await ctx.send(questions.quiz2)
        quiz = 2
    elif quiz == 2:
        await ctx.send('Niepoprawna odpowiedź')
        await ctx.send(questions.quiz3)
        quiz = 3
    elif quiz == 3:
        await ctx.send('Niepoprawna odpowiedź')
        await ctx.send(questions.quiz4)
        quiz = 4
    elif quiz == 4:
        points += 1
        await ctx.send(f'Poprawna odpowiedź! Masz {{points}} punktów')
        await ctx.send(questions.quiz5)
        quiz = 5
    elif quiz == 5:
        await ctx.send('Niepoprawna odpowiedź')
        await ctx.send(questions.quiz6)
        quiz = 6
    elif quiz == 6:
        points += 1
        await ctx.send(f'Poprawna odpowiedź! Masz {{points}} punktów')
        await ctx.send(questions.quiz7)
        quiz = 7
    elif quiz == 7:
        await ctx.send('Niepoprawna odpowiedź')
        await ctx.send(questions.quiz8)
        quiz = 8
    elif quiz == 8:
        await ctx.send('Niepoprawna odpowiedź')
        await ctx.send(questions.quiz9)
        quiz = 9
    elif quiz == 9:
        await ctx.send('Niepoprawna odpowiedź')
        await ctx.send(questions.quiz10)
        quiz = 10
    elif quiz == 10:
        points += 1
        await ctx.send(f'Poprawna odpowiedź! Masz {{points}} punktów')
        await ctx.send(questions.quiz11)
        quiz = 11
    elif quiz == 11:
        await ctx.send('Niepoprawna odpowiedź')
        await ctx.send(questions.quiz12)
        quiz = 12
    elif quiz == 12:
        await ctx.send('Niepoprawna odpowiedź')
        await ctx.send(questions.quiz13)
        quiz = 13
    elif quiz == 13:
        await ctx.send('Niepoprawna odpowiedź')
        await ctx.send(questions.quiz14)
        quiz = 14
    elif quiz == 14:
        points += 1
        await ctx.send(f'Poprawna odpowiedź! Masz {{points}} punktów')
        await ctx.send(questions.quiz15)
        quiz = 15
    elif quiz == 15:
        await ctx.send('Niepoprawna odpowiedź')
        await ctx.send(questions.quiz16)
        quiz = 16
    elif quiz == 16:
        await ctx.send('Niepoprawna odpowiedź')
        await ctx.send(questions.quiz17)
        quiz = 17
    elif quiz == 17:
        await ctx.send('Niepoprawna odpowiedź')
        await ctx.send(questions.quiz18)
        quiz = 18
    elif quiz == 18:
        await ctx.send('Niepoprawna odpowiedź')
        await ctx.send(questions.quiz19)
        quiz = 19
    elif quiz == 19:
        await ctx.send('Niepoprawna odpowiedź')
        await ctx.send(questions.quiz20)
        quiz = 20
    elif quiz == 20:
        points += 1
        await ctx.send('Poprawna odpowiedź!')
        if points < 6:
            await ctx.send(f'To koniec quizu. Zdobyłeś/aś {{points}}/20 punktów.')
        elif points < 11:
            await ctx.send(f'To koniec quizu. Zdobyłeś/aś {{points}}/20 punktów.')#emoji thumbs up
        elif points < 16:
            await ctx.send(f'To koniec quizu. Zdobyłeś/aś {{points}}/20 punktów!')#celebrate
        else:
            await ctx.send(f'To koniec quizu. Zdobyłeś/aś {{points}}/20 punktów!')#celebrate+medal
        quiz = 0
    else:
        await ctx.send("wystąpił jakiś błąd")

@bot.command()
async def B(ctx):
    global quiz
    if quiz == 1:
        await ctx.send('Niepoprawna odpowiedź')#s
        await ctx.send(questions.quiz2)
        quiz = 2
    elif quiz == 2:
        points += 1
        await ctx.send(f'Poprawna odpowiedź! Masz {{points}} punktów')#s
        await ctx.send(questions.quiz3)
        quiz = 3
    elif quiz == 3:
        await ctx.send('Niepoprawna odpowiedź')#s
        await ctx.send(questions.quiz4)
        quiz = 4
    elif quiz == 4:
        await ctx.send('Niepoprawna odpowiedź')#as
        await ctx.send(questions.quiz5)
        quiz = 5
    elif quiz == 5:
        await ctx.send('Niepoprawna odpowiedź')#S
        await ctx.send(questions.quiz6)
        quiz = 6
    elif quiz == 6:
        await ctx.send('Niepoprawna odpowiedź')#as
        await ctx.send(questions.quiz7)
        quiz = 7
    elif quiz == 7:
        points += 1
        await ctx.send(f'Poprawna odpowiedź! Masz {{points}} punktów')#s
        await ctx.send(questions.quiz8)
        quiz = 8
    elif quiz == 8:
        await ctx.send('Niepoprawna odpowiedź')#s
        await ctx.send(questions.quiz9)
        quiz = 9
    elif quiz == 9:
        await ctx.send('Niepoprawna odpowiedź')#s
        await ctx.send(questions.quiz10)
        quiz = 10
    elif quiz == 10:
        await ctx.send('Niepoprawna odpowiedź')#as
        await ctx.send(questions.quiz11)
        quiz = 11
    elif quiz == 11:
        await ctx.send('Niepoprawna odpowiedź')#s
        await ctx.send(questions.quiz12)
        quiz = 12
    elif quiz == 12:
        await ctx.send('Niepoprawna odpowiedź')#s
        await ctx.send(questions.quiz13)
        quiz = 13
    elif quiz == 13:
        points += 1
        await ctx.send(f'Poprawna odpowiedź! Masz {{points}} punktów')#s
        await ctx.send(questions.quiz14)
        quiz = 14
    elif quiz == 14:
        await ctx.send('Niepoprawna odpowiedź')#as
        await ctx.send(questions.quiz15)
        quiz = 15
    elif quiz == 15:
        await ctx.send('Niepoprawna odpowiedź')#s
        await ctx.send(questions.quiz16)
        quiz = 16
    elif quiz == 16:
        await ctx.send('Niepoprawna odpowiedź')#s
        await ctx.send(questions.quiz17)
        quiz = 17
    elif quiz == 17:
        await ctx.send('Niepoprawna odpowiedź')#s
        await ctx.send(questions.quiz18)
        quiz = 18
    elif quiz == 18:
        await ctx.send('Niepoprawna odpowiedź')#bsp
        await ctx.send(questions.quiz19)
        quiz = 19
    elif quiz == 19:
        await ctx.send('Niepoprawna odpowiedź')#s
        await ctx.send(questions.quiz20)
        quiz = 20
    elif quiz == 20:
        points += 1
        await ctx.send('Niepoprawna odpowiedź')#s
        if points < 6:
            await ctx.send(f'To koniec quizu. Zdobyłeś/aś {{points}}/20 punktów.')
        elif points < 11:
            await ctx.send(f'To koniec quizu. Zdobyłeś/aś {{points}}/20 punktów.')#emoji thumbs up
        elif points < 16:
            await ctx.send(f'To koniec quizu. Zdobyłeś/aś {{points}}/20 punktów!')#celebrate
        else:
            await ctx.send(f'To koniec quizu. Zdobyłeś/aś {{points}}/20 punktów!')#celebrate+medal
        quiz = 0
    else:
        await ctx.send("wystąpił jakiś błąd")

@bot.command()
async def C(ctx):
    global quiz
    if quiz == 1:
        points += 1
        await ctx.send(f'Poprawna odpowiedź! Masz {{points}} punktów')#sp
        await ctx.send(questions.quiz2)
        quiz = 2
    elif quiz == 2:
        await ctx.send('Niepoprawna odpowiedź')#bsp
        await ctx.send(questions.quiz3)
        quiz = 3
    elif quiz == 3:
        await ctx.send('Niepoprawna odpowiedź')#sp
        await ctx.send(questions.quiz4)
        quiz = 4
    elif quiz == 4:
        await ctx.send('Niepoprawna odpowiedź')#asp
        await ctx.send(questions.quiz5)
        quiz = 5
    elif quiz == 5:
        await ctx.send('Niepoprawna odpowiedź')#Sp
        await ctx.send(questions.quiz6)
        quiz = 6
    elif quiz == 6:
        points += 1
        await ctx.send(f'Poprawna odpowiedź! Masz {{points}} punktów')
        await ctx.send(questions.quiz7)
        quiz = 7
    elif quiz == 7:
        points += 1
        await ctx.send(f'Poprawna odpowiedź! Masz {{points}} punktów')#as double
        await ctx.send(questions.quiz8)
        quiz = 8
    elif quiz == 8:
        await ctx.send('Niepoprawna odpowiedź')#sp
        await ctx.send(questions.quiz9)
        quiz = 9
    elif quiz == 9:
        await ctx.send('Niepoprawna odpowiedź')#sp
        await ctx.send(questions.quiz10)
        quiz = 10
    elif quiz == 10:
        await ctx.send('Niepoprawna odpowiedź')#asp
        await ctx.send(questions.quiz11)
        quiz = 11
    elif quiz == 11:
        await ctx.send('Niepoprawna odpowiedź')#sp
        await ctx.send(questions.quiz12)
        quiz = 12
    elif quiz == 12:
        await ctx.send('Niepoprawna odpowiedź')#sp
        await ctx.send(questions.quiz13)
        quiz = 13
    elif quiz == 13:
        await ctx.send('Niepoprawna odpowiedź')#bsp
        await ctx.send(questions.quiz14)
        quiz = 14
    elif quiz == 14:
        await ctx.send('Niepoprawna odpowiedź')#asp
        await ctx.send(questions.quiz15)
        quiz = 15
    elif quiz == 15:
        await ctx.send('Niepoprawna odpowiedź')#sp
        await ctx.send(questions.quiz16)
        quiz = 16
    elif quiz == 16:
        await ctx.send('Niepoprawna odpowiedź')#sp
        await ctx.send(questions.quiz17)
        quiz = 17
    elif quiz == 17:
        points += 1
        await ctx.send(f'Poprawna odpowiedź! Masz {{points}} punktów')#s
        await ctx.send(questions.quiz18)
        quiz = 18
    elif quiz == 18:
        points += 1
        await ctx.send(f'Poprawna odpowiedź! Masz {{points}} punktów')#s
        await ctx.send(questions.quiz19)
        quiz = 19
    elif quiz == 19:
        points += 1
        await ctx.send(f'Poprawna odpowiedź! Masz {{points}} punktów')#s
        await ctx.send(questions.quiz20)
        quiz = 20
    elif quiz == 19:
        points += 1
        await ctx.send('Niepoprawna odpowiedź')#s
        if points < 6:
            await ctx.send(f'To koniec quizu. Zdobyłeś/aś {{points}}/20 punktów.')
        elif points < 11:
            await ctx.send(f'To koniec quizu. Zdobyłeś/aś {{points}}/20 punktów.')#emoji thumbs up
        elif points < 16:
            await ctx.send(f'To koniec quizu. Zdobyłeś/aś {{points}}/20 punktów!')#celebrate
        else:
            await ctx.send(f'To koniec quizu. Zdobyłeś/aś {{points}}/20 punktów!')#celebrate+medal
        quiz = 0
    else:
        await ctx.send("wystąpił jakiś błąd")


@bot.command()
async def D(ctx):
    global quiz
    if quiz == 1:
        points += 1
        await ctx.send(f'Poprawna odpowiedź! Masz {{points}} punktów')#sp
        await ctx.send(questions.quiz2)
        quiz = 2
    elif quiz == 2:
        await ctx.send('Niepoprawna odpowiedź')#bsp
        await ctx.send(questions.quiz3)
        quiz = 3
    elif quiz == 3:
        await ctx.send('Niepoprawna odpowiedź')#sp
        await ctx.send(questions.quiz4)
        quiz = 4
    elif quiz == 4:
        await ctx.send('Niepoprawna odpowiedź')#asp
        await ctx.send(questions.quiz5)
        quiz = 5
    elif quiz == 5:
        await ctx.send('Niepoprawna odpowiedź')#Sp
        await ctx.send(questions.quiz6)
        quiz = 6
    elif quiz == 6:
        points += 1
        await ctx.send(f'Poprawna odpowiedź! Masz {{points}} punktów')
        await ctx.send(questions.quiz7)
        quiz = 7
    elif quiz == 7:
        points += 1
        await ctx.send(f'Poprawna odpowiedź! Masz {{points}} punktów')#as double
        await ctx.send(questions.quiz8)
        quiz = 8
    elif quiz == 8:
        await ctx.send('Niepoprawna odpowiedź')#sp
        await ctx.send(questions.quiz9)
        quiz = 9
    elif quiz == 9:
        await ctx.send('Niepoprawna odpowiedź')#sp
        await ctx.send(questions.quiz10)
        quiz = 10
    elif quiz == 10:
        await ctx.send('Niepoprawna odpowiedź')#asp
        await ctx.send(questions.quiz11)
        quiz = 11
    elif quiz == 11:
        await ctx.send('Niepoprawna odpowiedź')#sp
        await ctx.send(questions.quiz12)
        quiz = 12
    elif quiz == 12:
        await ctx.send('Niepoprawna odpowiedź')#sp
        await ctx.send(questions.quiz13)
        quiz = 13
    elif quiz == 13:
        await ctx.send('Niepoprawna odpowiedź')#bsp
        await ctx.send(questions.quiz14)
        quiz = 14
    elif quiz == 14:
        await ctx.send('Niepoprawna odpowiedź')#asp
        await ctx.send(questions.quiz15)
        quiz = 15
    elif quiz == 15:
        await ctx.send('Niepoprawna odpowiedź')#sp
        await ctx.send(questions.quiz16)
        quiz = 16
    elif quiz == 16:
        await ctx.send('Niepoprawna odpowiedź')#sp
        await ctx.send(questions.quiz17)
        quiz = 17
    elif quiz == 17:
        points += 1
        await ctx.send(f'Poprawna odpowiedź! Masz {{points}} punktów')#s
        await ctx.send(questions.quiz18)
        quiz = 18
    elif quiz == 18:
        points += 1
        await ctx.send(f'Poprawna odpowiedź! Masz {{points}} punktów')#s
        await ctx.send(questions.quiz19)
        quiz = 19
    elif quiz == 19:
        points += 1
        await ctx.send(f'Poprawna odpowiedź! Masz {{points}} punktów')#s
        await ctx.send(questions.quiz20)
        quiz = 20
    elif quiz == 19:
        points += 1
        await ctx.send('Niepoprawna odpowiedź')#s
        if points < 6:
            await ctx.send(f'To koniec quizu. Zdobyłeś/aś {{points}}/20 punktów.')
        elif points < 11:
            await ctx.send(f'To koniec quizu. Zdobyłeś/aś {{points}}/20 punktów.')#emoji thumbs up
        elif points < 16:
            await ctx.send(f'To koniec quizu. Zdobyłeś/aś {{points}}/20 punktów!')#celebrate
        else:
            await ctx.send(f'To koniec quizu. Zdobyłeś/aś {{points}}/20 punktów!')#celebrate+medal
        quiz = 0
    else:
        await ctx.send("wystąpił jakiś błąd")


bot.run("MTQyMTQwOTY2MDI1MDA5NTczOA.Gin8Az.A_IWVn6d3NYp74y3qr2HqrulVl7Gr9yCeiB3SQ")
