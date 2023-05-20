#image _koto_blink_a:
   # alpha 0.0
  #  renpy.random.randint(3, 6)
  #  choice:
   #     alpha 1.0
    #    "mod_assets/MPT/kotonoha/eyes/koto_blink.png"
     #   0.015
      #  "mod_assets/MPT/kotonoha/eyes/koto_blinkpt2.png"
       # 0.03
        #"mod_assets/MPT/kotonoha/eyes/koto_blink.png"
        #0.015
    
    #repeat

#image _koto_blink_alt:
#    alpha 0.0
 #   renpy.random.randint(3, 6)
  #  choice:
   #     alpha 1.0
    #    "mod_assets/MPT/kotonoha/eyes/koto_blink2.png"
     #   0.015
      #  "mod_assets/MPT/kotonoha/eyes/koto_blink2pt2.png"
       # 0.03
        #"mod_assets/MPT/kotonoha/eyes/koto_blink2.png"
        #0.015
    
   # repeat



layeredimage Kotonoha toward:
    at AutofocusDisplayable(name="Kotonoha toward")

    always if_any(["uniform"]) if_not(["casual", "bikini", "hoodie", "nightgown", "tanktop", "dress", "hoodie2"]):
        "mod_assets/MPT/kotonoha/bases/base1.png"

    always if_any(["bikini"]) if_not(["casual", "uniform", "hoodie", "nightgown", "tanktop", "dress", "hoodie2"]):
        "mod_assets/MPT/kotonoha/bases/base3.png"

    always if_any(["casual"]) if_not(["uniform", "bikini", "hoodie", "nightgown", "tanktop", "dress", "hoodie2"]):
        "mod_assets/MPT/kotonoha/bases/base2.png"
    
    always if_any(["hoodie"]) if_not(["casual", "uniform", "bikini", "nightgown", "tanktop", "dress", "hoodie2"]):
        "mod_assets/MPT/kotonoha/bases/base4.png"
    
    always if_any(["hoodie2"]) if_not(["casual", "uniform", "bikini", "nightgown", "tanktop", "dress", "hoodie"]):
        "mod_assets/MPT/kotonoha/bases/base4.png"
    
    always if_any(["nightgown"]) if_not(["casual", "uniform", "bikini", "hoodie", "tanktop", "dress", "hoodie2"]):
        "mod_assets/MPT/kotonoha/bases/base5.png"
    
    always if_any(["tanktop"]) if_not(["casual", "uniform", "bikini", "hoodie", "nightgown", "dress", "hoodie2"]):
        "mod_assets/MPT/kotonoha/bases/base7.png" 
    
    always if_any(["dress"]) if_not(["casual", "uniform", "bikini", "hoodie", "nightgown", "tanktop", "hoodie2"]):
        "mod_assets/MPT/kotonoha/bases/base6.png"
        

    group outfit:

        attribute uniform default null
        attribute casual null
        attribute bikini null
        attribute hoodie null
        attribute nightgown null
        attribute tanktop null
        attribute dress null

    group mood:

        attribute neut default null #neutral
        attribute angr null #angry
        attribute curi null #curious
        attribute anno null #annoyed
        attribute cry null #cry
        attribute doub null #doubtful
        attribute dist null #distant
        attribute flus null #flustered
        attribute happ null #happy
        attribute laug null #laughing
        attribute surp null #surprised
        attribute nerv null #nervouse
        attribute sad null #sad
        attribute worr null #worried



    
    group eyes:

        attribute oe default if_any(["neut", "curi", "happ", "laug", "surp", "anno"]):
            "mod_assets/MPT/kotonoha/eyes/e1a.png"
        attribute oe default if_any(["angr", "sad"]):
            "mod_assets/MPT/kotonoha/eyes/e1d.png"
        attribute oe default if_any(["flus", "nerv", "doub", "worr", "dist"]):
            "mod_assets/MPT/kotonoha/eyes/e1c.png"
        attribute oe default if_any(["cry"]):
            "mod_assets/MPT/kotonoha/eyes/e4a.png"

        attribute ce if_any(["neut", "angr", "doub", "sad", "worr", "dist", "anno"]):
            "mod_assets/MPT/kotonoha/eyes/e2b.png"
        attribute ce if_any(["curi", "flus", "happ", "laug", "surp", "nerv"]):
            "mod_assets/MPT/kotonoha/eyes/e2a.png"
        attribute ce if_any(["cry"]):
            "mod_assets/MPT/kotonoha/eyes/e4b.png" 

        attribute e1a:
            "mod_assets/MPT/kotonoha/eyes/e1a.png"
        attribute e1b:
            "mod_assets/MPT/kotonoha/eyes/e1b.png"
        attribute e1c:
            "mod_assets/MPT/kotonoha/eyes/e1c.png"
        attribute e1d:
            "mod_assets/MPT/kotonoha/eyes/e1d.png"
        attribute e2a:
            "mod_assets/MPT/kotonoha/eyes/e2a.png"
        attribute e2b:
            "mod_assets/MPT/kotonoha/eyes/e2b.png"
        attribute e3a:
            "mod_assets/MPT/kotonoha/eyes/e3a.png"
        attribute e3b:
            "mod_assets/MPT/kotonoha/eyes/e3b.png"
        attribute e4a:
            "mod_assets/MPT/kotonoha/eyes/e4a.png"
        attribute e4b:
            "mod_assets/MPT/kotonoha/eyes/e4b.png"
    
    

    group brows:

        attribute brow default if_any(["neut", "happ", "dist"]):
            "mod_assets/MPT/kotonoha/brows/b1a.png"
        attribute brow default if_any(["angr", "anno"]):
            "mod_assets/MPT/kotonoha/brows/b1c.png"
        attribute brow default if_any(["curi", "doub"]):
            "mod_assets/MPT/kotonoha/brows/b1e.png"
        attribute brow default if_any(["flus", "laug", "nerv", "sad", "worr", "cry"]):
            "mod_assets/MPT/kotonoha/brows/b1b.png"
        attribute brow default if_any(["surp"]):
            "mod_assets/MPT/kotonoha/brows/b1d.png"

        attribute b1a:
            "mod_assets/MPT/kotonoha/brows/b1a.png"
        attribute b1b:
            "mod_assets/MPT/kotonoha/brows/b1b.png"
        attribute b1c:
            "mod_assets/MPT/kotonoha/brows/b1c.png"
        attribute b1d:
            "mod_assets/MPT/kotonoha/brows/b1d.png"
        attribute b1e:
            "mod_assets/MPT/kotonoha/brows/b1e.png"

    group mouths:

        attribute cm default if_any(["neut", "angr", "flus", "sad", "worr", "dist", "anno", "cry"]):
            "mod_assets/MPT/kotonoha/mouths/me.png"
        attribute cm default if_any(["curi", "surp", "doub"]):
            "mod_assets/MPT/kotonoha/mouths/mf.png"
        attribute cm default if_any(["happ", "laug", "nerv"]):
            "mod_assets/MPT/kotonoha/mouths/ma.png"
        
        attribute om if_any(["angr", "surp", "cry"]):
            "mod_assets/MPT/kotonoha/mouths/mg.png"
        attribute om if_any(["curi", "flus", "doub", "neut", "worr", "sad", "dist", "anno"]):
            "mod_assets/MPT/kotonoha/mouths/mb.png"
        attribute om if_any(["happ"]):
            "mod_assets/MPT/kotonoha/mouths/md.png"
        attribute om if_any(["laug", "nerv"]):
            "mod_assets/MPT/kotonoha/mouths/mc.png"

        attribute ma:
            "mod_assets/MPT/kotonoha/mouths/ma.png"
        attribute mb:
            "mod_assets/MPT/kotonoha/mouths/mb.png"
        attribute mc:
            "mod_assets/MPT/kotonoha/mouths/mc.png"
        attribute md:
            "mod_assets/MPT/kotonoha/mouths/md.png"
        attribute me:
            "mod_assets/MPT/kotonoha/mouths/me.png"
        attribute mf:
            "mod_assets/MPT/kotonoha/mouths/mf.png"
        attribute mg:
            "mod_assets/MPT/kotonoha/mouths/mg.png"

    group noses:

        attribute nose default if_any(["neut", "angr", "curi", "doub", "flus", "happ", "laug", "surp", "sad", "dist", "anno", "cry"]):
            "mod_assets/MPT/kotonoha/noses/n1.png"
        attribute nose default if_any(["worr"]):
            "mod_assets/MPT/kotonoha/noses/n2.png"
        attribute nose default if_any(["nerv"]):
            "mod_assets/MPT/kotonoha/noses/n3.png"
        
        attribute n1:
            "mod_assets/MPT/kotonoha/noses/n1.png"
        attribute n2:
            "mod_assets/MPT/kotonoha/noses/n2.png"
        attribute n3:
            "mod_assets/MPT/kotonoha/noses/n3.png"

    group right:
        anchor (0,0) subpixel (True)
        

        attribute rdown default if_any("uniform"):
            "mod_assets/MPT/kotonoha/clothes/uniform/rdown.png" xoffset -1 yoffset -0.6
        attribute rdown default if_any("casual"):
            "mod_assets/MPT/kotonoha/clothes/casual/rdown.png" yoffset -0.6
        attribute rdown default if_any("bikini"):
            "mod_assets/MPT/kotonoha/clothes/bikini/rdown.png" xoffset -0.9 yoffset 0.2
        attribute rdown default if_any("hoodie"):
            "mod_assets/MPT/kotonoha/clothes/hoodie/rdown.png" yoffset -1.0
        attribute rdown default if_any("hoodie2"):
            "mod_assets/MPT/kotonoha/clothes/hoodie2/rdown.png"
        attribute rdown default if_any(["nightgown"]):
            "mod_assets/MPT/kotonoha/clothes/nightgown/rdown.png" xoffset -0.8
        attribute rdown default if_any(["tanktop"]):
            "mod_assets/MPT/kotonoha/clothes/tanktop/rdown.png" xoffset -0.85
        attribute rdown default if_any(["dress"]):
            "mod_assets/MPT/kotonoha/clothes/dress/rdown.png" xoffset -1.0
            
            

        attribute rbehind if_any(["uniform"]):
            "mod_assets/MPT/kotonoha/clothes/uniform/rbehind.png" yoffset -1.0 xoffset -1.0
        attribute rbehind if_any(["casual"]):
            "mod_assets/MPT/kotonoha/clothes/casual/rbehind.png" yoffset -1.0
        attribute rbehind if_any(["bikini"]):
            "mod_assets/MPT/kotonoha/clothes/bikini/rbehind.png" yoffset 0.0 xoffset -0.75
        attribute rbehind if_any(["hoodie"]):
            "mod_assets/MPT/kotonoha/clothes/hoodie/rbehind.png" yoffset -1.0
        attribute rbehind if_any(["hoodie2"]):
            "mod_assets/MPT/kotonoha/clothes/hoodie2/rbehind.png"
        attribute rbehind if_any(["nightgown"]):
            "mod_assets/MPT/kotonoha/clothes/nightgown/rbehind.png" xoffset -0.9
        attribute rbehind if_any(["tanktop"]):
            "mod_assets/MPT/kotonoha/clothes/tanktop/rbehind.png" xoffset -0.9
        attribute rbehind if_any(["dress"]):
            "mod_assets/MPT/kotonoha/clothes/dress/rbehind.png" xoffset -1.0
            
            

        attribute rhip if_any(["uniform"]):
            "mod_assets/MPT/kotonoha/clothes/uniform/rhip.png" yoffset -1.0 xoffset -1.0
        attribute rhip if_any(["casual"]):
            "mod_assets/MPT/kotonoha/clothes/casual/rhip.png" yoffset -1.0
        attribute rhip if_any(["bikini"]):
            "mod_assets/MPT/kotonoha/clothes/bikini/rhip.png" yoffset 0.0 xoffset -0.75
        attribute rhip if_any(["hoodie"]):
            "mod_assets/MPT/kotonoha/clothes/hoodie/rhip.png" yoffset -1.0
        attribute rhip if_any(["hoodie2"]):
            "mod_assets/MPT/kotonoha/clothes/hoodie2/rhip.png"
        attribute rhip if_any(["nightgown"]):
            "mod_assets/MPT/kotonoha/clothes/nightgown/rhip.png" xoffset -0.9
        attribute rhip if_any(["tanktop"]):
            "mod_assets/MPT/kotonoha/clothes/tanktop/rhip.png" xoffset -0.9
        attribute rhip if_any(["dress"]):
            "mod_assets/MPT/kotonoha/clothes/dress/rhip.png" xoffset -1.0
     
    group left:
        anchor (0,0) subpixel (True)
        

        attribute ldown default if_any(["uniform"]):
            "mod_assets/MPT/kotonoha/clothes/uniform/ldown.png"
        attribute ldown default if_any(["casual"]):
            "mod_assets/MPT/kotonoha/clothes/casual/ldown.png"
        attribute ldown default if_any(["bikini"]):
            "mod_assets/MPT/kotonoha/clothes/bikini/ldown.png"
        attribute ldown default if_any(["hoodie"]):
            "mod_assets/MPT/kotonoha/clothes/hoodie/ldown.png"
        attribute ldown default if_any(["hoodie2"]):
            "mod_assets/MPT/kotonoha/clothes/hoodie2/ldown.png"
        attribute ldown default if_any(["nightgown"]):
            "mod_assets/MPT/kotonoha/clothes/nightgown/ldown.png" xoffset -0.5
        attribute ldown default if_any(["tanktop"]):
            "mod_assets/MPT/kotonoha/clothes/tanktop/ldown.png" xoffset -0.5
        attribute ldown default if_any(["dress"]):
            "mod_assets/MPT/kotonoha/clothes/dress/ldown.png" 
            

        attribute lchest if_any(["uniform"]):
            "mod_assets/MPT/kotonoha/clothes/uniform/lchest.png"
        attribute lchest if_any(["casual"]):
            "mod_assets/MPT/kotonoha/clothes/casual/lchest.png"
        attribute lchest if_any(["bikini"]):
            "mod_assets/MPT/kotonoha/clothes/bikini/lchest.png"
        attribute lchest if_any(["hoodie"]):
            "mod_assets/MPT/kotonoha/clothes/hoodie/lchest.png"
        attribute lchest if_any(["hoodie2"]):
            "mod_assets/MPT/kotonoha/clothes/hoodie2/lchest.png"
        attribute lchest if_any(["nightgown"]):
            "mod_assets/MPT/kotonoha/clothes/nightgown/lchest.png" xoffset -0.5
        attribute lchest if_any(["tanktop"]):
            "mod_assets/MPT/kotonoha/clothes/tanktop/lchest.png" xoffset -0.5
        attribute lchest if_any(["dress"]):
            "mod_assets/MPT/kotonoha/clothes/dress/lchest.png"
                    

        attribute lup if_any(["uniform"]):
            "mod_assets/MPT/kotonoha/clothes/uniform/lup.png"
        attribute lup if_any(["casual"]):
            "mod_assets/MPT/kotonoha/clothes/casual/lup.png"
        attribute lup if_any(["bikini"]):
            "mod_assets/MPT/kotonoha/clothes/bikini/lup.png"
        attribute lup if_any(["hoodie"]):
            "mod_assets/MPT/kotonoha/clothes/hoodie/lup.png"
        attribute lup if_any(["hoodie2"]):
            "mod_assets/MPT/kotonoha/clothes/hoodie2/lup.png"
        attribute lup if_any(["nightgown"]):
            "mod_assets/MPT/kotonoha/clothes/nightgown/lup.png" xoffset -0.5
        attribute lup if_any(["tanktop"]):
            "mod_assets/MPT/kotonoha/clothes/tanktop/lup.png" xoffset -0.5
        attribute lup if_any(["dress"]):
            "mod_assets/MPT/kotonoha/clothes/dress/lup.png"
            

    
