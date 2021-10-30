import cssutils as css
from cssutils.css import CSSStyleRule
import os

style = ""

while True:
    cmd = input("css >> ")
    if cmd == "quit":
        break
    elif cmd == "help":
        print("""
        CSSScripts - A tool for generating CSS for your Sphinx projects
        
        Commands:
            quit - exit program
            help - this message
            select <style> - select style from inbuilt styles
            list - list inbuilt styles
            save [file] - save selected style with edits
            rm <selector> - remove selector from style
            edit <selector> <tag> <new value> - change style of selector
            add <selector> <css string> - add style
            view - view current style
            url <style> - get raw file URL for the style
        """)
    elif cmd.startswith("select"):
        name = cmd.split()[1]
        style = open("css/"+name+".css", "r").read()
    elif cmd.startswith("url"):
        name = cmd.split()[1]
        print(f"https://github.com/FoxNerdSaysMoo/CSSScripts/raw/master/css/{name}.css")
    elif cmd == "list":
        print("\n".join(os.listdir("css")))
    elif cmd == "view":
        print(style)
    elif cmd.startswith("save"):
        name = cmd.split()
        file = "out.css"
        if len(name) > 1:
            file = name[1]
        with open(file, "w") as write:
            write.write(style)
        print("Saved style to", file)
    elif cmd.startswith("edit"):
        args = cmd.split()
        edit = css.parseString(style)
        styles = edit.cssRules
        for s in styles:
            if s.type == s.STYLE_RULE:
                if s.selectorList.selectorText == args[1]:
                    s.style[args[2]] = args[3]
        style = edit.cssText.decode("utf-8")
    elif cmd.startswith("rm"):
        args = cmd.split()
        edit = css.parseString(style)
        styles = edit.cssRules
        for s in styles:
            if s.type == s.STYLE_RULE:
                if s.selectorList.selectorText == args[1]:
                    styles.remove(s)
        style = edit.cssText.decode("utf-8")
    elif cmd.startswith("add"):
        args = cmd.split()
        edit = css.parseString(style)
        styles = edit.cssRules
        styles.insert(
            0,
            CSSStyleRule(args[1], " ".join(args[2:]))
        )
        style = edit.cssText.decode("utf-8")

