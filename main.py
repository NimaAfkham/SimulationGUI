from tkinter import *
import tkinter.ttk as ttk

global ee2 , ee3 

def about_us( w ):
    w.destroy()
    w2 = Tk()
    w2.geometry( "%dx%d+%d+%d" % ( 800 , 750 , 300 , 50 ) )
    w2.title("About Us" )
    
    #Create a Main Frame 
    main_frame = Frame( w2 )
    main_frame.pack( fill= BOTH , expand = 1 )
    
    #Create a Canvas 
    my_canvas = Canvas( main_frame )
    my_canvas.pack( side =LEFT , fill =BOTH , expand = 1 )
    
    #Add a Scrollbar to the Canvas
    my_scrollbar = ttk.Scrollbar( main_frame , orient = VERTICAL , command = my_canvas.yview )
    my_scrollbar.pack( side =RIGHT , fill = Y )
    
    #Configure the Canvas
    my_canvas.configure( yscrollcommand = my_scrollbar.set )
    my_canvas.bind( '<Configure>' , lambda e : my_canvas.configure( scrollregion = my_canvas.bbox("all") ) ) 
    
    #Create another frame inside the canvas 
    second_frame = Frame( my_canvas )
    
    #Add that new frame to a window in the canvas
    my_canvas.create_window( (0,0) , window=second_frame , anchor="nw" )
    
    l1 = Label( second_frame  ,  text="Step into the realm of system dynamics with our \n \
                   Single Server Simulation Application, a sophisticated \n \
                   tool meticulously crafted by the talented developers \n \
                   Ali Sojoudizadeh and Nima Afkham. This application is your \n \
                   gateway to the fascinating world of queuing theory, offering \n \
                    a user-friendly interface to explore the intricacies of time  \n \
                    between arrivals and server time. As you embark on your simulation \n \
                    journey, Ali and Nima's expertise shines through, ensuring a seamless experience.\n \
                    The application empowers you to input parameters with ease, \n \
                    guiding you through the process of generating simulation tables \n \
                    that unveil the inner workings of your system. Whether you're a novice \n \
                    or an experienced analyst, the user-friendly design caters to all levels \n \
                    of expertise. But it doesn't stop there. Our application goes the extra mile \n \
                    by providing in-depth statistics that illuminate key aspects of the simulation.\n \
                    Analyze the results with confidence, armed with a comprehensive understanding of single \n \
                    server dynamics. Ali and Nima's commitment to excellence is evident \n \
                    in the meticulous development of this tool, promising accuracy \n \
                    and reliability in every simulation run. To enhance your insights further,\n \
                    the application doesn't just stop at tables and statistics. \n \
                    Engage with visually appealing charts that bring the data to life, \n \
                    offering a holistic perspective on your system's performance.\n \
                    Ali and Nima's dedication to user-centric design ensures that you \n \
                    not only comprehend the results but also gain actionable insights \n \
                    for system optimization. In conclusion, Ali Sojoudizadeh and Nima Afkham \n \
                    have not just created an application; they've crafted a simulation \n \
                    experience that combines expertise, user-friendliness, and comprehensive \n \
                    analysis. Take the plunge into the world of single server dynamics \n \
                    with confidence, knowing that you have a powerful tool at \n \
                    your fingertips, courtesy of these talented developers." \
                    ,font="arial 28 normal"  , bg="white" , fg="black" )
    l1.pack()
