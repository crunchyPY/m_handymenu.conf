#!/usr/bin/python
# -*-coding:utf-8-*
#######################
# handy linux main menu
# by manon, Meier & arpinux
########################################################################

import pygtk
pygtk.require("2.0")
import gtk
import os
import threading, gobject
from lxml import etree

gobject.threads_init()
EMPLACEMENT_ICONS = "/usr/local/bin/handy-menu/themes/icons/"
EMPLACEMENT_BANNIERES = "/usr/local/bin/handy-menu/themes/banniere/"
tree = etree.parse('/usr/local/bin/handy-menu/handy-menu.glade')
options = {}	

########################################################################
# main window
########################################################################
class HandyMenu():
    def __init__(self):
		
		interface = gtk.Builder()
		interface.add_from_file("/usr/local/bin/handy-menu/handy-menu.glade")	
		interface.connect_signals(self)
  
    def on_mainWindow_destroy(self, widget, event):
	    gtk.main_quit()
	    
########################################################################
# files tab
########################################################################
    def on_mes_images_clicked(self, widget):
        os.system("exo-open --launch FileManager $HOME/Images &")
	self.quitter(self)
    
    def on_mes_documents_clicked(self, widget):
        os.system("exo-open --launch FileManager $HOME/Documents &")
	self.quitter(self)

    def on_mes_telechargements_clicked(self, widget):
        os.system("exo-open --launch FileManager $HOME/Téléchargements &")
        self.quitter(self)

    def on_dossier_personnel_clicked(self, widget):
        os.system("exo-open --launch FileManager $HOME &")
        self.quitter(self)
       

    def on_ma_musique_clicked(self, widget):
        os.system("exo-open --launch FileManager $HOME/Musique &")
        self.quitter(self)

    def on_vider_corbeille_clicked(self, widget):
        os.system("exo-open --launch FileManager trash:/// &")
        self.quitter(self)

    def on_mes_videos_clicked(self, widget):
        os.system("exo-open --launch FileManager $HOME/Vidéos &")
        self.quitter(self)

    def on_aide_fichiers_clicked(self, widget):
        os.system("exo-open --launch WebBrowser http://handylinux.org/documentation/doku.php/fichiers &")
        self.quitter(self)
########################################################################
# web tab
########################################################################
    def on_webbrowser_clicked(self, widget):
        os.system("exo-open --launch WebBrowser &")
        self.quitter(self)

    def on_icedove_clicked(self, widget):
        os.system("exo-open --launch MailReader &")
        self.quitter(self)

    def on_skype_clicked(self, widget):
        os.system("skype &")
        self.quitter(self)

    def on_minitube_clicked(self, widget):
        os.system("minitube &")
        self.quitter(self)

    def on_facebook_clicked(self, widget):
        os.system("exo-open --launch WebBrowser https://fr-fr.facebook.com/ &")
        self.quitter(self)

    def on_aide_internet_clicked(self, widget):
        os.system("exo-open --launch WebBrowser http://handylinux.org/documentation/doku.php/internet &")
        self.quitter(self)
########################################################################
# media tab
########################################################################
    def on_vlc_clicked(self, widget):
        os.system("vlc &")
        self.quitter(self)

    def on_ristretto_clicked(self, widget):
        os.system("shotwell &")
        self.quitter(self)

    def on_quodlibet_clicked(self, widget):
        os.system("quodlibet &")
        self.quitter(self)

    def on_xfburn_clicked(self, widget):
        os.system("xfburn &")
        self.quitter(self)

    def on_mixer_clicked(self, widget):
        os.system("xfce4-mixer &")
        self.quitter(self)

    def on_aide_media_clicked(self, widget):
        os.system("exo-open --launch WebBrowser http://handylinux.org/documentation/doku.php/multimedia &")
        self.quitter(self)
########################################################################
# office tab
########################################################################
    def on_mousepad_clicked(self, widget):
        os.system("leafpad &")
        self.quitter(self)

    def on_xpad_clicked(self, widget):
        os.system("xpad &")
        self.quitter(self)

    def on_libreoffice_clicked(self, widget):
        os.system("libreoffice &")
        self.quitter(self)

    def on_xcalc_clicked(self, widget):
        os.system("gcalctool &")
        self.quitter(self)

    def on_xsane_clicked(self, widget):
        os.system("simple-scan &")
        self.quitter(self)

    def on_aide_office_clicked(self, widget):
        os.system("exo-open --launch WebBrowser http://handylinux.org/documentation/doku.php/bureautique &")
        self.quitter(self)
