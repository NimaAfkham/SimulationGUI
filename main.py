from tkinter import *
import tkinter.ttk as ttk
import sqlite3 as db 
import os 
import random

#global variables
database_path = ""
row_count_of_arrival_time_table_information = 0
row_count_of_service_time_table_information = 0
List_of_ATTI_Time_Between_Arrivals = []
List_of_ATTI_Probability = []
List_of_STTI_Service_Time = []
List_of_STTI_Probability = []
List_of_ATTI_Random_Digit_Lower_Limit = []
List_of_ATTI_Random_Digit_Upper_Limit = []
List_of_STTI_Random_Digit_Lower_Limit = []
List_of_STTI_Random_Digit_Upper_Limit = []
count_of_entry = 0
tedad_ashar_atti = 0
tedad_ashar_stti = 0
#/global variables


#Processing 
def Arrival_Time_Table_Information_Processing():
    global row_count_of_arrival_time_table_information
    global List_of_ATTI_Time_Between_Arrivals 
    global List_of_ATTI_Probability 
    global tedad_ashar_atti
    global List_of_ATTI_Random_Digit_Lower_Limit 
    global List_of_ATTI_Random_Digit_Upper_Limit 
    List_of_ATTI_Cummulative_Probability = []
    
    List_of_ATTI_Cummulative_Probability.append( float(List_of_ATTI_Probability[0]) )
    for i in range(1 , len(List_of_ATTI_Probability)) :
        List_of_ATTI_Cummulative_Probability.append(float(List_of_ATTI_Probability[i]) + List_of_ATTI_Cummulative_Probability[i - 1])
    
    minimum = 1.1 
    for i in range(len(List_of_ATTI_Time_Between_Arrivals)) :
    
        if ( float(List_of_ATTI_Probability[i]) < minimum ):
        
            minimum = float(List_of_ATTI_Probability[i])

    tedad_ashar = 0     
    for i in range(1,7) : 
        if ( minimum * 10 ** i - int(minimum * 10 ** i ) > 0 ) :
            tedad_ashar += 1 
        else :
            break
    tedad_ashar += 1 
    
    tedad_ashar_atti=tedad_ashar
    
    List_of_ATTI_Random_Digit_Lower_Limit.append("1")
    List_of_ATTI_Random_Digit_Upper_Limit.append( List_of_ATTI_Cummulative_Probability[0] * 10 ** tedad_ashar )
    for i in range( 1 , len(List_of_ATTI_Time_Between_Arrivals) ) :
        List_of_ATTI_Random_Digit_Upper_Limit.append( List_of_ATTI_Cummulative_Probability[i] * 10 ** tedad_ashar )
        List_of_ATTI_Random_Digit_Lower_Limit.append( List_of_ATTI_Random_Digit_Upper_Limit[i-1] + 1 )
        
    
    
    con = db.connect( database_path )
    cur = con.cursor()
    for i in range( len(List_of_ATTI_Time_Between_Arrivals) ) : 
        cur.execute('''update DTBA set "cummulative probability" = {} where "time between arrivals" = "{}" ;'''.format( List_of_ATTI_Cummulative_Probability[i] , List_of_ATTI_Time_Between_Arrivals[i] ) ) 
    for i in range( len(List_of_ATTI_Time_Between_Arrivals) ) : 
        cur.execute('''update DTBA set "random digit assignment" = "{}" where "time between arrivals" = "{}" ;'''.format( str(List_of_ATTI_Random_Digit_Lower_Limit[i]) + "_" + str(List_of_ATTI_Random_Digit_Upper_Limit[i]) , List_of_ATTI_Time_Between_Arrivals[i] ) )
    con.commit()
    con.close() 
    
