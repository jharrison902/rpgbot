#Main code
#will include imports later
import sys
sys.path.append('lib/')
import rpgclient
import rpgdb
import argparse

#TODO: add start up args
#TODO: config files?

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--token", help="Discord token for the server/channel you want to connect to", type=str)
    parser.add_argument("--verbosity", help="How verbose the logging should be. 0 is no logs. 2 is verbose.", type=int)
    parser.add_argument("-n", "--tag", help="The tag to be used to call the bot.", type=str)
    parser.add_argument("-d", "--description", help="The description of the bot.", type=str)
    parser.add_argument("-v", "--version", help="Display the version information.")
    args = parser.parse_args()
    if not args.token:
        print("No token supplied. Exiting...")
    else:
        #TODO: run the bot
        print("to be implemented")
    print("exiting")

if __name__=="__main__":
    

    print("RPG BOT")
    main()
    
    