########################################################################
# game tab
########################################################################
    def on_sudoku_clicked(self, widget):
        os.system("gnome-sudoku &")
        self.quitter(self)

    def on_cards_clicked(self, widget):
        os.system("sol &")
        self.quitter(self)

    def on_boards_clicked(self, widget):
        os.system("mahjongg &")
        self.quitter(self)

    def on_gbrainy_clicked(self, widget):
        os.system("gbrainy &")
        self.quitter(self)
########################################################################
# dev tab
########################################################################
    def on_terminal_clicked(self, widget):
        os.system("cd ~ && exo-open --launch TerminalEmulator &")
        self.quitter(self)

    def on_synaptic_clicked(self, widget):
        os.system("software-center &")
        self.quitter(self)

    def on_appslist_clicked(self, widget):
        os.system("xfce4-appfinder &")
        self.quitter(self)

    def on_network_clicked(self, widget):
        os.system("nm-connection-editor &")
        self.quitter(self)

    def on_dev_print_clicked(self, widget):
        os.system("xfprint-settings && x-www-browser http://localhost:631/admin && xfprint4-manager &")
        self.quitter(self)

    def on_dev_config_clicked(self, widget):
        os.system("xfce4-settings-manager &")
        self.quitter(self)
########################################################################
# action
########################################################################

    def on_preferences_clicked(self, widget):
        self.config = ConfHandyMenu(self)
        self.config.start()
        return

    def on_aide_clicked(self, widget):
        os.system("exo-open --launch WebBrowser http://handylinux.org/documentation &")
        self.quitter(self)
        
    def on_check_clicked(self, widget):
		tree = etree.parse('handy-menu.glade')
		if widget.get_active():
			tree.find('//object[@class="GtkCheckButton"]/property[@name="active"]').text = "True"
		else:
			tree.find('//object[@class="GtkCheckButton"]/property[@name="active"]').text = "False"
		tree.write('handy-menu.glade')
			
    def quitter(self, widget):
	    tree = etree.parse('handy-menu.glade')
	    if tree.find('//object[@class="GtkCheckButton"]/property[@name="active"]').text == "True":
			gtk.main_quit()
			
