import random
versia = "1.2.21"
text = " © BoburBro <tool> "



a = """
  ____        _                _      
 |  _ \      | |              | |    
 | |_) | ___ | |__  _   _ _ __| |__  _ __ ___    
 |  _ < / _ \| '_ \| | | | '__| '_ \| '__/ _ \    
 | |_) | (_) | |_) | |_| | |  | |_) | | | (_) |    
 |____/ \___/|_.__/ \__,_|_|  |_.__/|_|  \___/
"""

b = """
██████╗  ██████╗ ██████╗ ██╗   ██╗██████╗ ██████╗ ██████╗  ██████╗ 
██╔══██╗██╔═══██╗██╔══██╗██║   ██║██╔══██╗██╔══██╗██╔══██╗██╔═══██╗
██████╔╝██║   ██║██████╔╝██║   ██║██████╔╝██████╔╝██████╔╝██║   ██║
██╔══██╗██║   ██║██╔══██╗██║   ██║██╔══██╗██╔══██╗██╔══██╗██║   ██║
██████╔╝╚██████╔╝██████╔╝╚██████╔╝██║  ██║██████╔╝██║  ██║╚██████╔╝
╚═════╝  ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ 
                                                                   
"""

ab = """
 ######                              ######                
 #     #  ####  #####  #    # #####  #     # #####   ####  
 #     # #    # #    # #    # #    # #     # #    # #    # 
 ######  #    # #####  #    # #    # ######  #    # #    # 
 #     # #    # #    # #    # #####  #     # #####  #    # 
 #     # #    # #    # #    # #   #  #     # #   #  #    # 
 ######   ####  #####   ####  #    # ######  #    #  ####  
                                                           """
aa = """
╔╗ ┌─┐┌┐ ┬ ┬┬─┐╔╗ ┬─┐┌─┐
╠╩╗│ │├┴┐│ │├┬┘╠╩╗├┬┘│ │
╚═╝└─┘└─┘└─┘┴└─╚═╝┴└─└─┘
"""
aaa = """
 ███████████           █████                          ███████████                    
░░███░░░░░███         ░░███                          ░░███░░░░░███                   
 ░███    ░███  ██████  ░███████  █████ ████ ████████  ░███    ░███ ████████   ██████ 
 ░██████████  ███░░███ ░███░░███░░███ ░███ ░░███░░███ ░██████████ ░░███░░███ ███░░███
 ░███░░░░░███░███ ░███ ░███ ░███ ░███ ░███  ░███ ░░░  ░███░░░░░███ ░███ ░░░ ░███ ░███
 ░███    ░███░███ ░███ ░███ ░███ ░███ ░███  ░███      ░███    ░███ ░███     ░███ ░███
 ███████████ ░░██████  ████████  ░░████████ █████     ███████████  █████    ░░██████ 
░░░░░░░░░░░   ░░░░░░  ░░░░░░░░    ░░░░░░░░ ░░░░░     ░░░░░░░░░░░  ░░░░░      ░░░░░░  
                                                                                     
                                                                                     
                                                                                     """

a1 = """
 ▄▀▀█▄▄   ▄▀▀▀▀▄   ▄▀▀█▄▄   ▄▀▀▄ ▄▀▀▄  ▄▀▀▄▀▀▀▄  ▄▀▀█▄▄   ▄▀▀▄▀▀▀▄  ▄▀▀▀▀▄  
▐ ▄▀   █ █      █ ▐ ▄▀   █ █   █    █ █   █   █ ▐ ▄▀   █ █   █   █ █      █ 
  █▄▄▄▀  █      █   █▄▄▄▀  ▐  █    █  ▐  █▀▀█▀    █▄▄▄▀  ▐  █▀▀█▀  █      █ 
  █   █  ▀▄    ▄▀   █   █    █    █    ▄▀    █    █   █   ▄▀    █  ▀▄    ▄▀ 
 ▄▀▄▄▄▀    ▀▀▀▀    ▄▀▄▄▄▀     ▀▄▄▄▄▀  █     █    ▄▀▄▄▄▀  █     █     ▀▀▀▀   
█    ▐            █    ▐              ▐     ▐   █    ▐   ▐     ▐            
▐                 ▐                             ▐                           
"""

