#Main code
#will include imports later
import sys
sys.path.append('lib/')
from rpgclient import RpgClient
from rpgdb import RpgDB
import argparse
from getpass import getpass

#TODO: add start up args
#TODO: config files?

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--token", help="Discord token for the server/channel you want to connect to", type=str)
    parser.add_argument("--verbosity", help="How verbose the logging should be. 0 is no logs. 2 is verbose.", type=int)
    parser.add_argument("-n", "--tag", help="The tag to be used to call the bot.", type=str)
    parser.add_argument("-d", "--description", help="The description of the bot.", type=str)
    parser.add_argument("-b", "--database", help="Database File Path.")
    parser.add_argument("-v", "--version", help="Display the version information.")
    parser.add_argument("-i", "--interactive", help="Interactively enter your token", action="store_true")
    parser.add_argument("-c", "--channel", help="Channel to join on server", type=str)
    args = parser.parse_args()
    if not args.token and not args.interactive:
        print("No token supplied. Exiting...")
    elif not args.database:
        print("No database path supplied. Exiting...")
    else:
        #TODO: run the bot
        print("to be implemented")
        rpgDB = RpgDB(args.database)
        rpgClient = RpgClient(rpgDB, args.tag, args.description)
        #TODO: start client with token
        token = None
        if args.interactive:
            token = getpass(prompt='Token:')
        else:
            token = args.token
        rpgClient.startup(token)
        
        #END
        del rpgClient
        del rpgDB
    print("exiting")

if __name__=="__main__":
    

    print("RPG BOT")
    main()
    
    