def Service_Time_Table_Information_Processing():
    global row_count_of_service_time_table_information
    global List_of_STTI_Service_Time 
    global List_of_STTI_Probability 
    global tedad_ashar_stti
    global List_of_STTI_Random_Digit_Lower_Limit 
    global List_of_STTI_Random_Digit_Upper_Limit 
    List_of_STTI_Cummulative_Probability = []
    
    List_of_STTI_Cummulative_Probability.append( float(List_of_STTI_Probability[0]) )
    for i in range(1 , len(List_of_STTI_Probability)) :
        List_of_STTI_Cummulative_Probability.append(float(List_of_STTI_Probability[i]) + List_of_STTI_Cummulative_Probability[i - 1])
    
    minimum = 1.1 
    for i in range(len(List_of_STTI_Service_Time)) :
    
        if ( float(List_of_STTI_Probability[i]) < minimum ):
        
            minimum = float(List_of_STTI_Probability[i])

    tedad_ashar = 0     
    for i in range(1,7) : 
        if ( minimum * 10 ** i - int(minimum * 10 ** i ) > 0 ) :
            tedad_ashar += 1 
        else :
            break
    tedad_ashar += 1
    tedad_ashar_stti=tedad_ashar
    
    List_of_STTI_Random_Digit_Lower_Limit.append("1")
    List_of_STTI_Random_Digit_Upper_Limit.append( List_of_STTI_Cummulative_Probability[0] * 10 ** tedad_ashar )
    for i in range( 1 , len(List_of_STTI_Service_Time) ) :
        List_of_STTI_Random_Digit_Upper_Limit.append( List_of_STTI_Cummulative_Probability[i] * 10 ** tedad_ashar )
        List_of_STTI_Random_Digit_Lower_Limit.append( List_of_STTI_Random_Digit_Upper_Limit[i-1] + 1 )
        
    
    
    con = db.connect(database_path )
    cur = con.cursor()
    for i in range( len(List_of_STTI_Service_Time) ) : 
        cur.execute('''update DST set "cummulative probability" = {} where "service time" = "{}" ;'''.format( List_of_STTI_Cummulative_Probability[i] , List_of_STTI_Service_Time[i] ) ) 
    for i in range( len(List_of_STTI_Service_Time) ) : 
        cur.execute('''update DST set "random digit assignment" = "{}" where "service time" = "{}" ;'''.format( str(List_of_STTI_Random_Digit_Lower_Limit[i]) + "_" + str(List_of_STTI_Random_Digit_Upper_Limit[i]) , List_of_STTI_Service_Time[i] ) )
    con.commit()
    con.close()
    
def Time_Between_Arrivals_Determination_Processing() :
    global List_of_ATTI_Random_Digit_Lower_Limit 
    global List_of_ATTI_Random_Digit_Upper_Limit
    tbadet_rand_digit=[]
    con = db.connect(database_path )
    cur = con.cursor()
    for i in range( count_of_entry ) : 
        if count_of_entry == 0 :
            cur.execute('''update TBADet set "random digit" = {} where customer = {} ;'''.format( 'NULL'  , i + 1 ) )
            cur.execute('''update TBADet set "time between arrivals" = {} where customer = {} ;'''.format( 'NULL' , i + 1 ) )
        else :
            tbadet_rand_digit.append(random.randrange(int(10 ** (tedad_ashar_atti - 1)) , int( 10 ** tedad_ashar_atti ) ))
            cur.execute('''update TBADet set "random digit" = {} where customer = {} ;'''.format( tbadet_rand_digit[i]  , i + 1 ) ) 
            x = tbadet_rand_digit[i]
            for j in range( len(List_of_ATTI_Time_Between_Arrivals) ) :
                if x in range( int(List_of_ATTI_Random_Digit_Lower_Limit[j]) , int(List_of_ATTI_Random_Digit_Upper_Limit[j])  ):
                    y = List_of_ATTI_Time_Between_Arrivals[j]
                
            cur.execute('''update TBADet set "time between arrivals" = {} where customer = {} ;'''.format( y , i + 1 ) )
    
    con.commit()
    con.close() 