a2 = '''
 ,ggggggggggg,                                             ,ggggggggggg,                          
dP"""88""""""Y8,             ,dPYb,                       dP"""88""""""Y8,                        
Yb,  88      `8b             IP'`Yb                       Yb,  88      `8b                        
 `"  88      ,8P             I8  8I                        `"  88      ,8P                        
     88aaaad8P"              I8  8'                            88aaaad8P"                         
     88""""Y8ba    ,ggggg,   I8 dP      gg      gg   ,gggggg,  88""""Y8ba   ,gggggg,    ,ggggg,   
     88      `8b  dP"  "Y8gggI8dP   88ggI8      8I   dP""""8I  88      `8b  dP""""8I   dP"  "Y8ggg
     88      ,8P i8'    ,8I  I8P    8I  I8,    ,8I  ,8'    8I  88      ,8P ,8'    8I  i8'    ,8I  
     88_____,d8',d8,   ,d8' ,d8b,  ,8I ,d8b,  ,d8b,,dP     Y8, 88_____,d8',dP     Y8,,d8,   ,d8'  
    88888888P"  P"Y8888P"   8P'"Y88P"' 8P'"Y88P"`Y88P      `Y888888888P"  8P      `Y8P"Y8888P"    
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  '''



a3 = """
 ******            **                     ******                  
/*////**          /**                    /*////**                 
/*   /**   ****** /**      **   ** ******/*   /**  ******  ****** 
/******   **////**/****** /**  /**//**//*/******  //**//* **////**
/*//// **/**   /**/**///**/**  /** /** / /*//// ** /** / /**   /**
/*    /**/**   /**/**  /**/**  /** /**   /*    /** /**   /**   /**
/******* //****** /****** //******/***   /******* /***   //****** 
///////   //////  /////    ////// ///    ///////  ///     //////  """

a4="""
 ________  ________  ________  ___  ___  ________  ________  ________  ________     
|\   __  \|\   __  \|\   __  \|\  \|\  \|\   __  \|\   __  \|\   __  \|\   __  \    
\ \  \|\ /\ \  \|\  \ \  \|\ /\ \  \\\  \ \  \|\  \ \  \|\ /\ \  \|\  \ \  \|\  \   
 \ \   __  \ \  \\\  \ \   __  \ \  \\\  \ \   _  _\ \   __  \ \   _  _\ \  \\\  \  
  \ \  \|\  \ \  \\\  \ \  \|\  \ \  \\\  \ \  \\  \\ \  \|\  \ \  \\  \\ \  \\\  \ 
   \ \_______\ \_______\ \_______\ \_______\ \__\\ _\\ \_______\ \__\\ _\\ \_______\
    \|_______|\|_______|\|_______|\|_______|\|__|\|__|\|_______|\|__|\|__|\|_______|
                                                                                    
                                                                                    
                                                                                    
"""
a5= """
 .S_SSSs      sSSs_sSSs     .S_SSSs     .S       S.    .S_sSSs     .S_SSSs     .S_sSSs      sSSs_sSSs    
.SS~SSSSS    d%%SP~YS%%b   .SS~SSSSS   .SS       SS.  .SS~YS%%b   .SS~SSSSS   .SS~YS%%b    d%%SP~YS%%b   
S%S   SSSS  d%S'     `S%b  S%S   SSSS  S%S       S%S  S%S   `S%b  S%S   SSSS  S%S   `S%b  d%S'     `S%b  
S%S    S%S  S%S       S%S  S%S    S%S  S%S       S%S  S%S    S%S  S%S    S%S  S%S    S%S  S%S       S%S  
S%S SSSS%P  S&S       S&S  S%S SSSS%P  S&S       S&S  S%S    d*S  S%S SSSS%P  S%S    d*S  S&S       S&S  
S&S  SSSY   S&S       S&S  S&S  SSSY   S&S       S&S  S&S   .S*S  S&S  SSSY   S&S   .S*S  S&S       S&S  
S&S    S&S  S&S       S&S  S&S    S&S  S&S       S&S  S&S_sdSSS   S&S    S&S  S&S_sdSSS   S&S       S&S  
S&S    S&S  S&S       S&S  S&S    S&S  S&S       S&S  S&S~YSY%b   S&S    S&S  S&S~YSY%b   S&S       S&S  
S*S    S&S  S*b       d*S  S*S    S&S  S*b       d*S  S*S   `S%b  S*S    S&S  S*S   `S%b  S*b       d*S  
S*S    S*S  S*S.     .S*S  S*S    S*S  S*S.     .S*S  S*S    S%S  S*S    S*S  S*S    S%S  S*S.     .S*S  
S*S SSSSP    SSSbs_sdSSS   S*S SSSSP    SSSbs_sdSSS   S*S    S&S  S*S SSSSP   S*S    S&S   SSSbs_sdSSS   
S*S  SSY      YSSP~YSSY    S*S  SSY      YSSP~YSSY    S*S    SSS  S*S  SSY    S*S    SSS    YSSP~YSSY    
SP                         SP                         SP          SP          SP                         
Y                          Y                          Y           Y           Y                          
                                                                                                         
"""

