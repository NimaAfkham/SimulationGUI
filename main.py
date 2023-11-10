from tkinter import *
import tkinter.ttk as ttk

def about_us():
    w.destroy()
    w2 = Tk()
    w2.geometry( "%dx%d+%d+%d" % ( 800 , 750 , 300 , 50 ) )
    w2.title("About Us" )
    w2.resizable(True,True)
    
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
    
    l1 = Label( second_frame , justify="left" ,  text="Step into the realm of system dynamics with our \n \
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

def atti_import():
    pass

def stti_import():
    pass

def confirm():
    pass

def new_project():
    w.destroy()
    w2 = Tk()
    w2.geometry( "%dx%d+%d+%d" % ( 700 , 400 , 450 , 200 ) )
    w2.title("Import Data " )
    w2.resizable(True,True)
    
    b1 = Button( w2 , text="Arrival Time Table Information " , width=30  , command=atti_import )
    b1.place( x = 100 , y = 80  )
    
    b2 = Button( w2 , text="Service Time Table Information " , width=30  , command=stti_import )
    b2.place( x = 350 , y = 80  )
   
    l2 = Label( w2 , text="Count of entry : " , font="tahoma 17 bold" )
    l2.place( x = 150 , y = 200 )
    
    packet_number = IntVar()
    e1 = Entry( w2 , textvariable = packet_number ,  font="tahoma 14 normal "  , bg="white" , fg = "black"  ,width=9  )
    e1.place ( x = 375 , y = 210 )
    
    b3 = Button( w2 , text="Confirm" , width=30  , command=confirm )
    b3.place( x = 450 , y = 350 )
    
    w2.mainloop()

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
fv.add_command(label="New Project" , command=new_project ) 
fv.add_command(label="Exit" , command=w.destroy )
fr.add_command(label="Show Tables")
fr.add_command(label="Show Charts")
fr.add_command(label="Show Statistics")
fx.add_command(label="About Us",command=about_us )
w.mainloop()