def Service_Time_Determination():
    global List_of_STTI_Random_Digit_Lower_Limit 
    global List_of_STTI_Random_Digit_Upper_Limit
    global count_of_entry
    Service_Time_Determination_rand_digit=[]
    con = db.connect(database_path )
    cur = con.cursor()
    for i in range( count_of_entry ) : 
        Service_Time_Determination_rand_digit.append(random.randrange(int(10 ** (tedad_ashar_stti - 1)) , int( 10 ** tedad_ashar_stti ) ))
        cur.execute('''update STDet set "random digit" = {} where customer = {} ;'''.format( Service_Time_Determination_rand_digit[i]  , i + 1 ) ) 
        x = Service_Time_Determination_rand_digit[i]
        for j in range( len(List_of_STTI_Service_Time) ) :
            if x in range( int(List_of_STTI_Random_Digit_Lower_Limit[j]) , int(List_of_STTI_Random_Digit_Upper_Limit[j])  ):
                y = List_of_STTI_Service_Time[j]
            
        cur.execute('''update STDet set "service time" = {} where customer = {} ;'''.format( y , i + 1 ) )
    
    con.commit()
    con.close()

def Single_Server_Queueing_Problem():
    global count_of_entry
    time_since_last_arrival = []
    arrival_time = []
    service_time = []
    time_service_begins = []
    
    con = db.connect(database_path )
    cur = con.cursor()
    
    for i in range( count_of_entry  ) :     
        cur.execute(''' select "time between arrivals" from TBADet ''' )
        time_since_last_arrival = cur.fetchall()
    for i in range( count_of_entry ) : 
        cur.execute('''update STQP set "time since last arrival" = {} where customer = {} ;'''.format( time_since_last_arrival[i][0] , i + 1 ) )
    
    arrival_time.append(0)
    for i in range( 1 , count_of_entry  ) : 
        arrival_time.append( arrival_time[i-1] + time_since_last_arrival[i][0] )
    for i in range( count_of_entry ) : 
        cur.execute('''update STQP set "arrival time" = {} where customer = {} ;'''.format( arrival_time[i] , i + 1 ) )
    
    for i in range( count_of_entry  ) :     
        cur.execute(''' select "service time" from STDet ''' )
        service_time = cur.fetchall()
    for i in range( count_of_entry ) : 
        cur.execute('''update STQP set "service time" = {} where customer = {} ;'''.format( service_time[i][0] , i + 1 ) )
    
    time_service_begins.append(0)
    for i in range( 1 , count_of_entry  ) : 
        if time_service_begins[i-1] + service_time[i-1][0] > arrival_time[i] : 
            time_service_begins.append( time_service_begins[i-1] + service_time[i-1][0]  )
        else : 
            time_service_begins.append( arrival_time[i] )
    for i in range( count_of_entry ) : 
        cur.execute('''update STQP set "time service begins" = {} where customer = {} ;'''.format( time_service_begins[i] , i + 1 ) )
    
    for i in range( count_of_entry ) : 
        cur.execute('''update STQP set "time customer waits in queue" = {} where customer = {} ;'''.format( time_service_begins[i] - arrival_time[i] , i + 1 ) )
    
    for i in range( count_of_entry ) : 
        cur.execute('''update STQP set "time service ends" = {} where customer = {} ;'''.format( time_service_begins[i] + service_time[i][0] , i + 1 ) )
    
    for i in range( count_of_entry ) : 
        if time_service_begins[i] == arrival_time[i] : 
            cur.execute('''update STQP set "time customer spend in system" = {} where customer = {} ;'''.format( service_time[i][0] , i + 1 ) )
        else : 
            cur.execute('''update STQP set "time customer spend in system" = {} where customer = {} ;'''.format( (time_service_begins[i]- arrival_time[i]) + service_time[i][0] , i + 1 ) )
    
    #cur.execute('''update STQP set "idle time" = 0 where customer = 1 ;''')
    cur.execute('''update STQP set "idle time" = 0.0 where customer = 1 ;''')
    for i in range( 1 , count_of_entry ) : 
        cur.execute('''update STQP set "idle time" = {} where customer = {} ;'''.format( time_service_begins[i] - ( time_service_begins[i-1] + service_time[i-1][0] ) , i + 1 ) )
    con.commit()
    con.close()