a6 = """
.sSSSSs.                                                    .sSSSSs.                            
SSSSSSSSSs. .sSSSSs.    .sSSSSs.    .sSSS s.    .sSSSSSSSs. SSSSSSSSSs. .sSSSSSSSs. .sSSSSs.    
S SSS SSSSS S SSSSSSSs. S SSSSSSSs. S SSS SSSs. S SSS SSSSS S SSS SSSSS S SSS SSSSS S SSSSSSSs. 
S  SS SSSS' S  SS SSSSS S  SS SSSS' S  SS SSSSS S  SS SSSS' S  SS SSSS' S  SS SSSS' S  SS SSSSS 
S..SSsSSSa. S..SS SSSSS S..SSsSSSa. S..SS SSSSS S..SSsSSSa. S..SSsSSSa. S..SSsSSSa. S..SS SSSSS 
S:::S SSSSS S:::S SSSSS S:::S SSSSS S:::S SSSSS S:::S SSSSS S:::S SSSSS S:::S SSSSS S:::S SSSSS 
S;;;S SSSSS S;;;S SSSSS S;;;S SSSSS S;;;S SSSSS S;;;S SSSSS S;;;S SSSSS S;;;S SSSSS S;;;S SSSSS 
S%%%S SSSSS S%%%S SSSSS S%%%S SSSSS S%%%S SSSSS S%%%S SSSSS S%%%S SSSSS S%%%S SSSSS S%%%S SSSSS 
SSSSSsSSSS' SSSSSsSSSSS SSSSSsSSSS' SSSSSsSSSSS SSSSS SSSSS SSSSSsSSSS' SSSSS SSSSS SSSSSsSSSSS 
                                                                                                
"""

