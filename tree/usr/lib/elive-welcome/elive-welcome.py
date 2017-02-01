#!/usr/bin/python3

import os
import gettext
import signal

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from gi.repository.GdkPixbuf import Pixbuf

# NORUN_FLAG = os.path.expanduser("~/.config/elive-welcome/norun.flag")

# i18n
gettext.install("elive-welcome", "/usr/share/locale")

signal.signal(signal.SIGINT, signal.SIG_DFL)


class EliveWelcome():

    def __init__(self):
        window = Gtk.Window()
        window.set_title(_("Welcome Screen"))
        window.set_icon_from_file("/usr/share/elive-welcome/icons/logo.png")
        window.set_position(Gtk.WindowPosition.CENTER)
        window.connect("destroy", Gtk.main_quit)

# FIXME: the "dict" part throws an error, so I have hardcoded it until there's a python magician around that can make it working :)
# Note: we also don't have / use this file, but we need it in a dynamic way so we should use /etc/elive-version instead
        # with open("/etc/linuxmint/info") as f:
            # config = dict([line.strip().split("=") for line in f])

        codename = "Elive"
        # edition = "editiion"
        release = ""
        desktop = "Enlightenment"
        self.release_notes = "http://www.elivecd.org/news/"
        self.user_guide = "http://www.elivecd.org/faq/"
        self.new_features = "http://www.elivecd.org/"

        # distro-specific
        self.dist_name = "Elive"


        bgcolor = Gdk.RGBA()
        bgcolor.parse("rgba(0,0,0,0)")
        fgcolor = Gdk.RGBA()
        fgcolor.parse("#3e3e3e")

        main_box = Gtk.VBox()

        event_box = Gtk.EventBox()
        event_box.set_name("event_box")
        event_box.override_background_color(Gtk.StateType.NORMAL, bgcolor)
        event_box.override_color(Gtk.StateType.NORMAL, fgcolor)
        main_box.pack_start(event_box, True, True, 0)

        vbox = Gtk.VBox()
        vbox.set_border_width(12)
        vbox.set_spacing(0)
        event_box.add(vbox)

        headerbox = Gtk.VBox()
        logo = Gtk.Image()

        logo.set_from_file("/usr/share/elive-welcome/icons/logo.png")

        headerbox.pack_start(logo, False, False, 0)
        # label = Gtk.Label()

        # label.set_markup("<span font='12.5' fgcolor='#3e3e3e'>%s %s '<span fgcolor='#709937'>%s</span>'</span>" % (self.dist_name, release, codename))

        # headerbox.pack_start(label, False, False, 0)
        label = Gtk.Label()
        # label.set_markup("<span font='8' fgcolor='#3e3e3e'><i>%s</i></span>" % edition)
        headerbox.pack_start(label, False, False, 2)
        vbox.pack_start(headerbox, False, False, 10)

        welcome_label = Gtk.Label()
        welcome_message = _("Welcome and thank you for choosing Elive. We hope you'll enjoy using it as much as we did designing it. This operating system aims to be simple and intuitive but it hides thousands of features and secrets. The links below will help you to get started with your new operating system. Now it's time to fly!")
        welcome_label.set_markup("<span font='9' fgcolor='#3e3e3e'>%s</span>" % welcome_message)
        welcome_label.set_line_wrap(True)
        vbox.pack_start(welcome_label, False, False, 10)

        separator = Gtk.Image()
        separator.set_from_file('/usr/share/elive-welcome/icons/separator.png')
        vbox.pack_start(separator, False, False, 10)

        liststore = Gtk.ListStore(Pixbuf, str, str, str, Pixbuf, Pixbuf)
        self.iconview = Gtk.IconView.new()
        self.iconview.add_events(Gdk.EventMask.POINTER_MOTION_MASK)
        self.iconview.connect("item-activated", self.item_activated)
        self.iconview.connect("motion-notify-event", self.on_pointer_motion)
        self.iconview.connect("button-press-event", self.on_mouse_click)
        self.iconview.set_model(liststore)
        self.iconview.set_pixbuf_column(0)
        self.iconview.set_text_column(2)
        self.iconview.set_tooltip_column(3)
        self.iconview.set_columns(6)
        # self.iconview.set_columns(5)
        self.iconview.set_margin(0)
        self.iconview.set_spacing(6)
        self.iconview.set_item_padding(3)
        self.iconview.set_row_spacing(20)
        self.iconview.set_column_spacing(20)
        self.iconview.override_background_color(Gtk.StateType.NORMAL, bgcolor)
        self.iconview.override_color(Gtk.StateType.NORMAL, fgcolor)
        #self.iconview.connect("selection-changed", self.item_activated)
        hbox = Gtk.HBox()
        hbox.pack_start(self.iconview, True, True, 30)
        vbox.pack_start(hbox, False, False, 10)

        actions = []


        self.last_selected_path = None

        # TODO / wishes:
        # release notes
        # user guide
        # hotkeys
        # elive tips to best uses / fast usage
        # contact?
        # FAQ
        # launcher (alt + esc), users needs to know about this feature (and others, hum...)
        #
        # share elive / tweet about it / facebook likes, etc
        # learn: make emodules, theme elive, etc...
        #
        # penguins!
        # compiz!
        # hardware health checker (write a small tool to tutorial and run to the user?)
        # windows applications (photoshop, others), maybe a simple howto explaining how they can be run
        # xbmc ? FIXME WARNING: can be unstable? mmh... try in real live

        # actions.append(['new_features', _("New features"), _("See what is new in this release")])
        actions.append(['new_features', _("Install Elive"), _("Launch the Elive Installer and start enjoying for real this amazing system")])

        # actions.append(['software', _("Apps"), _("Install additional software")])

        # actions.append(['driver', _("Drivers"), _("Install hardware drivers")])
        actions.append(['translate', _("Translate Elive"), _("Help us to translate Elive to your language or also to improve the english sentences")])

        actions.append(['chatroom', _("Chat"), _("Chat live with other users in the chat room")])
        actions.append(['forums', _("Forums"), _("Seek help from other users in the Elive forums")])
        actions.append(['issues', _("Issues"), _("Report an issue so we can solve it")])
        actions.append(['subscribe', _("Be Notified"), _("Be notified about Elive releases or other topics")])
        actions.append(['donors', _("Donate"), _("Make a donation to the Elive project")])
        actions.append(['get_involved', _("Getting involved"), _("Find out how to get involved in the Elive project")])
        # actions.append(['user_guide', _("Documentation"), _("Learn all the basics to get started with Elive")])

        # actions.append(['release_notes', _("Release notes"), _("Read the release notes")])


        # actions.append(['driver', _("Drivers"), _("Install hardware drivers")])
        # actions.append(['codecs', _("Media Center"), _("Run an amazing media center to play movies, music, or a lot of other things")])
        # actions.append(['office', _("Office"), _("Launch the office suite")])
        actions.append(['penguins', _("Penguins"), _("Look at those penguins!")])
        actions.append(['compiz', _("Compiz"), _("Do you want to try a Compiz experience?")])
        actions.append(['help_compiz', _("Fix Compiz"), _("Help us to fix a bug on it so we can include it on the stable version of Elive")])
        actions.append(['help_wikipedia', _("Improve Wikipedia"), _("Help us to have our Elive entry in the Wikipedia")])


        for action in actions:
            desat_pixbuf = Pixbuf.new_from_file('/usr/share/elive-welcome/icons/desat/%s.png' % action[0])
            color_pixbuf = Pixbuf.new_from_file('/usr/share/elive-welcome/icons/color/%s.png' % action[0])
            pixbuf = desat_pixbuf
            liststore.append([pixbuf, action[0], action[1], action[2], desat_pixbuf, color_pixbuf])