def Queue_Count_Table():
    global count_of_entry
    x , y , z , k = 0.0 , 0.0 , 0.0 , 0.0
    sum_of_service_time = []
    sum_of_time_customer_waits_in_queue = []
    sum_of_time_customer_spend_in_system = []
    sum_of_idle_time = []
    con = db.connect(database_path )
    cur = con.cursor()
    cur.execute(''' select "service time" from STQP ''' )
    sum_of_service_time = cur.fetchall()
    cur.execute(''' select "time customer waits in queue" from STQP ''' )
    sum_of_time_customer_waits_in_queue = cur.fetchall()
    cur.execute(''' select "time customer spend in system" from STQP ''' )
    sum_of_time_customer_spend_in_system = cur.fetchall()
    cur.execute(''' select "idle time" from STQP ''' )
    sum_of_idle_time = cur.fetchall()
    for i in range( count_of_entry ) :
        x += sum_of_service_time[i][0]
        y += sum_of_time_customer_waits_in_queue[i][0]
        z += sum_of_time_customer_spend_in_system[i][0]
        k += sum_of_idle_time[i][0]
    
    cur.execute('''update "Queue Count" set "sum of service time" = {} ;'''.format( x ) )
    cur.execute('''update "Queue Count" set "sum of time customer waits in queue" = {} ;'''.format( y ) )
    cur.execute('''update "Queue Count" set "sum of time customer spend in system" = {} ;'''.format( z ) )
    cur.execute('''update "Queue Count" set "sum of idle time" = {} ;'''.format( k ) )
    #cur.execute('''update "Queue Count" set "average time between arrivals" = {} ;'''.format( m ) )
    #cur.execute('''update "Queue Count" set "average waiting time in queue" = {} ;'''.format( n ) )
    #cur.execute('''update "Queue Count" set "average time customer spends in system" = {} ;'''.format( o ) )
    con.commit()
    con.close()
#/Processing 

#Importing Data
def Create_Database( e2 ):
    global database_path
    data_base_name = e2.get()
    if not os.path.exists( "Databases" ):
        os.makedirs( "Databases" )
    
    Install_path=os.getcwd()
    con = db.connect(Install_path + "\Databases\\" + data_base_name + '.db' )
    cur = con.cursor()
    cur.execute( '''CREATE TABLE DTBA ( "time between arrivals" double  , probability double ,
                                        "cummulative probability" double , "random digit assignment" text) ; ''' )
    cur.execute('''CREATE TABLE DST ( "service time" double  , probability double , "cummulative probability" double , "random digit assignment" text) ;''')
    cur.execute('''CREATE TABLE TBADet ( customer integer , "random digit" integer , "time between arrivals" double ) ;''')
    cur.execute('''CREATE TABLE STDet ( customer integer , "random digit" text , "service time" double ) ;''')
    cur.execute('''CREATE TABLE STQP ( customer integer  , "time since last arrival" double , "arrival time" double ,
                                        "service time" double , "time service begins" double , "time customer waits in queue" double ,
                                        "time service ends" double ,"time customer spend in system" double , "idle time" double ) ;''')
    cur.execute('''CREATE TABLE "Queue Count" ( "sum of service time" double , "sum of time customer waits in queue" double , "sum of time customer spend in system" double ,
                                                "sum of idle time" double , "average time between arrivals" double , "average waiting time of who those wait" double ,
                                                "average time customer spends in the system" double  );''')
    cur.execute('''CREATE TABLE Statistics ("average waiting time" double , probability double , "probability of idle server" double , "average service time" double) ;''')
    con.commit()
    con.close()
    print("install path : " , type(Install_path) )
    database_path = Install_path + "\Databases\\" + data_base_name + '.db'
    print("installed path : "  , Install_path )