a7="""
:::::::::   ::::::::  :::::::::  :::    ::: :::::::::  :::::::::  :::::::::   ::::::::  
:+:    :+: :+:    :+: :+:    :+: :+:    :+: :+:    :+: :+:    :+: :+:    :+: :+:    :+: 
+:+    +:+ +:+    +:+ +:+    +:+ +:+    +:+ +:+    +:+ +:+    +:+ +:+    +:+ +:+    +:+ 
+#++:++#+  +#+    +:+ +#++:++#+  +#+    +:+ +#++:++#:  +#++:++#+  +#++:++#:  +#+    +:+ 
+#+    +#+ +#+    +#+ +#+    +#+ +#+    +#+ +#+    +#+ +#+    +#+ +#+    +#+ +#+    +#+ 
#+#    #+# #+#    #+# #+#    #+# #+#    #+# #+#    #+# #+#    #+# #+#    #+# #+#    #+# 
#########   ########  #########   ########  ###    ### #########  ###    ###  ########  
"""
a8= """
'########:::'#######::'########::'##::::'##:'########::'########::'########:::'#######::
 ##.... ##:'##.... ##: ##.... ##: ##:::: ##: ##.... ##: ##.... ##: ##.... ##:'##.... ##:
 ##:::: ##: ##:::: ##: ##:::: ##: ##:::: ##: ##:::: ##: ##:::: ##: ##:::: ##: ##:::: ##:
 ########:: ##:::: ##: ########:: ##:::: ##: ########:: ########:: ########:: ##:::: ##:
 ##.... ##: ##:::: ##: ##.... ##: ##:::: ##: ##.. ##::: ##.... ##: ##.. ##::: ##:::: ##:
 ##:::: ##: ##:::: ##: ##:::: ##: ##:::: ##: ##::. ##:: ##:::: ##: ##::. ##:: ##:::: ##:
 ########::. #######:: ########::. #######:: ##:::. ##: ########:: ##:::. ##:. #######::
........::::.......:::........::::.......:::..:::::..::........:::..:::::..:::.......:::"""


a9 = """
                                                                                                                                 
8 888888888o       ,o888888o.     8 888888888o   8 8888      88 8 888888888o.   8 888888888o   8 888888888o.      ,o888888o.     
8 8888    `88.  . 8888     `88.   8 8888    `88. 8 8888      88 8 8888    `88.  8 8888    `88. 8 8888    `88.  . 8888     `88.   
8 8888     `88 ,8 8888       `8b  8 8888     `88 8 8888      88 8 8888     `88  8 8888     `88 8 8888     `88 ,8 8888       `8b  
8 8888     ,88 88 8888        `8b 8 8888     ,88 8 8888      88 8 8888     ,88  8 8888     ,88 8 8888     ,88 88 8888        `8b 
8 8888.   ,88' 88 8888         88 8 8888.   ,88' 8 8888      88 8 8888.   ,88'  8 8888.   ,88' 8 8888.   ,88' 88 8888         88 
8 8888888888   88 8888         88 8 8888888888   8 8888      88 8 888888888P'   8 8888888888   8 888888888P'  88 8888         88 
8 8888    `88. 88 8888        ,8P 8 8888    `88. 8 8888      88 8 8888`8b       8 8888    `88. 8 8888`8b      88 8888        ,8P 
8 8888      88 `8 8888       ,8P  8 8888      88 ` 8888     ,8P 8 8888 `8b.     8 8888      88 8 8888 `8b.    `8 8888       ,8P  
8 8888    ,88'  ` 8888     ,88'   8 8888    ,88'   8888   ,d8P  8 8888   `8b.   8 8888    ,88' 8 8888   `8b.   ` 8888     ,88'   
8 888888888P       `8888888P'     8 888888888P      `Y88888P'   8 8888     `88. 8 888888888P   8 8888     `88.    `8888888P'     
"""

a10="""
888888b.            888                       888888b.                   
888  "88b           888                       888  "88b                  
888  .88P           888                       888  .88P                  
8888888K.   .d88b.  88888b.  888  888 888d888 8888888K.  888d888 .d88b.  
888  "Y88b d88""88b 888 "88b 888  888 888P"   888  "Y88b 888P"  d88""88b 
888    888 888  888 888  888 888  888 888     888    888 888    888  888 
888   d88P Y88..88P 888 d88P Y88b 888 888     888   d88P 888    Y88..88P 
8888888P"   "Y88P"  88888P"   "Y88888 888     8888888P"  888     "Y88P"  
                                                                         
                                                                         
                                                                         
"""