# Disabled checkbox for launch at every start, so we want this only in live mode and so its useless
        # hbox = Gtk.HBox()
        # hbox.set_border_width(6)
        # main_box.pack_end(hbox, False, False, 0)
        # checkbox = Gtk.CheckButton()
        # checkbox.set_label(_("Show this dialog at startup"))

        # if not os.path.exists(NORUN_FLAG):
            # checkbox.set_active(True)

        # checkbox.connect("toggled", self.on_button_toggled)
        # hbox.pack_end(checkbox, False, False, 2)

        window.add(main_box)
        window.set_default_size(540, 420)

        css_provider = Gtk.CssProvider()
        css = """
 #event_box {
      background-image: -gtk-gradient (linear,
                                       left top,
       left bottom,
       from (#d6d6d6),
       color-stop (0.5, #efefef),
       to (#d6d6d6));
    }
"""

        css_provider.load_from_data(css.encode('UTF-8'))
        screen = Gdk.Screen.get_default()
        style_context = window.get_style_context()
        style_context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        window.show_all()

    def on_pointer_motion(self, widget, event):
        path = self.iconview.get_path_at_pos(event.x, event.y)
        if path != None:
            if path == self.last_selected_path:
                return
            self.unhighlight_icon(widget)
            treeiter = widget.get_model().get_iter(path)
            widget.get_model().set_value(treeiter, 0, widget.get_model().get_value(treeiter, 5))
            self.last_selected_path = path
        #If we're outside of an item, deselect all items (turn off highlighting)
        if path == None:
            self.unhighlight_icon(widget)
            self.iconview.unselect_all()

    def unhighlight_icon(self, widget):
        if self.last_selected_path != None:
            treeiter = widget.get_model().get_iter(self.last_selected_path)
            widget.get_model().set_value(treeiter, 0, widget.get_model().get_value(treeiter, 4))
            self.last_selected_path = None

    # def on_button_toggled(self, button):
        # if button.get_active():
            # if os.path.exists(NORUN_FLAG):
                # os.system("rm -rf %s" % NORUN_FLAG)
        # else:
            # os.system("mkdir -p ~/.config/elive-welcome")
            # os.system("touch %s" % NORUN_FLAG)

    def on_mouse_click(self, widget, event):
        if event.type == Gdk.EventType.BUTTON_PRESS:
            path = self.iconview.get_path_at_pos(event.x, event.y)
            #if left click, activate the item to execute
            if event.button == 1 and path != None:
                self.item_activated(widget, path)

    def item_activated(self, view, path):
        treeiter = view.get_model().get_iter(path)
        value = view.get_model().get_value(treeiter, 1)

        if value == "chatroom":
            os.system("xchat &")
        # elif value == "restore_data":
            # if os.path.exists("/usr/bin/mintbackup"):
                # os.system("/usr/bin/mintbackup &")
        # elif value == "new_features":
            # os.system("xdg-open %s &" % self.new_features)
        # NOTE: we use new_features instead of installer_run because it has already a nice icon, so we can change the icon name from this ID
        elif value == "new_features":
            os.system("sudo eliveinstaller &")
        elif value == "translate":
            os.system("eltrans &")
        # elif value == "release_notes":
            # os.system("xdg-open %s &" % self.release_notes)
        elif value == "issues":
            os.system("xdg-open http://bugs.elivecd.org &")
        elif value == "subscribe":
            os.system("xdg-open http://www.elivecd.org/newsletters/ &")
        elif value == "forums":
            os.system("xdg-open http://forum.elivecd.org &")
        # elif value == "tutorials":
            # os.system("xdg-open http://forum.elivecd.org/tutorial &")
        # elif value == "ideas":
            # os.system("xdg-open http://community.linuxmint.com/idea &")
        elif value == "software":
            os.system("sudo synaptic &")
        elif value == "codecs":
            os.system("xbmc &")
        elif value == "office":
            os.system("libreoffice &")

        elif value == "penguins":
            os.system("if test -e /tmp/.emodule_loaded_penguins ; then zenity --info --text='Note: if you see an error, just press F1 in your keyboard' ; enlightenment_remote -module-disable penguins ; enlightenment_remote -module-unload penguins ; rm -f /tmp/.emodule_loaded_penguins ;   else enlightenment_remote -module-load penguins ; enlightenment_remote -module-enable penguins ; touch /tmp/.emodule_loaded_penguins ; chmod a+w /tmp/.emodule_loaded_penguins ; fi")

        elif value == "compiz":
            os.system("if test -e /tmp/.emodule_loaded_ecomorph ; then enlightenment_remote -module-disable ecomorph ; enlightenment_remote -module-unload ecomorph ; rm -f /tmp/.emodule_loaded_ecomorph ;   else enlightenment_remote -module-load ecomorph ; enlightenment_remote -module-enable ecomorph ; touch /tmp/.emodule_loaded_ecomorph ; chmod a+w /tmp/.emodule_loaded_ecomorph ; fi")

        elif value == "help_compiz":
            help_compiz_message = _("Compiz effects (ecomorph) has a bug that makes it unusable, but we want to include it for the stable version, can you help us to solve this problem? (requirements: C programming skills). Note: we suggest you to contact Thanatermesis after to do a look to the issue")
            os.system("if zenity --question --text='%s' ; then xdg-open http://www.github.com/Elive/ecomorph/issues ; fi &" % help_compiz_message)

        elif value == "help_wikipedia":
            os.system("xdg-open http://en.wikipedia.org/wiki/Elive")

        # elif value == "driver":
            # os.system("mintdrivers &")
        # elif value == "hardware":
            # os.system("xdg-open http://community.linuxmint.com/hardware &")
        elif value == "issues":
            os.system("xdg-open http://www.github.com/Elive &")
        # elif value == "sponsors":
            # os.system("xdg-open http://www.linuxmint.com/sponsors.php &")
        elif value == "donors":
            os.system("xdg-open http://www.elivecd.org/donate &")
        elif value == "get_involved":
            os.system("xdg-open http://www.elivecd.org/collaborate &")


if __name__ == "__main__":
    EliveWelcome()
    Gtk.main()