def about_us( Startup_main_window ):
    Startup_main_window.destroy()
    About_us_window = Tk()
    About_us_window.geometry( "%dx%d+%d+%d" % ( 800 , 750 , 300 , 50 ) )
    About_us_window.title("About Us" )
    
    #Create a Main Frame 
    main_frame = Frame( About_us_window )
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
def Arrival_Time_Table_Information():
    global row_count_of_arrival_time_table_information
    global List_of_ATTI_Time_Between_Arrivals 
    global List_of_ATTI_Probability 
    row_count_of_arrival_time_table_information = 0
    
    def import_data_in_atti( e2 , e3 ) :
        global row_count_of_arrival_time_table_information
        global List_of_ATTI_Time_Between_Arrivals 
        global List_of_ATTI_Probability
        List_of_ATTI_Time_Between_Arrivals.append(e2.get())
        List_of_ATTI_Probability.append(e3.get())
        
    def import_data_in_atti_last( e2 , e3 ) :
        global row_count_of_arrival_time_table_information
        global List_of_ATTI_Time_Between_Arrivals 
        global List_of_ATTI_Probability
        List_of_ATTI_Time_Between_Arrivals.append(e2.get())
        List_of_ATTI_Probability.append(e3.get())
        w3.destroy()
        Confirm_Arrival_Time_Table_Information( )
        
    
    def next_import ( w3  , b3 , b4 , e2 , e3  ):
        global row_count_of_arrival_time_table_information
        global List_of_ATTI_Time_Between_Arrivals 
        global List_of_ATTI_Probability
        import_data_in_atti( e2 , e3 )
        next_row( w3  , b3 , b4 , e2 , e3  )
        print("list tba : " , List_of_ATTI_Time_Between_Arrivals )
        print("list p : " , List_of_ATTI_Probability )
        
    def next_row(  w3 , b3 , b4 , e2 , e3  ):
        global row_count_of_arrival_time_table_information
        global List_of_ATTI_Time_Between_Arrivals 
        global List_of_ATTI_Probability
        row_count_of_arrival_time_table_information += 1
        i = 50 + row_count_of_arrival_time_table_information * 50 
        w3.geometry( "%dx%d+%d+%d" % ( 850  , 120 + i , 300 , 50 ) )
        
        lextra = Label( w3 , text="Row {}".format(row_count_of_arrival_time_table_information + 1 ) , justify = LEFT , font="tahoma 10 bold" , fg="black"   )
        lextra.place( x = 10 , y= 10 + i  )
        
        tba = IntVar()
        e2 = Entry( w3 , textvariable= tba , font="tahoma 10 normal"  , fg="black" , width=10 ) 
        e2.place( x = 100 , y = 10 + i  )
        
        p = IntVar()
        e3 = Entry( w3 , textvariable= p , font="tahoma 10 normal"  , fg="black" , width=10 ) 
        e3.place( x = 265 , y = 10 + i)
        
        cp = IntVar()
        e4 = Entry( w3 , textvariable= cp , font="tahoma 10 normal"  , fg="black" , width=10 , state=DISABLED ) 
        e4.place( x = 400 , y = 10  + i)
        
        rda = IntVar()
        e5 = Entry( w3 , textvariable= rda , font="tahoma 10 normal"  , fg="black" , width=10 , state=DISABLED ) 
        e5.place( x = 575 , y = 10 + i )
        
        b4.destroy()
        b4 = Button( w3 , text="Confirm Data" , width=10  , command= lambda : import_data_in_atti_last( e2 , e3 ) )
        b4.place( x = 750 , y = 80 + i )
        
        b3.destroy()
        b3 = Button( w3 , text="+ Add Row" , width=10  , command= lambda : next_import( w3  , b3 , b4 , e2 , e3  ) )
        b3.place( x = 750 , y = 10 + i )
        
        
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
    
    tba = DoubleVar()
    e2 = Entry( w3 , textvariable= tba , font="tahoma 10 normal"  , fg="black" , width=10 )
    e2.place( x = 100 , y = 60 )
    
    p = DoubleVar()
    e3 = Entry( w3 , textvariable= p , font="tahoma 10 normal"  , fg="black" , width=10 )
    e3.place( x = 265 , y = 60 )
    
    cp = DoubleVar()
    e4 = Entry( w3 , textvariable= cp , font="tahoma 10 normal"  , fg="black" , width=10 , state=DISABLED ) 
    e4.place( x = 400 , y = 60 )
    
    
    rda = DoubleVar()
    e5 = Entry( w3 , textvariable= rda , font="tahoma 10 normal"  , fg="black" , width=10 , state=DISABLED ) 
    e5.place( x = 575 , y = 60 )
    
    
    b3 = Button( w3 , text="+ Add Row" , width=10  , command= lambda : next_import(  w3  , b3 , b4 , e2 , e3  ) )
    b3.place( x= 750 , y = 60 )
    
    b4 = Button( w3 , text="Confirm Data" , width=10  , command= lambda : import_data_in_atti_last( e2 , e3 )  )
    b4.place( x= 750 , y = 100 )
    
    w3.mainloop()