a11="""
                                                                                                                                                    
                                    bbbbbbbb                                                                                                        
BBBBBBBBBBBBBBBBB                   b::::::b                                               BBBBBBBBBBBBBBBBB                                        
B::::::::::::::::B                  b::::::b                                               B::::::::::::::::B                                       
B::::::BBBBBB:::::B                 b::::::b                                               B::::::BBBBBB:::::B                                      
BB:::::B     B:::::B                 b:::::b                                               BB:::::B     B:::::B                                     
  B::::B     B:::::B   ooooooooooo   b:::::bbbbbbbbb    uuuuuu    uuuuuu rrrrr   rrrrrrrrr   B::::B     B:::::Brrrrr   rrrrrrrrr      ooooooooooo   
  B::::B     B:::::B oo:::::::::::oo b::::::::::::::bb  u::::u    u::::u r::::rrr:::::::::r  B::::B     B:::::Br::::rrr:::::::::r   oo:::::::::::oo 
  B::::BBBBBB:::::B o:::::::::::::::ob::::::::::::::::b u::::u    u::::u r:::::::::::::::::r B::::BBBBBB:::::B r:::::::::::::::::r o:::::::::::::::o
  B:::::::::::::BB  o:::::ooooo:::::ob:::::bbbbb:::::::bu::::u    u::::u rr::::::rrrrr::::::rB:::::::::::::BB  rr::::::rrrrr::::::ro:::::ooooo:::::o
  B::::BBBBBB:::::B o::::o     o::::ob:::::b    b::::::bu::::u    u::::u  r:::::r     r:::::rB::::BBBBBB:::::B  r:::::r     r:::::ro::::o     o::::o
  B::::B     B:::::Bo::::o     o::::ob:::::b     b:::::bu::::u    u::::u  r:::::r     rrrrrrrB::::B     B:::::B r:::::r     rrrrrrro::::o     o::::o
  B::::B     B:::::Bo::::o     o::::ob:::::b     b:::::bu::::u    u::::u  r:::::r            B::::B     B:::::B r:::::r            o::::o     o::::o
  B::::B     B:::::Bo::::o     o::::ob:::::b     b:::::bu:::::uuuu:::::u  r:::::r            B::::B     B:::::B r:::::r            o::::o     o::::o
BB:::::BBBBBB::::::Bo:::::ooooo:::::ob:::::bbbbbb::::::bu:::::::::::::::uur:::::r          BB:::::BBBBBB::::::B r:::::r            o:::::ooooo:::::o
B:::::::::::::::::B o:::::::::::::::ob::::::::::::::::b  u:::::::::::::::ur:::::r          B:::::::::::::::::B  r:::::r            o:::::::::::::::o
B::::::::::::::::B   oo:::::::::::oo b:::::::::::::::b    uu::::::::uu:::ur:::::r          B::::::::::::::::B   r:::::r             oo:::::::::::oo 
BBBBBBBBBBBBBBBBB      ooooooooooo   bbbbbbbbbbbbbbbb       uuuuuuuu  uuuurrrrrrr          BBBBBBBBBBBBBBBBB    rrrrrrr               ooooooooooo   
                                                                                                                                                    
                                                                                                                                                    
                                                                                                                                                    
                                                                                                                                                    
                                                                                                                                                    
                                                                                                                                                    
                                                                                                                                                    """

a12="""
 __   __   __        __   __   __   __  
|__) /  \ |__) |  | |__) |__) |__) /  \ 
|__) \__/ |__) \__/ |  \ |__) |  \ \__/ 
                                        
"""