layeredimage Kotonoha sweater:
    at AutofocusDisplayable(name="Kotonoha sweater")

    
    group outfit:

        attribute uniform default null
    

    group mood:

        attribute neut default null #neutral
        attribute angr null #angry
        attribute curi null #curious
        attribute anno null #annoyed
        attribute cry null #cry
        attribute doub null #doubtful
        attribute dist null #distant
        attribute flus null #flustered
        attribute happ null #happy
        attribute laug null #laughing
        attribute surp null #surprised
        attribute nerv null #nervouse
        attribute sad null #sad
        attribute worr null #worried


    group right:
        anchor (0,0) subpixel (True)
        

        attribute rdown default if_any("uniform"):
            "mod_assets/MPT/kotonoha/clothes/sweater/rdown.png" xoffset -1 yoffset -0.6
        
        attribute rbehind if_any(["uniform"]):
            "mod_assets/MPT/kotonoha/clothes/sweater/rbehind.png" yoffset -1.0 xoffset -1.0

        attribute rhip if_any(["uniform"]):
            "mod_assets/MPT/kotonoha/clothes/sweater/rhip.png" yoffset -1.0 xoffset -1.0

     
    group left:
        anchor (0,0) subpixel (True)
        

        attribute ldown default if_any(["uniform"]):
            "mod_assets/MPT/kotonoha/clothes/sweater/ldown.png"


        attribute lchest if_any(["uniform"]):
            "mod_assets/MPT/kotonoha/clothes/sweater/lchest.png"

                    

        attribute lup if_any(["uniform"]):
            "mod_assets/MPT/kotonoha/clothes/sweater/lup.png"
    
    group eyes:

        attribute oe default if_any(["neut", "curi", "happ", "laug", "surp", "anno"]):
            "mod_assets/MPT/kotonoha/eyes/e1a.png"
        attribute oe default if_any(["angr", "sad"]):
            "mod_assets/MPT/kotonoha/eyes/e1d.png"
        attribute oe default if_any(["flus", "nerv", "doub", "worr", "dist"]):
            "mod_assets/MPT/kotonoha/eyes/e1c.png"
        attribute oe default if_any(["cry"]):
            "mod_assets/MPT/kotonoha/eyes/e4a.png"

        attribute ce if_any(["neut", "angr", "doub", "sad", "worr", "dist", "anno"]):
            "mod_assets/MPT/kotonoha/eyes/e2b.png"
        attribute ce if_any(["curi", "flus", "happ", "laug", "surp", "nerv"]):
            "mod_assets/MPT/kotonoha/eyes/e2a.png"
        attribute ce if_any(["cry"]):
            "mod_assets/MPT/kotonoha/eyes/e4b.png" 

        attribute e1a:
            "mod_assets/MPT/kotonoha/eyes/e1a.png"
        attribute e1b:
            "mod_assets/MPT/kotonoha/eyes/e1b.png"
        attribute e1c:
            "mod_assets/MPT/kotonoha/eyes/e1c.png"
        attribute e1d:
            "mod_assets/MPT/kotonoha/eyes/e1d.png"
        attribute e2a:
            "mod_assets/MPT/kotonoha/eyes/e2a.png"
        attribute e2b:
            "mod_assets/MPT/kotonoha/eyes/e2b.png"
        attribute e3a:
            "mod_assets/MPT/kotonoha/eyes/e3a.png"
        attribute e3b:
            "mod_assets/MPT/kotonoha/eyes/e3b.png"
        attribute e4a:
            "mod_assets/MPT/kotonoha/eyes/e4a.png"
        attribute e4b:
            "mod_assets/MPT/kotonoha/eyes/e4b.png"
    
    

    group brows:

        attribute brow default if_any(["neut", "happ", "dist"]):
            "mod_assets/MPT/kotonoha/brows/b1a.png"
        attribute brow default if_any(["angr", "anno"]):
            "mod_assets/MPT/kotonoha/brows/b1c.png"
        attribute brow default if_any(["curi", "doub"]):
            "mod_assets/MPT/kotonoha/brows/b1e.png"
        attribute brow default if_any(["flus", "laug", "nerv", "sad", "worr", "cry"]):
            "mod_assets/MPT/kotonoha/brows/b1b.png"
        attribute brow default if_any(["surp"]):
            "mod_assets/MPT/kotonoha/brows/b1d.png"

        attribute b1a:
            "mod_assets/MPT/kotonoha/brows/b1a.png"
        attribute b1b:
            "mod_assets/MPT/kotonoha/brows/b1b.png"
        attribute b1c:
            "mod_assets/MPT/kotonoha/brows/b1c.png"
        attribute b1d:
            "mod_assets/MPT/kotonoha/brows/b1d.png"
        attribute b1e:
            "mod_assets/MPT/kotonoha/brows/b1e.png"

    group mouths:

        attribute cm default if_any(["neut", "angr", "flus", "sad", "worr", "dist", "anno", "cry"]):
            "mod_assets/MPT/kotonoha/mouths/me.png"
        attribute cm default if_any(["curi", "surp", "doub"]):
            "mod_assets/MPT/kotonoha/mouths/mf.png"
        attribute cm default if_any(["happ", "laug", "nerv"]):
            "mod_assets/MPT/kotonoha/mouths/ma.png"
        
        attribute om if_any(["angr", "surp", "cry"]):
            "mod_assets/MPT/kotonoha/mouths/mg.png"
        attribute om if_any(["curi", "flus", "doub", "neut", "worr", "sad", "dist", "anno"]):
            "mod_assets/MPT/kotonoha/mouths/mb.png"
        attribute om if_any(["happ"]):
            "mod_assets/MPT/kotonoha/mouths/md.png"
        attribute om if_any(["laug", "nerv"]):
            "mod_assets/MPT/kotonoha/mouths/mc.png"

        attribute ma:
            "mod_assets/MPT/kotonoha/mouths/ma.png"
        attribute mb:
            "mod_assets/MPT/kotonoha/mouths/mb.png"
        attribute mc:
            "mod_assets/MPT/kotonoha/mouths/mc.png"
        attribute md:
            "mod_assets/MPT/kotonoha/mouths/md.png"
        attribute me:
            "mod_assets/MPT/kotonoha/mouths/me.png"
        attribute mf:
            "mod_assets/MPT/kotonoha/mouths/mf.png"
        attribute mg:
            "mod_assets/MPT/kotonoha/mouths/mg.png"

    group noses:

        attribute nose default if_any(["neut", "angr", "curi", "doub", "flus", "happ", "laug", "surp", "sad", "dist", "anno", "cry"]):
            "mod_assets/MPT/kotonoha/noses/n1.png"
        attribute nose default if_any(["worr"]):
            "mod_assets/MPT/kotonoha/noses/n2.png"
        attribute nose default if_any(["nerv"]):
            "mod_assets/MPT/kotonoha/noses/n3.png"
        
        attribute n1:
            "mod_assets/MPT/kotonoha/noses/n1.png"
        attribute n2:
            "mod_assets/MPT/kotonoha/noses/n2.png"
        attribute n3:
            "mod_assets/MPT/kotonoha/noses/n3.png"

    

            
            

    