def Service_Time_Table_Information():
    global row_count_of_service_time_table_information
    global List_of_STTI_Service_Time 
    global List_of_STTI_Probability 
    row_count_of_service_time_table_information = 0
    
    def import_data_in_atti( e2 , e3 ) :
        global List_of_STTI_Service_Time 
        global List_of_STTI_Probability
        List_of_STTI_Service_Time.append(e2.get())
        List_of_STTI_Probability.append(e3.get())
        
    def import_data_in_atti_last( e2 , e3 ) :
        global List_of_STTI_Service_Time 
        global List_of_STTI_Probability
        List_of_STTI_Service_Time.append(e2.get())
        List_of_STTI_Probability.append(e3.get())
        w4.destroy()
        Confirm_Service_Time_Table_Information( )
        
    
    def next_import ( w4  , b3 , b4 , e2 , e3  ):
        global row_count_of_service_time_table_information 
        global List_of_STTI_Service_Time 
        global List_of_STTI_Probability
        import_data_in_atti( e2 , e3 )
        next_row( w4  , b3 , b4 , e2 , e3  )
        print("list st : " , List_of_STTI_Service_Time )
        print("list pp : " , List_of_STTI_Probability )
        
    def next_row(  w3 , b3 , b4 , e2 , e3  ):
        global List_of_STTI_Service_Time 
        global List_of_STTI_Probability
        global row_count_of_service_time_table_information
        row_count_of_service_time_table_information += 1
        i = 50 + row_count_of_service_time_table_information * 50 
        w3.geometry( "%dx%d+%d+%d" % ( 850  , 120 + i , 300 , 50 ) )
        
        lextra = Label( w4 , text="Row {}".format(row_count_of_service_time_table_information + 1 ) , justify = LEFT , font="tahoma 10 bold" , fg="black"   )
        lextra.place( x = 10 , y= 10 + i  )
        
        tba = IntVar()
        e2 = Entry( w4 , textvariable= tba , font="tahoma 10 normal"  , fg="black" , width=10 ) 
        e2.place( x = 100 , y = 10 + i  )
        
        p = IntVar()
        e3 = Entry( w4 , textvariable= p , font="tahoma 10 normal"  , fg="black" , width=10 ) 
        e3.place( x = 265 , y = 10 + i)
        
        cp = IntVar()
        e4 = Entry( w4 , textvariable= cp , font="tahoma 10 normal"  , fg="black" , width=10 , state=DISABLED ) 
        e4.place( x = 400 , y = 10  + i)
        
        rda = IntVar()
        e5 = Entry( w4 , textvariable= rda , font="tahoma 10 normal"  , fg="black" , width=10 , state=DISABLED ) 
        e5.place( x = 575 , y = 10 + i )
        
        b4.destroy()
        b4 = Button( w4 , text="Confirm Data" , width=10  , command= lambda : import_data_in_atti_last( e2 , e3 ) )
        b4.place( x = 750 , y = 80 + i )
        
        b3.destroy()
        b3 = Button( w4 , text="+ Add Row" , width=10  , command= lambda : next_import( w3  , b3 , b4 , e2 , e3  ) )
        b3.place( x = 750 , y = 10 + i )
        
        
    w4 = Tk()
    w4.geometry( "%dx%d+%d+%d" % ( 850 , 150 , 300 , 50 ) )
    w4.title("Service Time Table Information " )
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
    
    tba = DoubleVar()
    e2 = Entry( w4 , textvariable= tba , font="tahoma 10 normal"  , fg="black" , width=10 )
    e2.place( x = 100 , y = 60 )
    
    p = DoubleVar()
    e3 = Entry( w4 , textvariable= p , font="tahoma 10 normal"  , fg="black" , width=10 )
    e3.place( x = 265 , y = 60 )
    
    cp = DoubleVar()
    e4 = Entry( w4 , textvariable= cp , font="tahoma 10 normal"  , fg="black" , width=10 , state=DISABLED ) 
    e4.place( x = 400 , y = 60 )
    
    
    rda = DoubleVar()
    e5 = Entry( w4 , textvariable= rda , font="tahoma 10 normal"  , fg="black" , width=10 , state=DISABLED ) 
    e5.place( x = 575 , y = 60 )
    
    
    b3 = Button( w4 , text="+ Add Row" , width=10  , command= lambda : next_import(  w4  , b3 , b4 , e2 , e3  ) )
    b3.place( x= 750 , y = 60 )
    
    b4 = Button( w4 , text="Confirm Data" , width=10  , command= lambda : import_data_in_atti_last( e2 , e3 )  )
    b4.place( x= 750 , y = 100 )
    
    w4.mainloop()