a13="""
 _______     ______    _______   ____  ____   _______   _______    _______     ______    
|   _  "\   /    " \  |   _  "\ ("  _||_ " | /"      \ |   _  "\  /"      \   /    " \   
(. |_)  :) // ____  \ (. |_)  :)|   (  ) : ||:        |(. |_)  :)|:        | // ____  \  
|:     \/ /  /    ) :)|:     \/ (:  |  | . )|_____/   )|:     \/ |_____/   )/  /    ) :) 
(|  _  \\(: (____/ // (|  _  \\  \\ \__/ //  //      / (|  _  \\  //      /(: (____/ //  
|: |_)  :)\        /  |: |_)  :) /\\ __ //\ |:  __   \ |: |_)  :)|:  __   \ \        /   
(_______/  \"_____/   (_______/ (__________)|__|  \___)(_______/ |__|  \___) \"_____/    
                                                                                         
"""
a14="""
  _                  _        
 |_)  _  |_      ._ |_) ._ _  
 |_) (_) |_) |_| |  |_) | (_) 
                              
"""
a15 = """
 _______  _______  _______  __   __  ______    _______  ______    _______ 
|  _    ||       ||  _    ||  | |  ||    _ |  |  _    ||    _ |  |       |
| |_|   ||   _   || |_|   ||  | |  ||   | ||  | |_|   ||   | ||  |   _   |
|       ||  | |  ||       ||  |_|  ||   |_||_ |       ||   |_||_ |  | |  |
|  _   | |  |_|  ||  _   | |       ||    __  ||  _   | |    __  ||  |_|  |
| |_|   ||       || |_|   ||       ||   |  | || |_|   ||   |  | ||       |
|_______||_______||_______||_______||___|  |_||_______||___|  |_||_______|
"""
a16 = """
==================================================================
=      ===========  =====================      ===================
=  ===  ==========  =====================  ===  ==================
=  ====  =========  =====================  ====  =================
=  ===  ====   ===  =====  =  ==  =   ===  ===  ===  =   ====   ==
=      ====     ==    ===  =  ==    =  ==      ====    =  ==     =
=  ===  ===  =  ==  =  ==  =  ==  =======  ===  ===  =======  =  =
=  ====  ==  =  ==  =  ==  =  ==  =======  ====  ==  =======  =  =
=  ===  ===  =  ==  =  ==  =  ==  =======  ===  ===  =======  =  =
=      =====   ===    ====    ==  =======      ====  ========   ==
==================================================================
"""

a17 = """
__/\\\\\\\\\\\\\__________________/\\\_____________________________________/\\\\\\\\\\\\\_______________________________        
 _\/\\\/////////\\\_______________\/\\\____________________________________\/\\\/////////\\\_____________________________       
  _\/\\\_______\/\\\_______________\/\\\____________________________________\/\\\_______\/\\\_____________________________      
   _\/\\\\\\\\\\\\\\______/\\\\\____\/\\\_________/\\\____/\\\__/\\/\\\\\\\__\/\\\\\\\\\\\\\\___/\\/\\\\\\\______/\\\\\____     
    _\/\\\/////////\\\___/\\\///\\\__\/\\\\\\\\\__\/\\\___\/\\\_\/\\\/////\\\_\/\\\/////////\\\_\/\\\/////\\\___/\\\///\\\__    
     _\/\\\_______\/\\\__/\\\__\//\\\_\/\\\////\\\_\/\\\___\/\\\_\/\\\___\///__\/\\\_______\/\\\_\/\\\___\///___/\\\__\//\\\_   
      _\/\\\_______\/\\\_\//\\\__/\\\__\/\\\__\/\\\_\/\\\___\/\\\_\/\\\_________\/\\\_______\/\\\_\/\\\_________\//\\\__/\\\__  
       _\/\\\\\\\\\\\\\/___\///\\\\\/___\/\\\\\\\\\__\//\\\\\\\\\__\/\\\_________\/\\\\\\\\\\\\\/__\/\\\__________\///\\\\\/___ 
        _\/////////////_______\/////_____\/////////____\/////////___\///__________\/////////////____\///_____________\/////_____
"""


photos = [a3,a4,a2,a,b,ab,aa,aaa, a1,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17]
photo = random.choice(photos)
