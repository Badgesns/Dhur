#Script Write By Ghost King
#Github:https://github.com/minarulns
#Fb Group:Termux Free Command World 2024
#═══════════<( MODULE )>═══════════#
import os, random, time
#═══════════<( COLORS )>═══════════#
class Colors:
    RESET = "\033[0m"
class ExtendedColors:
    BRIGHT_PINK = "\033[38;5;200m"     # Bright pink
    CHARTREUSE = "\033[38;5;190m"      # Chartreuse
    SKY_BLUE = "\033[38;5;117m"        # Sky blue
    DARK_VIOLET = "\033[38;5;55m"      # Dark violet
    BRIGHT_YELLOW = "\033[38;5;226m"   # Bright yellow
    SLIME_GREEN = "\033[38;5;82m"      # Slime green
    NEON_PINK = "\033[38;5;201m"       # Neon pink
    FRESH_LIME = "\033[38;5;46m"       # Fresh lime
    MYSTIC_BLUE = "\033[38;5;39m"      # Mystic blue
    CRIMSON = "\033[38;5;9m"            # Crimson
    AMBER = "\033[38;5;214m"           # Amber
    ELECTRIC_BLUE = "\033[38;5;51m"    # Electric blue
    WISTERIA = "\033[38;5;183m"        # Wisteria
    BUBBLEGUM = "\033[38;5;13m"        # Bubblegum
    DEEP_PURPLE = "\033[38;5;55m"      # Deep purple
    LAVENDER = "\033[38;5;189m"        # Lavender
    PEACH = "\033[38;5;215m"            # Peach
    OLIVE_GREEN = "\033[38;5;100m"     # Olive green
color_choices = [
    ExtendedColors.BRIGHT_PINK,
    ExtendedColors.CHARTREUSE,
    ExtendedColors.SKY_BLUE,
    ExtendedColors.DARK_VIOLET,
    ExtendedColors.BRIGHT_YELLOW,
    ExtendedColors.SLIME_GREEN,
    ExtendedColors.NEON_PINK,
    ExtendedColors.FRESH_LIME,
    ExtendedColors.MYSTIC_BLUE,
    ExtendedColors.CRIMSON,
    ExtendedColors.AMBER,
    ExtendedColors.ELECTRIC_BLUE,
    ExtendedColors.WISTERIA,
    ExtendedColors.BUBBLEGUM,
    ExtendedColors.DEEP_PURPLE,
    ExtendedColors.LAVENDER,
    ExtendedColors.PEACH,
    ExtendedColors.OLIVE_GREEN,
]
random_color = random.choice(color_choices)
#═══════════<( COLOR )>═══════════#
WHITE='\x1b[1;97m';BLUE='\033[1;34m';GREEN='\033[1;32m';RED='\033[1;31m'
#═══════════<( CLEAR )>═══════════#
def clear():
    os.system('clear');print(logo)
#═══════════<( LINE )>═══════════#
def linex():
    print(f'\033[1;93m--------------------------------------------------\033[1;97m')
#═══════════<( BANNER  )>═══════════#
def banner():
    os.system('clear');print(logo);linex()
#═══════════<( USER AGENT )>═══════════#
model = random.choice(['SM-A205F','SM-A205FN','SM-A205GN','SM-A205YN','SM-A205G','SM-A205W','SM-A205U','SM-A205S','SM-S205DL','SM-A205U1'])
def ___uaa___():
    end = '[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.'+str(random.randint(11,99))+'.'+str(random.randint(111,999))+';FBBV/'+str(random.randint(111111111,999999999))+';'+'FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBCR/Tele2;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/'+str(model)+';FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]'
    ua = 'Davik/2.1.0 (Linux; U; Android '+str(random.randint(5,14))+'.0.1; '+str(model)+' Build/QP1A.190711.020; wv) '+end
    return ua
#═══════════<( LOGO BOX )>═══════════#
logo = '''\033[1;36m
           ▗▄▄▖▗▖ ▗▖ ▗▄▖  ▗▄▄▖▗▄▄▄▖
          ▐▌   ▐▌ ▐▌▐▌ ▐▌▐▌     █  
          ▐▌▝▜▌▐▛▀▜▌▐▌ ▐▌ ▝▀▚▖  █  
          ▝▚▄▞▘▐▌ ▐▌▝▚▄▞▘▗▄▄▞▘  █ 

\033[1;93m--------------------------------------------------
\033[1;31m[\033[1;37m=\033[1;31m] \033[1;32mAuthor    :  \033[1;32mMd. Minarul Islam
\033[1;31m[\033[1;37m+\033[1;31m] \033[1;32mFacebook  :  \033[1;32m MD.MINARULNS
\033[1;31m[\033[1;37m=\033[1;31m] \033[1;32mGithub    :  \033[1;32mminarulns
\033[1;93m--------------------------------------------------\033[1;97m
'''
#═══════════<( SECURITY )>═══════════#
def passwrd():
    try:
        time.sleep(1)
        os.system('xdg-open https://youtube.com/@minarulns')
        user = str(input(f'{WHITE}YouTube Channel Name : {BLUE}'))
        if user == 'minarulns':
            password = str(input(f'{WHITE}PASSWORD : {BLUE}'))
            if password == '123':
                time.sleep(1)
                print(f'{GREEN}[=] LOGIN SUCESSFULL ! ')
                linex()
                time.sleep(1)
            else:
                print(f'{RED}[×] PASSWORD INCORRECT!')
                linex()
                time.sleep(1)
                passwrd()
        else:
            print(f'{RED}[*] USERNAME INCORRECT!')
            linex()
            time.sleep(1)
            passwrd()
    except Exception as e:
        print(f'Error: {str(e)}')
#═══════════<( UA PRINTER )>═══════════#
def ___filef5___():
    time.sleep(1)
    clear()
    print(f'\033[1;31m[\033[1;37m=\033[1;31m] \033[1;32mPLEASE WAIT...')
    print(f'\033[1;31m[\033[1;37m=\033[1;31m] \033[1;32mSCRIPT GIFT BY GHOST...')
    time.sleep(1)
    print(f'\033[1;31m[\033[1;37m=\033[1;31m] \033[1;32mGETTING USER AGENT...')
    linex()
    count = 1
    while True:
        try:
            random_color = random.choice(color_choices)
            print(f"{count}. USER AGENT :{random_color} {___uaa___()}{Colors.RESET}")
            print(f'\033[1;97m----------------------------------------------\033[1;97m')
            open('/sdcard/GHOST-UA.txt', 'a').write(___uaa___()+'\n')
            count += 1
            time.sleep(2)
        except KeyboardInterrupt:
            break
#═══════════<( REMOVE COOKIE )>═══════════#
def remove_cookie():
    os.system('rm -rf .token .cookie .ua')
#═══════════<( UA CHECK )>═══════════#
def check_user_agent():
    try:
        print('1. Get User Agent')
        user_agent = open('.ua', 'r').read()
        print(f'{user_agent}')
    except FileNotFoundError:
        print(f' No User Agent Found!')
    except Exception as e:
        print(f'Error: {str(e)}')
#═══════════<( MENU SYSTEM )>═══════════#
if __name__ == '__main__':
    banner()
    passwrd()
    ___filef5___()
    check_user_agent()
    remove_cookie()
    print('All done!')
#═══════════<( SCRIPT CODE END HERE )>═══════════#