def Confirm_Arrival_Time_Table_Information() :
    global row_count_of_arrival_time_table_information
    global List_of_ATTI_Time_Between_Arrivals 
    global List_of_ATTI_Probability 
    con = db.connect(database_path )
    cur = con.cursor()
    for i in range( row_count_of_arrival_time_table_information + 1 ) :
        cur.execute('''insert into DTBA values ({},{},{},"{}") ;'''.format(List_of_ATTI_Time_Between_Arrivals[i] , List_of_ATTI_Probability[i] , 'NULL' , '' ) ) 
    con.commit()
    con.close()
    Arrival_Time_Table_Information_Processing()
def Confirm_Service_Time_Table_Information() :
    global row_count_of_service_time_table_information
    global List_of_STTI_Service_Time 
    global List_of_STTI_Probability
    con = db.connect(database_path )
    cur = con.cursor()
    for i in range( row_count_of_service_time_table_information + 1 ) :
        cur.execute('''insert into DST values ({},{},{},"{}") ;'''.format(List_of_STTI_Service_Time[i] , List_of_STTI_Probability[i] , 'NULL' , 'NULL' ) ) 
    con.commit()
    con.close()
    Service_Time_Table_Information_Processing()
def Confirm_New_Project( New_Project_Window , e1 ) :
    global count_of_entry
    count_of_entry = int( e1.get() )
    if ( count_of_entry == 0  ) : 
        alert_window_of_new_project_window = Tk()
        alert_window_of_new_project_window.geometry( "%dx%d+%d+%d" % ( 400 , 100 , 600 , 300 ) )
        alert_window_of_new_project_window.title("Lack Of Information" )
        alert_window_of_new_project_window.resizable(False,False)
        Lable_of_alert_window_of_new_project_window = Label( alert_window_of_new_project_window , text="Please Enter a Valid Counts of Entry" ,
                                                             font="arial 14 bold" , bg="white" , fg="red" )
        Lable_of_alert_window_of_new_project_window.pack()
        Button_of_alert_window_of_new_project_window = Button( alert_window_of_new_project_window , text="OK" ,
                                                                font="arial 14 bold" , bg="white" , fg="black" , command= lambda : alert_window_of_new_project_window.destroy() )
        Button_of_alert_window_of_new_project_window.pack()
    else : 
        con = db.connect( database_path )
        cur = con.cursor()
        for i in range( count_of_entry ) :
            cur.execute('''insert into TBADet values ({},{},{}) ;'''.format( i + 1 , 'NULL' , 'NULL'  ) )
            cur.execute('''insert into STDet values ({},"{}",{}) ;'''.format( i + 1 , '' , 'NULL'  ) )
            cur.execute('''insert into STQP values ({},{},{},{},{},{},{},{},{}) ;'''.format( i + 1 , 'NULL' , 'NULL' , 'NULL' , 'NULL' , 'NULL' , 'NULL' , 'NULL' , 'NULL'  ) ) 
            cur.execute('''insert into "Queue Count" values ({},{},{},{},{},{},{}) ;'''.format( 'NULL' , 'NULL' , 'NULL' , 'NULL' , 'NULL' , 'NULL' , 'NULL'  ) )
        con.commit()
        con.close()
        Time_Between_Arrivals_Determination_Processing()
        Service_Time_Determination()
        Single_Server_Queueing_Problem()
        Queue_Count_Table()
        New_Project_Window.destroy()
        startup_menu() 
