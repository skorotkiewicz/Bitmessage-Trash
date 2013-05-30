#!/usr/bin/env python2

import sqlite3
import gtk
import gtk.glade
import pygtk


pygtk.require("2.0")

class messages:

    def __init__(self):

        # Database
        self.engine = sqlite3.connect('messages.db')

        # Load gui window from glade XML
        self.wTree = gtk.glade.XML ('guiContact.glade', 'window1')

        # gui element(s): label(s)
        self.lblMode      = self.wTree.get_widget("lblMode")

        # gui element(s): input(s)
        self.fields = ('rowid', 'subject')
        for field in self.fields:
            setattr(self, field, self.wTree.get_widget(field))

        # gui element(s): list(s)
        self.list  = self.wTree.get_widget("treeview1")

        # gui liststore for treeview
        self.dataList = gtk.ListStore(str, str)
        self.list.set_model(self.dataList)


        # gui treeview columns
        counter = 0
        self.columns = ('Id', 'Subject')
        for col in self.columns:
            self.addlistcolumn(col, counter)
            counter += 1

        # Load list data
        self.load_list()

        # gui element signals
        dic = { 
                "on_delete_button_clicked": self.on_delete_button_clicked,\
                "read_message_button": self.read_message_button,\
                "on_exit": self.on_exit}

        self.wTree.signal_autoconnect (dic)

    # on click button: delete
    def on_delete_button_clicked(self, widget):

        # Yes/No Dialog
        message = "Delete message?"
        dialog = gtk.MessageDialog(None, gtk.DIALOG_MODAL, gtk.MESSAGE_QUESTION, gtk.BUTTONS_YES_NO, message)
        dialog.set_position(gtk.WIN_POS_CENTER)
        response = dialog.run()
        dialog.destroy()

        if response == gtk.RESPONSE_YES:
            # get selection
            selection = self.list.get_selection()
            result = selection.get_selected()

            if result:
               # get GtkListStore(model) and GtkTreeIter(iter) from object result
               model, iter = result
               # get name
               messageid = model.get_value(iter, 0)

            # delete row
            model.remove(iter)

            # delete from databse table
            query = 'DELETE FROM inbox WHERE rowid = "{0}"'\
                .format(messageid)
            self.engine.execute(query)
            self.engine.commit()


    #load list from databse
    def load_list(self):
        result = self.engine.execute('SELECT rowid,subject FROM inbox WHERE folder = "trash"')
        for row in result:
            self.dataList.append((row[0], row[1]))

    # add column to treeview
    def addlistcolumn(self, title, columnId):
        column = gtk.TreeViewColumn(title, gtk.CellRendererText(), text=columnId)
        column.set_resizable(True)
        column.set_sort_column_id(columnId)
        self.list.append_column(column)

    def read_message_button(self, widget):
        selection = self.list.get_selection()
        resultID = selection.get_selected()
        model, iter = resultID
        messageid = model.get_value(iter, 0)

        query = 'SELECT rowid,subject,message FROM inbox WHERE rowid = "{0}"'\
                .format(messageid)
        result = self.engine.execute(query)
        for row in result:
            title = row[1]+"\n"
            message = title+row[2]

        md = gtk.MessageDialog(None, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_INFO, gtk.BUTTONS_CLOSE, message)
        md.run()
        md.destroy()

    def on_exit(self, widget):
        gtk.main_quit()

app = messages()
gtk.mainloop()