def Arrival_Time_Table_Information( ee2 , ee3 ):
    
    list_tba = []
    list_p = []
    row_count = 0
    
    def import_data_in_atti( e2 , e3 ) :
        list_tba.append(e2.get())
        list_p.append(e3.get())
    
    def next_import ( row_count  , w3  , b3 , e2 , e3 , ee2 , ee3 ): 
        if ( row_count == 0 ) :
            import_data_in_atti( e2 , e3 )
        else :
            import_data_in_atti( ee2 , ee3 )
        next_row( row_count  , w3  , b3 , e2 , e3 , ee2 , ee3 )
        print("list tba : " , list_tba )
        print("list p : " , list_p )
        
    def next_row( row_count , w3 , b3 , e2 , e3 , ee2 , ee3 ):
        row_count += 1
        i = 50 + row_count * 50 
        w3.geometry( "%dx%d+%d+%d" % ( 850  , 100 + i , 300 , 50 ) )
        
        lextra = Label( w3 , text="Row {}".format(row_count + 1 ) , justify = LEFT , font="tahoma 10 bold" , fg="black"   )
        lextra.place( x = 10 , y= 10 + i  )
        
        tba = IntVar()
        ee2 = Entry( w3 , textvariable= tba , font="tahoma 10 normal"  , fg="black" , width=10 ) 
        ee2.place( x = 100 , y = 10 + i  )
        
        p = IntVar()
        ee3 = Entry( w3 , textvariable= p , font="tahoma 10 normal"  , fg="black" , width=10 ) 
        ee3.place( x = 265 , y = 10 + i)
        
        cp = IntVar()
        e4 = Entry( w3 , textvariable= cp , font="tahoma 10 normal"  , fg="black" , width=10 , state=DISABLED ) 
        e4.place( x = 400 , y = 10  + i)
        
        rda = IntVar()
        e5 = Entry( w3 , textvariable= rda , font="tahoma 10 normal"  , fg="black" , width=10 , state=DISABLED ) 
        e5.place( x = 575 , y = 10 + i )
        
        b3 = Button( w3 , text="+ Add Row" , width=10  , command= lambda : next_import( row_count  , w3  , b3 , e2 , e3 , ee2 , ee3 ) )
        b3.place( x = 750 , y = 60 )
        
        b4.place( x = 750 , y = 50 + i )
        
    w3 = Tk()
    w3.geometry( "%dx%d+%d+%d" % ( 850 , 150 , 300 , 50 ) )
    w3.title("Arrival Time Table Information " )
    w3.resizable(True,True)
    l3 = Label( w3 , text="Time Between Arrivals" , justify = CENTER ,  font="tahoma 10 normal" , fg="black" , width=20  )
    l3.place( x = 75 , y = 10  )
    l4 = Label( w3 , text="Probability" , justify = CENTER , font="tahoma 10 normal" , fg="black" , width=20  )
    l4.place( x = 225 , y = 10  )
    l5 = Label( w3 , text="Cummulative Probability" , justify = CENTER , font="tahoma 10 normal" , fg="black" , width=20  )
    l5.place( x = 375 , y = 10  )
    l6 = Label( w3 , text="Random Digit Assignment" , justify = CENTER , font="tahoma 10 normal" , fg="black" , width=30  )
    l6.place( x = 525 , y = 10  )
    l7 = Label( w3 , text="Row 1 " , justify = LEFT , font="tahoma 10 bold" , fg="black" )
    l7.place( x = 10 , y= 60  )
    
    tba = IntVar()
    e2 = Entry( w3 , textvariable= tba , font="tahoma 10 normal"  , fg="black" , width=10 )
    e2.place( x = 100 , y = 60 )
    
    p = IntVar()
    e3 = Entry( w3 , textvariable= p , font="tahoma 10 normal"  , fg="black" , width=10 )
    e3.place( x = 265 , y = 60 )
    
    cp = IntVar()
    e4 = Entry( w3 , textvariable= cp , font="tahoma 10 normal"  , fg="black" , width=10 , state=DISABLED ) 
    e4.place( x = 400 , y = 60 )
    
    
    rda = IntVar()
    e5 = Entry( w3 , textvariable= rda , font="tahoma 10 normal"  , fg="black" , width=10 , state=DISABLED ) 
    e5.place( x = 575 , y = 60 )
    
    
    b3 = Button( w3 , text="+ Add Row" , width=10  , command= lambda : next_import( row_count  , w3  , b3 , e2 , e3 , 0 , 0 ) )
    b3.place( x= 750 , y = 60 )
    
    b4 = Button( w3 , text="Confirm Data" , width=10  , command= lambda : Confirm_Arrival_Time_Table_Information( w3 , list_tba , list_p , e2 , e3 , row_count , ee2 , ee3 ) )
    b4.place( x= 750 , y = 100 )
    
    w3.mainloop()
