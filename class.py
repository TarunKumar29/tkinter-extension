from tkinter import *




# Tables

class PlainTable(Frame) :

    def del_row(self, n) :
        if n < 0 : raise ValueError(f"error : n = {n}, it should be >= 0")
        if n >= self.rows : raise ValueError(f"error : n = {n}, it should be < {self.rows}")

        #retrieve data
     
        data = list()
        for c in range(self.columns) :
            a = list()
            for r in range(self.rows) :
                if r == n : continue
                val = self.get_val('c', c, r)
                a.append(val)
                del val
            data.append(a)
            del a 

        #destroy the widgets in the table
        for c in range(self.columns) :
            for r in range(self.rows) :
                exec(f"self.c_{c}_{r}.destroy()")

        self.rows-=1
        #Make a new table
        for c in range(self.columns) :
            for r in range(self.rows) :
                exec("self.c_"+str(c)+'_'+str(r)+f" = Label(self, bd = self.border, relief = RAISED, font = self.font, text = data[{c}][{r}])")
                exec("self.c_"+str(c)+'_'+str(r)+".grid(column = "+str(c)+', row = '+str(r+1)+", sticky = \'nsew\')")
        

    
    def del_column(self, n) :
        if n < 0 : raise ValueError(f"error : n = {n}, it should be >= 0")
        if n >= self.columns : raise ValueError(f"error : n = {n}, it should be < {self.columns}")

        #retrieve data
        bla = True
        h_data = list()
        for i in range(len(self.heading)) :
            if i == n : continue
            val = self.get_val(type = 'h', n = i)
            h_data.append(val)
            bla = False
        if not bla : del val
        self.heading.remove(self.heading[n])
        data = list()
        for c in range(self.columns) :
            if c != n :
                a = list()
                for r in range(self.rows) :
                    val = self.get_val('c', c, r)
                    a.append(val)
                    del val
                data.append(a)
                del a 

        #destroy the widgets in the table
        for i in range(len(self.heading)+1) :
            exec(f"self.h{i}.destroy()")
        for c in range(self.columns) :
            for r in range(self.rows) :
                exec(f"self.c_{c}_{r}.destroy()")

        self.columns-=1
        #Make a new table

        for i in range(len(self.heading)) :
            exec("self.h"+str(i)+'='+"Label(self, text = h_data[i], bd = self.border, font = self.h_font, relief = RAISED)")
            exec("self.h"+str(i)+'.grid(column = '+str(i)+", row = 0, sticky = \"nsew\")")
        for c in range(self.columns) :
            for r in range(self.rows) :
                exec("self.c_"+str(c)+'_'+str(r)+f" = Label(self, bd = self.border, relief = RAISED, font = self.font, text = data[{c}][{r}])")
                exec("self.c_"+str(c)+'_'+str(r)+".grid(column = "+str(c)+', row = '+str(r+1)+", sticky = \'nsew\')")
        if self.columns == 0 : self.destroy()



    def get_val( self, type = 'c', column = 0, row = 0, n = 0) :
        if type == 'h' :
            if n < 0 : raise ValueError(f"error : n = {n}, it should be >= 0")
            if n >= len(self.heading) : raise ValueError(f"error : n >= {n}, it should be < {len(self.heading)}")
            
            exec(f"self.val = self.h{n}[\'text\']")
            return self.val
        elif type == "c" :
            
            if column >= self.columns : raise ValueError(f"error : columnumn = {column}, it should be < {self.columns}")#column = self.columns-1
            if row >= self.rows : raise ValueError(f"error : row = {row}, should be < {self.rows} ")#row = self.rows
            if row < 0 : raise ValueError(f"error : row = {row}, should be >= {0} ")#row = 1
            if column < 0 : raise ValueError(f"error : column = {column}, should be >= {0} ")#column = 0
            
            exec(f"self.val = self.c_{column}_{row}[\'text\']")
            return self.val

    def set_val( self,value, row = 0, column = 0, n = 0, type = "c") :
        if type == "h" :
            if n >= len(self.heading) : raise ValueError(f"error : n >= {n}, it should be < {len(self.heading)}")#n = len(self.heading)-1
            if n < 0 : n = 0
            exec("self.h"+str(n)+"[\'text\'] = "+ '\'' +str(value)+'\'')
        else :
            if column >= self.columns : raise ValueError(f"error : columnumn = {column}, it should be < {self.columns}")#column = self.columns-1
            if row > self.rows : raise ValueError(f"error : row = {row}, should be < {self.rows} ")#row = self.rows
            if row < 0 : raise ValueError(f"error : row = {row}, should be >= {0} ")#row = 1
            if column < 0 : raise ValueError(f"error : column = {column}, should be >= {0} ")#column = 0

            exec("self.c_"+str(column)+'_'+str(row)+"[\'text\'] = "+'\''+ str(value)+'\'')
    
    def __init__(self, parent, border = 2, common_text = "", columns = 1, rows = 1, heading = list(), font = ("Courier", '15'), h_font = ("Courier", '20'), *args, **kwargs) :
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.heading = heading
        self.rows = rows
        self.border = border
        self.columns = columns
        self.common_text = common_text
        self.font = font
        self.h_font = h_font

        if self.rows == 0 : self.rows = 1
        if self.columns == 0 : self.columns = 1 

        if len(self.heading) != 0 : 
            i = 0
            for text in self.heading :
                exec("self.h"+str(i)+'='+"Label(self, text = text, bd = self.border, font = self.h_font, relief = RAISED)")
                exec("self.h"+str(i)+'.grid(column = '+str(i)+", row = 0, sticky = \"nsew\")")
                i+=1

        for c in range(self.columns) :
           
            for ro in range(self.rows) :
                r = ro+1
                exec("self.c_"+str(c)+'_'+str(ro)+" = Label(self, bd = self.border, relief = RAISED, font = self.font, text = self.common_text)")
                exec("self.c_"+str(c)+'_'+str(ro)+".grid(column = "+str(c)+', row = '+str(r)+", sticky = \'nsew\')")