layeredimage Kotonoha ponytail:
    at AutofocusDisplayable(name="Kotonoha ponytail")

    always if_any(["uniform"]) if_not(["casual", "bikini", "nightgown", "dress"]):
        "mod_assets/MPT/kotonoha/bases/pbase1.png"

    always if_any(["bikini"]) if_not(["casual", "uniform", "nightgown", "dress"]):
        "mod_assets/MPT/kotonoha/bases/pbase3.png"

    always if_any(["casual"]) if_not(["uniform", "bikini", "nightgown", "dress"]):
        "mod_assets/MPT/kotonoha/bases/pbase2.png"
    
    always if_any(["nightgown"]) if_not(["uniform", "bikini", "casual", "dress"]):
        "mod_assets/MPT/kotonoha/bases/pbase4.png"

    always if_any(["dress"]) if_not(["uniform", "bikini", "casual", "nightgown"]):
        "mod_assets/MPT/kotonoha/bases/pbase5.png"

    group outfit:

        attribute uniform default null
        attribute casual null
        attribute bikini null
        attribute nightgown null
        attribute dress null

    group mood:

        attribute neut default null #neutral
        attribute angr null #angry
        attribute curi null #curious
        attribute anno null #annoyed
        attribute cry null #cry
        attribute doub null #doubtful
        attribute dist null #distant
        attribute flus null #flustered
        attribute happ null #happy
        attribute laug null #laughing
        attribute surp null #surprised
        attribute nerv null #nervouse
        attribute sad null #sad
        attribute worr null #worried



    
    group eyes:

        attribute oe default if_any(["neut", "curi", "happ", "laug", "surp", "anno"]):
            "mod_assets/MPT/kotonoha/eyes/e1a.png"
        attribute oe default if_any(["angr", "sad"]):
            "mod_assets/MPT/kotonoha/eyes/e1d.png"
        attribute oe default if_any(["flus", "nerv", "doub", "worr", "dist"]):
            "mod_assets/MPT/kotonoha/eyes/e1c.png"
        attribute oe default if_any(["cry"]):
            "mod_assets/MPT/kotonoha/eyes/e4a.png"

        attribute ce if_any(["neut", "angr", "doub", "sad", "worr", "dist", "anno"]):
            "mod_assets/MPT/kotonoha/eyes/e2b.png"
        attribute ce if_any(["curi", "flus", "happ", "laug", "surp", "nerv"]):
            "mod_assets/MPT/kotonoha/eyes/e2a.png"
        attribute ce if_any(["cry"]):
            "mod_assets/MPT/kotonoha/eyes/e4b.png" 

        attribute e1a:
            "mod_assets/MPT/kotonoha/eyes/e1a.png"
        attribute e1b:
            "mod_assets/MPT/kotonoha/eyes/e1b.png"
        attribute e1c:
            "mod_assets/MPT/kotonoha/eyes/e1c.png"
        attribute e1d:
            "mod_assets/MPT/kotonoha/eyes/e1d.png"
        attribute e2a:
            "mod_assets/MPT/kotonoha/eyes/e2a.png"
        attribute e2b:
            "mod_assets/MPT/kotonoha/eyes/e2b.png"
        attribute e3a:
            "mod_assets/MPT/kotonoha/eyes/e3a.png"
        attribute e3b:
            "mod_assets/MPT/kotonoha/eyes/e3b.png"
        attribute e4a:
            "mod_assets/MPT/kotonoha/eyes/e4a.png"
        attribute e4b:
            "mod_assets/MPT/kotonoha/eyes/e4b.png"

    group brows:

        attribute brow default if_any(["neut", "happ", "dist"]):
            "mod_assets/MPT/kotonoha/brows/b1a.png"
        attribute brow default if_any(["angr", "anno"]):
            "mod_assets/MPT/kotonoha/brows/b1c.png"
        attribute brow default if_any(["curi", "doub"]):
            "mod_assets/MPT/kotonoha/brows/b1e.png"
        attribute brow default if_any(["flus", "laug", "nerv", "sad", "worr", "cry"]):
            "mod_assets/MPT/kotonoha/brows/b1b.png"
        attribute brow default if_any(["surp"]):
            "mod_assets/MPT/kotonoha/brows/b1d.png"

        attribute b1a:
            "mod_assets/MPT/kotonoha/brows/b1a.png"
        attribute b1b:
            "mod_assets/MPT/kotonoha/brows/b1b.png"
        attribute b1c:
            "mod_assets/MPT/kotonoha/brows/b1c.png"
        attribute b1d:
            "mod_assets/MPT/kotonoha/brows/b1d.png"
        attribute b1e:
            "mod_assets/MPT/kotonoha/brows/b1e.png"

    group mouths:

        attribute cm default if_any(["neut", "angr", "flus", "sad", "worr", "dist", "anno", "cry"]):
            "mod_assets/MPT/kotonoha/mouths/me.png"
        attribute cm default if_any(["curi", "surp", "doub"]):
            "mod_assets/MPT/kotonoha/mouths/mf.png"
        attribute cm default if_any(["happ", "laug", "nerv"]):
            "mod_assets/MPT/kotonoha/mouths/ma.png"
        
        attribute om if_any(["angr", "surp", "cry"]):
            "mod_assets/MPT/kotonoha/mouths/mg.png"
        attribute om if_any(["curi", "flus", "doub", "neut", "worr", "sad", "dist", "anno"]):
            "mod_assets/MPT/kotonoha/mouths/mb.png"
        attribute om if_any(["happ"]):
            "mod_assets/MPT/kotonoha/mouths/md.png"
        attribute om if_any(["laug", "nerv"]):
            "mod_assets/MPT/kotonoha/mouths/mc.png"

        attribute ma:
            "mod_assets/MPT/kotonoha/mouths/ma.png"
        attribute mb:
            "mod_assets/MPT/kotonoha/mouths/mb.png"
        attribute mc:
            "mod_assets/MPT/kotonoha/mouths/mc.png"
        attribute md:
            "mod_assets/MPT/kotonoha/mouths/md.png"
        attribute me:
            "mod_assets/MPT/kotonoha/mouths/me.png"
        attribute mf:
            "mod_assets/MPT/kotonoha/mouths/mf.png"
        attribute mg:
            "mod_assets/MPT/kotonoha/mouths/mg.png"

    group noses:

        attribute nose default if_any(["neut", "angr", "curi", "doub", "flus", "happ", "laug", "surp", "sad", "dist", "anno", "cry"]):
            "mod_assets/MPT/kotonoha/noses/n1.png"
        attribute nose default if_any(["worr"]):
            "mod_assets/MPT/kotonoha/noses/n2.png"
        attribute nose default if_any(["nerv"]):
            "mod_assets/MPT/kotonoha/noses/n3.png"
        
        attribute n1:
            "mod_assets/MPT/kotonoha/noses/n1.png"
        attribute n2:
            "mod_assets/MPT/kotonoha/noses/n2.png"
        attribute n3:
            "mod_assets/MPT/kotonoha/noses/n3.png"

    

    group right:
        anchor (0,0) subpixel (True)
        #yoffset (-1.0) xoffset(-1.0)

        attribute rdown default if_any("uniform"):
            "mod_assets/MPT/kotonoha/clothes/uniform/prdown.png"
        attribute rdown default if_any("casual"):
            "mod_assets/MPT/kotonoha/clothes/casual/prdown.png"
        attribute rdown default if_any("bikini"):
            "mod_assets/MPT/kotonoha/clothes/bikini/prdown.png"
        attribute rdown default if_any(["nightgown"]):
            "mod_assets/MPT/kotonoha/clothes/nightgown/prdown.png"
        attribute rdown default if_any(["dress"]):
            "mod_assets/MPT/kotonoha/clothes/dress/prdown.png"

        attribute rbehind if_any(["uniform"]):
            "mod_assets/MPT/kotonoha/clothes/uniform/prbehind.png"
        attribute rbehind if_any(["casual"]):
            "mod_assets/MPT/kotonoha/clothes/casual/prbehind.png"
        attribute rbehind if_any(["bikini"]):
            "mod_assets/MPT/kotonoha/clothes/bikini/prbehind.png"
        attribute rbehind if_any(["nightgown"]):
            "mod_assets/MPT/kotonoha/clothes/nightgown/prbehind.png"
        attribute rbehind if_any(["dress"]):
            "mod_assets/MPT/kotonoha/clothes/dress/prbehind.png"

        attribute rhip if_any(["uniform"]):
            "mod_assets/MPT/kotonoha/clothes/uniform/prhip.png"
        attribute rhip if_any(["casual"]):
            "mod_assets/MPT/kotonoha/clothes/casual/prhip.png"
        attribute rhip if_any(["bikini"]):
            "mod_assets/MPT/kotonoha/clothes/bikini/prhip.png"
        attribute rhip if_any(["nightgown"]):
            "mod_assets/MPT/kotonoha/clothes/nightgown/prhip.png"
        attribute rhip if_any(["dress"]):
            "mod_assets/MPT/kotonoha/clothes/dress/prhip.png"

    group left:
        anchor (0,0) subpixel (True)
        #yoffset (-0.5) xoffset(-0.5)

        attribute ldown default if_any(["uniform"]):
            "mod_assets/MPT/kotonoha/clothes/uniform/pldown.png"
        attribute ldown default if_any(["casual"]):
            "mod_assets/MPT/kotonoha/clothes/casual/pldown.png"
        attribute ldown default if_any(["bikini"]):
            "mod_assets/MPT/kotonoha/clothes/bikini/pldown.png"
        attribute ldown default if_any(["nightgown"]):
            "mod_assets/MPT/kotonoha/clothes/nightgown/pldown.png"
        attribute ldown default if_any(["dress"]):
            "mod_assets/MPT/kotonoha/clothes/dress/pldown.png"

        attribute lchest if_any(["uniform"]):
            "mod_assets/MPT/kotonoha/clothes/uniform/plchest.png"
        attribute lchest if_any(["casual"]):
            "mod_assets/MPT/kotonoha/clothes/casual/plchest.png"
        attribute lchest if_any(["bikini"]):
            "mod_assets/MPT/kotonoha/clothes/bikini/plchest.png"
        attribute lchest if_any(["nightgown"]):
            "mod_assets/MPT/kotonoha/clothes/nightgown/plchest.png"
        attribute lchest if_any(["dress"]):
            "mod_assets/MPT/kotonoha/clothes/dress/plchest.png"

        attribute lup if_any(["uniform"]):
            "mod_assets/MPT/kotonoha/clothes/uniform/plup.png"
        attribute lup if_any(["casual"]):
            "mod_assets/MPT/kotonoha/clothes/casual/plup.png"
        attribute lup if_any(["bikini"]):
            "mod_assets/MPT/kotonoha/clothes/bikini/plup.png"
        attribute lup if_any(["nightgown"]):
            "mod_assets/MPT/kotonoha/clothes/nightgown/plup.png"
        attribute lup if_any(["dress"]):
            "mod_assets/MPT/kotonoha/clothes/dress/plup.png"