def Service_Time_Table_Information():
    list_tba = []
    list_p = []
    row_count = 0
    def next_row( row_count , w4 , b3 ):
        row_count += 1
        i = 50 + row_count * 50 
        
        b3 = Button( w4 , text="+ Add Row" , width=10  , command= lambda : next_row( row_count  , w4  , b3 ) )
        b3.place( x = 750 , y = 60 )
        
        b4.place( x = 750 , y = 50 + i )
        
        w4.geometry( "%dx%d+%d+%d" % ( 850  , 100 + i , 300 , 50 ) )
            
        
        lextra = Label( w4 , text="Row {}".format(row_count + 1 ) , justify = LEFT , font="tahoma 10 bold" , fg="black"   )
        lextra.place( x = 10 , y= 10 + i  )
        
        tba = IntVar()
        e2 = Entry( w4 , textvariable= tba , font="tahoma 10 normal"  , fg="black" , width=10 ) 
        e2.place( x = 100 , y = 10 + i  )
        var1 = tba.get()
        
        p = IntVar()
        e3 = Entry( w4 , textvariable= p , font="tahoma 10 normal"  , fg="black" , width=10 ) 
        e3.place( x = 265 , y = 10 + i)
        var2 = p.get()
        
        cp = IntVar()
        e3 = Entry( w4 , textvariable= cp , font="tahoma 10 normal"  , fg="black" , width=10 , state=DISABLED ) 
        e3.place( x = 400 , y = 10  + i)
        
        
        rda = IntVar()
        e3 = Entry( w4 , textvariable= rda , font="tahoma 10 normal"  , fg="black" , width=10 , state=DISABLED ) 
        e3.place( x = 575 , y = 10 + i )
        
            
    w4 = Tk()
    w4.geometry( "%dx%d+%d+%d" % ( 850 , 150 , 300 , 50 ) )
    w4.title("Arrival Time Table Information " )
    w4.resizable(True,True)
    l3 = Label( w4 , text="Service Time" , justify = CENTER ,  font="tahoma 10 normal" , fg="black" , width=20  )
    l3.place( x = 75 , y = 10  )
    l4 = Label( w4 , text="Probability" , justify = CENTER , font="tahoma 10 normal" , fg="black" , width=20  )
    l4.place( x = 225 , y = 10  )
    l5 = Label( w4 , text="Cummulative Probability" , justify = CENTER , font="tahoma 10 normal" , fg="black" , width=20  )
    l5.place( x = 375 , y = 10  )
    l6 = Label( w4 , text="Random Digit Assignment" , justify = CENTER , font="tahoma 10 normal" , fg="black" , width=30  )
    l6.place( x = 525 , y = 10  )
    l7 = Label( w4 , text="Row 1 " , justify = LEFT , font="tahoma 10 bold" , fg="black" )
    l7.place( x = 10 , y= 60  )
    
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    
    tba = IntVar()
    e2 = Entry( w4 , textvariable= tba , font="tahoma 10 normal"  , fg="black" , width=10 )
    e2.place( x = 100 , y = 60 )
    var1 = tba.get()
    
    p = IntVar()
    e3 = Entry( w4 , textvariable= p , font="tahoma 10 normal"  , fg="black" , width=10 )
    e3.place( x = 265 , y = 60 )
    var2 = p.get()
    
    cp = IntVar()
    e3 = Entry( w4 , textvariable= cp , font="tahoma 10 normal"  , fg="black" , width=10 , state=DISABLED ) 
    e3.place( x = 400 , y = 60 )
    cp.set( var1 + var2 )
    
    rda = IntVar()
    e3 = Entry( w4 , textvariable= rda , font="tahoma 10 normal"  , fg="black" , width=10 , state=DISABLED ) 
    e3.place( x = 575 , y = 60 )
    rda.set( var1 * var2 )
    
    b3 = Button( w4 , text="+ Add Row" , width=10  , command= lambda : next_row( row_count  , w4 , b3 ) )
    b3.place( x= 750 , y = 60 )
    
    b4 = Button( w4 , text="Confirm Data" , width=10  , command=Confirm_Service_Time_Table_Information )
    b4.place( x= 750 , y = 100 )
    
    w4.mainloop()