########################################################################
# config
########################################################################			
class ConfHandyMenu(threading.Thread):
	
	def __init__ (self, widget):
		threading.Thread.__init__ (self, target=self)
		
	def Quitter(self,widget):
		self.maFenetre.destroy()
		
	def liste_bannieres_dispo(self, liste_banniere):
		'''forme la liste deroulante par rapport aux bannieres dispo'''
		bannieres_dispo= [nom for nom  in os.listdir(EMPLACEMENT_BANNIERES) if os.path.isfile(EMPLACEMENT_BANNIERES + nom) == True]
		for banniere in bannieres_dispo:
			self.liste_banniere.append_text(banniere)
			
	def banniere_choix(self, liste_banniere):
		'''fonction appelée au choix de la banniere dans la liste deroulante''' 
		choix = self.liste_banniere.get_active_text() #recuperation du choix
		if (choix == "Bannières"):
			pass 
		else:
			tree.find('//object[@id="banner"]/property[@name="pixbuf"]').text = EMPLACEMENT_BANNIERES + choix
			tree.write('/usr/local/bin/handy-menu/handy-menu.glade')
			
	def liste_icones_dispo(self, liste_icones):
		icones_dispo = [nom for nom  in os.listdir(EMPLACEMENT_ICONS) if os.path.isdir(EMPLACEMENT_ICONS + nom) == True]
		for icone in icones_dispo:
			liste_icones.append_text(icone)
			
	def icones_choix(self, liste_icones):
		tree.find('//object[@id="banner"]/property[@name="pixbuf"]').text = '/usr/local/bin/handy-menu/icons/handymenu_banner.png'
		tree.write('/usr/local/bin/handy-menu/handy-menu.glade')
		
		choix = liste_icones.get_active_text()
		if(choix == "Pack Icônes"):
			pass
		else:
			icones = tree.xpath('//object[@class="GtkImage"]/property[@name="pixbuf"]')
			for icone in icones:
				icone.text = EMPLACEMENT_ICONS + choix + '/' + os.path.basename(icone.text)
				tree.write('/usr/local/bin/handy-menu/handy-menu.glade')
			
	def update_handymenu(self, widget):
		os.system('handymenu.sh &')
		
	def analyse_config(self, widget, checkOption1, checkOption2):
		'''analyse la configuration pour avoir les bonnes valeur sur les boutons'''
		options['resizable'] = tree.find('//object[@class="GtkWindow"]/property[@name="resizable"]').text
		options['window_position'] = tree.find('//object[@class="GtkWindow"]/property[@name="window_position"]').text
		for cle, valeur in options.items():
			if 'resizable' in cle:
				if options['resizable'] == 'True':
					checkOption1.set_active(True)
				else:
					checkOption1.set_active(False)
			if 'window_position' in cle:	
				if options['window_position'] == 'center':
					checkOption2.set_active(False)
				else:
					checkOption2.set_active(True)
					
	def on_redimensionnement(self, widget):
		'''active ou desactive le redimensionnement'''
		if widget.get_active():
			tree.find('//object[@class="GtkWindow"]/property[@name="resizable"]').text = "True"
		else:
			tree.find('//object[@class="GtkWindow"]/property[@name="resizable"]').text = "False"
		tree.write('/usr/local/bin/handy-menu/handy-menu.glade')
	
	def position_ouverture(self, widget):
		'''active ou desactive l'ouverture du menu au niveau du lanceur'''
		if widget.get_active():
			tree.find('//object[@class="GtkWindow"]/property[@name="window_position"]').text = "mouse"
		else:
			tree.find('//object[@class="GtkWindow"]/property[@name="window_position"]').text = "center"
		tree.write('/usr/local/bin/handy-menu/handy-menu.glade')	
	def run(self):
		self.maFenetre = gtk.Window()
		self.maFenetre.set_title("options")
		self.maFenetre.connect("destroy", self.Quitter)
		self.maFenetre.set_modal(True)
		separateur = gtk.HSeparator()
		separateur.set_size_request(150, 10)
		
		separateur2 = gtk.HSeparator()
		separateur2.set_size_request(150, 10)
		
		separateur3 = gtk.HSeparator()
		separateur3.set_size_request(150, 10)
		
		fram1 = gtk.AspectFrame(label="Options", xalign=0.5, yalign=0.4, ratio=1.0, obey_child=True)
		fram1.set_shadow_type(gtk.SHADOW_OUT)
		
		boutonvBox = gtk.VBox()
		checkOption1 = gtk.CheckButton('Permettre le redimensionnement de la fenetre')
		checkOption2 = gtk.CheckButton('Ouvrir Handy-menu au niveau du lanceur')
		checkOption1.connect("clicked", self.on_redimensionnement)
		checkOption2.connect("clicked", self.position_ouverture)
		self.analyse_config(self, checkOption1, checkOption2)
			
		boutonvBox.add(checkOption1)
		boutonvBox.add(checkOption2)
		fram1.add(boutonvBox)
		
		fram2 = gtk.Frame("Apparence")
		fram2.set_shadow_type(gtk.SHADOW_OUT)
		listevbox = gtk.VBox()
		
		self.liste_banniere = gtk.combo_box_new_text()
		self.liste_banniere.append_text("Bannières")
		self.liste_banniere.set_wrap_width(0)
		self.liste_banniere.set_active(0)
		self.liste_bannieres_dispo(self.liste_banniere)
		self.liste_banniere.connect('changed', self.banniere_choix)
		
		liste_icones = gtk.combo_box_new_text()
		liste_icones.append_text("Pack Icônes")
		liste_icones.set_active(0)
		self.liste_icones_dispo(liste_icones)
		liste_icones.connect('changed', self.icones_choix)
		
		
		listevbox.add(self.liste_banniere)
		listevbox.add(liste_icones)
		fram2.add(listevbox)
		
		boutonActualiser = gtk.ToggleButton(label = "Actualiser HandyMenu")
		boutonActualiser.connect("clicked" ,self.update_handymenu)
		
		boutonQuitter = gtk.ToggleButton(label = "Quitter")
		boutonQuitter.connect("clicked" ,self.Quitter)
		
		
		mainvbox = gtk.VBox()
		mainvbox.add(separateur)
		mainvbox.add(fram1)
		mainvbox.add(separateur2)
		mainvbox.add(fram2)
		mainvbox.add(separateur3)
		mainvbox.add(boutonActualiser)
		mainvbox.add(boutonQuitter)
		self.maFenetre.add(mainvbox)
		self.maFenetre.show_all()
		
		
							
########################################################################
if __name__ == "__main__":

	HandyMenu()
	gtk.main()
