#!/usr/bin/env python
# -*-coding:utf-8-*

import pygtk
pygtk.require("2.0")
import os, gtk
from os import chdir
from lxml import etree

EMPLACEMENT = "/usr/local/bin/handy-menu/themes/"
options = {}
tree = etree.parse('/usr/local/bin/handy-menu/handy-menu.glade')

class HandyConfGui():
	
	def Quitter(self, widget):
		gtk.main_quit()
		
	def liste_bannieres_dispo(self, liste_banniere):
		'''forme la liste deroulante par rapport aux bannieres dispo'''
		bannieres_dispo= [nom for nom  in os.listdir(EMPLACEMENT + "bannieres/") if os.path.isfile(EMPLACEMENT + "bannieres/" + nom) == True]
		for banniere in bannieres_dispo:
			liste_banniere.append_text(banniere)
			
	def banniere_choix(self, liste_banniere):
		'''fonction appelée au choix de la banniere dans la liste deroulante''' 
		choix = liste_banniere.get_active_text() #recuperation du choix
		if (choix == "Bannières"):
			pass 
		else:
			tree.find('//object[@id="banner"]/property[@name="pixbuf"]').text = EMPLACEMENT + 'bannieres/' + choix
			tree.write('/usr/local/bin/handy-menu/handy-menu.glade')
			
	def liste_icones_dispo(self, liste_icones):
		icones_dispo = [nom for nom  in os.listdir(EMPLACEMENT + "icons/") if os.path.isdir(EMPLACEMENT + "icons/" + nom) == True]
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
				icone.text = EMPLACEMENT + "icons/" + choix + '/' + os.path.basename(icone.text)
				tree.write('/usr/local/bin/handy-menu/handy-menu.glade')
			
	def update_handymenu(self, widget):
		try:
			os.system('killall handymenu.py  && handymenu.sh &')
			
		except OSError:
			pass 
			
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
							
		
								
	def __init__(self):
		
		maFenetre = gtk.Window()
		maFenetre.set_title("options")
		maFenetre.connect("destroy", self.Quitter)
		#maFenetre.set_default_size(300, 250)
		
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
		
		liste_banniere = gtk.combo_box_new_text()
		liste_banniere.append_text("Bannières")
		liste_banniere.set_wrap_width(0)
		liste_banniere.set_active(0)
		self.liste_bannieres_dispo(liste_banniere)
		liste_banniere.connect('changed', self.banniere_choix)
		
		liste_icones = gtk.combo_box_new_text()
		liste_icones.append_text("Pack Icônes")
		liste_icones.set_active(0)
		self.liste_icones_dispo(liste_icones)
		liste_icones.connect('changed', self.icones_choix)
		
		
		listevbox.add(liste_banniere)
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
		maFenetre.add(mainvbox)
		maFenetre.show_all()
		
if __name__ == "__main__":
	
	 HandyConfGui()
	 gtk.main()	
		
		