def Confirm_Arrival_Time_Table_Information( w3 , list_tba , list_p , e2 , e3 , row_count , ee2 , ee3 ):
    
    if ( row_count == 0 ) :
        list_tba.append(e2.get())
        list_p.append(e3.get())
        print("list tba : " , list_tba )
        print("list p : " , list_p )
        w3.destroy()
    else :
        list_tba.append(ee2.get())
        list_p.append(ee3.get())
        print("list tba : " , list_tba )
        print("list p : " , list_p )
        w3.destroy()
def Confirm_Service_Time_Table_Information():
    pass
def Confirm_New_Project( w2 , e1 ) :
    packet_number = int( e1.get() )
    print("test is " , packet_number )
    w2.destroy()
    startup_menu() 
def new_project( w , ee2 , ee3 ) :
    w.destroy()
    w2 = Tk()
    w2.geometry( "%dx%d+%d+%d" % ( 700 , 400 , 450 , 200 ) )
    w2.title("Import Data " )
    w2.resizable(True,True)
    
    l1 = Label( w2 , text="Project Name " , font="tahoma 14 bold" )
    l1.place( x = 10 , y = 10 )
    
    project_name = StringVar()
    e2 = Entry( w2 , textvariable = project_name , font="tahoma 14 normal"  , fg="black" , width=20 )
    e2.place( x = 150 , y = 10 )
    
    b1 = Button( w2 , text="Arrival Time Table Information " , width=30  , command= lambda : Arrival_Time_Table_Information( ee2 , ee3 ) )
    b1.place( x = 100 , y = 80  )
    
    b2 = Button( w2 , text="Service Time Table Information " , width=30  , command=Service_Time_Table_Information )
    b2.place( x = 350 , y = 80  )
   
    l2 = Label( w2 , text="Count of entry : " , font="tahoma 17 bold" )
    l2.place( x = 150 , y = 200 )
    
    packet_number = IntVar()
    e1 = Entry( w2 , textvariable = packet_number ,  font="tahoma 14 normal "  , bg="white" , fg = "black"  ,width=9  )
    e1.place ( x = 375 , y = 210 )
    
    
    b3 = Button( w2 , text="Confirm" , width=30  , command = lambda : Confirm_New_Project( w2 , e1 ) )
    b3.place( x = 450 , y = 350 )
    
    w2.mainloop()
def startup_menu( ee2 , ee3 ):
    w = Tk()
    w.geometry( "%dx%d+%d+%d" % ( 650 , 650 , 100 , 100 ) )
    w.title("Single Server Simulation" )
    w.resizable(False,False)
    x = Menu(w)
    w.configure(menu=x)
    fv = Menu(x)
    fr = Menu(x) 
    fx = Menu(x)
    x.add_cascade(label="File",menu=fv)
    x.add_cascade(label="Project",menu=fr)
    x.add_cascade(label="About Us ",menu=fx)
    fv.add_command(label="New Project" , command=lambda : new_project( w , ee2 , ee3 ) ) 
    fv.add_command(label="Exit" , command=w.destroy )
    fr.add_command(label="Show Tables")
    fr.add_command(label="Show Charts")
    fr.add_command(label="Show Statistics")
    fx.add_command(label="About Us",command=lambda : about_us( w ) )
    w.mainloop()
startup_menu( 0 , 0 )
