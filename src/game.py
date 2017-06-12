import cmd
from room import get_room
import textwrap
import shutil
import tempfile
import os


class Game(cmd.Cmd):
    def __init__(self, *args):
        cmd.Cmd.__init__(self)
        
        self.dbfile = tempfile.mktemp()
        shutil.copyfile("game.db",self.dbfile)
        self.loc = get_room(1, self.dbfile)
        os.system('cls')
        os.system('clear')
        self.look()

    def move(self, dir):
        newroom = self.loc._neighbours(dir)
        if newroom is None:
            print("You can't go that way")
        else:
            self.loc = get_room(newroom, self.dbfile)
            os.system('cls')
            os.system('clear')
            self.look()
            
    def look(self):
        print self.loc.name
        print
        for line in textwrap.wrap(self.loc.description, 72):
            print line

    def do_quit(self, args):
        """Leaves the game"""
        print "Than you for playing"
        return True

    def do_look(self, args):
        """describes the room"""
        self.look()

    def do_n(self, args):
        """Go north"""
        self.move('n')
    def do_s(self, args):
        """Go south"""
        self.move('s')
    def do_e(self, args):
        """Go east"""
        self.move('e')
    def do_w(self, args):
        """Go west"""
        self.move('w')
    def do_save(self, args):
        """Saves the Game"""
        shutil.copyfile(self.dbfile, args)
        print "Game saved to {0}".format(args)


def intro():
    os.system('clear')
    os.system('cls')
    introtext="YOUR PRINCESS HAS BEEN KIDNAPPED BY A BAND OF MARAUDING PICTS, WHO ARE KEEPING HER INCARCERATED IN THE DUNGEON OF A FORTRESS TO THE NORTH. YOUR TASK IS A SIMPLE ONE... RETRIEVE THE GOLD THAT WILL PAY PRINCESS'S RANSOM!"
    for line in textwrap.wrap(introtext, 72):
        print line
    raw_input("\n\nPress Enter to continue...")

if __name__ == "__main__":
    intro()
    g=Game()
    g.cmdloop()