def new_project( Startup_main_window  ): 
    Startup_main_window.destroy()
    New_Project_Window = Tk()
    New_Project_Window.geometry( "%dx%d+%d+%d" % ( 700 , 400 , 450 , 200 ) )
    New_Project_Window.title("Import Data " )
    New_Project_Window.resizable(True,True)

    l1 = Label( New_Project_Window , text="Project Name " , font="tahoma 14 bold" )
    l1.place( x = 10 , y = 10 )
    
    project_name = StringVar()
    e2 = Entry( New_Project_Window , textvariable = project_name , font="tahoma 14 normal"  , fg="black" , width=20 )
    e2.place( x = 150 , y = 10 )
    
    b1 = Button( New_Project_Window , text="Arrival Time Table Information " , width=30  , command=Arrival_Time_Table_Information )
    b1.place( x = 100 , y = 80  )
    
    b2 = Button( New_Project_Window , text="Service Time Table Information " , width=30  , command=Service_Time_Table_Information )
    b2.place( x = 350 , y = 80  )
   
    l2 = Label( New_Project_Window , text="Count of entry : " , font="tahoma 17 bold" )
    l2.place( x = 150 , y = 200 )
    
    packet_number = IntVar()
    e1 = Entry( New_Project_Window , textvariable = packet_number ,  font="tahoma 14 normal "  , bg="white" , fg = "black"  ,width=9  )
    e1.place ( x = 375 , y = 210 )
    
    b4 = Button( New_Project_Window , text="Create DataBase" , font="tahoma 14 bold" , width=15  , command = lambda : Create_Database(e2) )
    b4.place( x = 450 , y = 10 )
    
    
    b3 = Button( New_Project_Window , text="Confirm" , width=30  , command = lambda : Confirm_New_Project( New_Project_Window , e1 ) )
    b3.place( x = 450 , y = 350 )
    
    New_Project_Window.mainloop()
def startup_menu():
    Startup_main_window = Tk()
    Startup_main_window.geometry( "%dx%d+%d+%d" % ( 650 , 650 , 100 , 100 ) )
    Startup_main_window.title("Single Server Simulation" )
    Startup_main_window.resizable(False,False)
    x = Menu(Startup_main_window)
    Startup_main_window.configure(menu=x)
    fv = Menu(x)
    fr = Menu(x) 
    fx = Menu(x)
    x.add_cascade(label="File",menu=fv )
    x.add_cascade(label="Project",menu=fr )
    x.add_cascade(label="About Us ",menu=fx)
    fv.add_command(label="New Project" , command=lambda : new_project( Startup_main_window ) ) 
    fv.add_command(label="Exit" , command=Startup_main_window.destroy )
    fr.add_command(label="Show Tables")
    fr.add_command(label="Show Charts")
    fr.add_command(label="Show Statistics")
    fx.add_command(label="About Us",command=lambda : about_us( Startup_main_window ) )
    Startup_main_window.mainloop()
startup_menu()
